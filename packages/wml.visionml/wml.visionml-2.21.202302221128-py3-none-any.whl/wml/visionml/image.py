# pylint: disable=import-outside-toplevel

"""Module dealing with getting image information from the muv1 database to the sqlite database
"""

from mt import tp, np, pd, aio
import mt.sql.base as sb

from wml.core import s3_bulk as s3b, imageio

from .sqlite import engine


__all__ = [
    "get_attributes",
    "get_parent",
    "get_edge_bin_crop",
    "get_image_files_asyn",
    "get_image_files",
    "load_asyn",
    "load",
]


def get_attributes(
    image_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets the image attributes of each image from a list of image ids.

    The image attributes are taken from the 'ml_image' table of the wml database. Currently, the
    following fields are returned 'id', 'url', 'width', 'height' and 'taken_at'.

    Parameters
    ----------
    image_id_list : list
        list of integers containing the image ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='id', columns=['url', 'width', 'height', 'taken_at'])`
        the dataframe of all metadata for the given image ids. Some image ids may be missing if
        they do not exist in the 'ml_image' table of the wml database. Duplicate image ids are
        removed.
    """

    if not isinstance(image_id_list, list):
        raise ValueError(
            "Expected a 'image_id_list' to be a list. Got '{}'.".format(
                type(image_id_list)
            )
        )
    image_id_list = list(set(image_id_list))
    values = ",".join((str(x) for x in image_id_list))
    query_str = "SELECT * FROM ml_image WHERE id IN ({values});".format(values=values)
    if logger:
        logger.info(
            "Querying {} records from table 'ml_image' of wml database.".format(
                len(image_id_list)
            )
        )
    df = sb.read_sql(query_str, engine, chunksize=100000, logger=logger)

    # make it unique for each image id
    df = df.sort_values(["id", "updated"]).groupby("id").tail(1)
    df = df.drop("updated", axis=1)
    df = df.set_index("id", drop=True)

    if len(df) < len(image_id_list):
        if missing == "raise":
            raise ValueError(
                "Requested {} images but returned only {} images.".format(
                    len(image_id_list), len(df)
                )
            )
        elif missing == "warn":
            if logger:
                logger.warn(
                    "Requested {} images but returned only {} images.".format(
                        len(image_id_list), len(df)
                    )
                )
                if len(df) < len(image_id_list) * 0.95:
                    logger.warn(
                        "Maybe run 'mutable_sync.py' or 'mutable_merge_from.py' to update?"
                    )
        else:
            raise ValueError(
                "Unknown value for 'missing' argument: '{}'.".format(missing)
            )

    # check for missing values
    for c in df.columns:
        s = df[c].isnull()
        if s.sum() > 0:
            if missing == "raise":
                raise ValueError(
                    "Detected {} images with missing '{}'.".format(s.sum(), c)
                )
            elif missing == "warn":
                if logger:
                    logger.warn(
                        "Removed {} images with missing '{}'.".format(s.sum(), c)
                    )
                df = df[~s]
            else:
                raise ValueError(
                    "Unknown value for 'missing' argument: '{}'.".format(missing)
                )
    return df


def get_parent(
    image_id_list: list,
    with_grandparent: bool = True,
    missing: str = "warn",
    logger=None,
) -> pd.DataFrame:
    """Gets the event id and optionally the installation id of each image from a list of image ids.

    The event id of each image is taken from the wml 'ml_event_image' table. If allowed, the
    installation id is obtained by invoking :func:`wml.visionml.event.get_parent`.

    Parameters
    ----------
    image_id_list : list
        list of integers containing the image ids
    with_grandparent: bool, optional
        whether to obtain the installation id as well (True) or not
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='image_id', columns=['event_id'[, 'installation_id']])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_event_image' or 'ml_event_with_prev' tables. Duplicate image ids are removed.

    Notes
    -----
    In case an image appears in more than one event, the event with the largest id will be
    returned.
    """

    if not isinstance(image_id_list, list):
        raise ValueError(
            "Expected a 'image_id_list' to be a list. Got '{}'.".format(
                type(image_id_list)
            )
        )
    image_id_list = list(set(image_id_list))
    values = ",".join((str(x) for x in image_id_list))
    query_str = "SELECT image_id, event_id FROM ml_event_image WHERE image_id IN ({values});".format(
        values=values
    )
    if logger:
        logger.info(
            "Querying {} records from wml table 'ml_event_image'.".format(
                len(image_id_list)
            )
        )
        df = sb.read_sql(query_str, engine, chunksize=100000, logger=logger)

    # make it unique for each image id
    df = df.sort_values(["image_id", "event_id"]).groupby("image_id").tail(1)
    df = df.set_index("image_id", drop=True)

    if with_grandparent:
        from .event import get_parent as event_get_parent

        df2 = event_get_parent(
            df["event_id"].drop_duplicates().tolist(), missing=missing, logger=logger
        )
        df = df.join(df2, on="event_id", how="inner")

    if len(df) < len(image_id_list):
        if missing == "raise":
            raise ValueError(
                "Requested {} images but returned only {} images.".format(
                    len(image_id_list), len(df)
                )
            )
        elif missing == "warn":
            if logger:
                logger.warn(
                    "Requested {} images but returned only {} images.".format(
                        len(image_id_list), len(df)
                    )
                )
                logger.warn(
                    "Maybe run 'mutable_sync.py' or 'mutable_merge_from.py' to update?"
                )
        else:
            raise ValueError(
                "Unknown value for 'missing' argument: '{}'.".format(missing)
            )

    return df


def get_edge_bin_crop(
    image_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets a system-picked bin crop for each image id, if the crop exists.

    Parameters
    ----------
    image_id_list : list
        list of integers containing the image ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='image_id', columns=['crop'])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_edge_bin_crop' and 'public_image' tables. Each crop is in the format
        `[min_x/width, min_y/height, max_x/width, max_y/height]`. Duplicate image ids are removed.
    """

    if not isinstance(image_id_list, list):
        raise ValueError(
            "Expected a 'image_id_list' to be a list. Got '{}'.".format(
                type(image_id_list)
            )
        )
    image_id_list = list(set(image_id_list))
    values = ",".join((str(x) for x in image_id_list))
    query_str = "SELECT image_id, min_x, min_y, max_x, max_y FROM ml_edge_bin_crop WHERE image_id IN ({values});".format(
        values=values
    )
    if logger:
        logger.info(
            "Querying {} crops from wml table 'ml_edge_bin_crop'.".format(
                len(image_id_list)
            )
        )
        df = sb.read_sql(query_str, engine, chunksize=100000, logger=logger)

    if len(df) < len(image_id_list):
        msg = "Only {} crops returned.".format(len(df))
        if missing == "raise":
            if logger:
                logger.error(msg)
            raise ValueError(
                "Asked for {} system-picked crops but only {} returned.".format(
                    len(image_id_list), len(df)
                )
            )

        if logger:
            logger.warn(msg)
        image_id_list = df["image_id"].drop_duplicates().tolist()

    if len(df) == 0:
        df = pd.DataFrame(columns=["crop"])
        df.index.name = "image_id"
        return df

    image_df = get_attributes(image_id_list, missing=missing, logger=logger)[
        ["width", "height"]
    ]
    df = df.set_index("image_id", drop=True).join(image_df, how="inner")

    if len(df) < len(image_id_list):
        msg = "Asked for the attributes of {} images but only {} returned.".format(
            len(image_id_list), len(df)
        )
        if missing == "raise":
            raise ValueError(msg)
        if logger:
            logger.warn(msg)

    if len(df) == 0:
        df = pd.DataFrame(columns=["crop"])
        df.index.name = "image_id"
        return df

    def func(row):
        min_x = row["min_x"]
        min_y = row["min_y"]
        max_x = row["max_x"]
        max_y = row["max_y"]
        w = row["width"]
        h = row["height"]

        if np.isnan([min_x, min_y, max_x, max_y, w, h]).any():
            return None

        return [min_x / w, min_y / h, max_x / w, max_y / h]

    s = df.apply(func, axis=1)
    df["crop"] = s
    if df["crop"].isnull().sum() > 0:
        df = [df["crop"].notnull()]
        msg = "Nan values detected in {}/{} crops.".format(len(df), len(image_id_list))
        if missing == "raise":
            raise ValueError(msg)
        elif logger:
            logger.warn(msg)

    return df[["crop"]]


async def get_image_files_asyn(
    image_id_list: list,
    use_thumbnails: bool = False,
    context_vars: dict = {},
    profile=None,
    logger=None,
) -> pd.DataFrame:
    """An asyn function that does everything needed to go from image ids to downloaded image files.

    The function starts with synchronising from muv1db to make sure all the image urls are
    identified. It then downloads all images that have not been downloaded, asynchronously
    and with multiprocessing. It finallly composes an output table.

    Parameters
    ----------
    image_id_list : list or int
        list of integers containing the image ids
    use_thumbnails : bool
        whether get the thumbnails (400-width) or not (False)
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
    profile : str, optional
        one of the profiles specified in the AWS credentials file. The default is used if None is
        given.
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    df : `pandas.DataFrame(index='id', columns=['s3cmd_url', 'local_filepath', 'image_type', 'image_width', 'image_height'])`
        A dataframe containing the corresponding list of s3cmd urls, list of image local_filepaths
        and list of image types (None to represent an invalid image). Some image ids may be
        skipped if they do not exist in the database. Duplicate image ids are removed.

    Notes
    -----
    This function combines the power of multiprocessing and asyncio. It shines when you have
    millions of files to inspect.
    """
    df = get_attributes(image_id_list, logger=logger)
    s = df["url"]
    s = s[s.notnull()]
    if use_thumbnails:
        s = s.apply(lambda x: x + ".400")
    df = await s3b.inspect_images_asyn(
        s, context_vars=context_vars, profile=profile, logger=logger
    )
    return df


def get_image_files(
    image_id_list: list, use_thumbnails: bool = False, profile=None, logger=None
) -> pd.DataFrame:
    """Does everything needed to go from image ids to downloaded image files.

    The function starts with synchronising from muv1db to make sure all the image urls are
    identified. It then downloads all images that have not been downloaded, asynchronously
    and with multiprocessing. It finallly composes an output table.

    Parameters
    ----------
    image_id_list : list or int
        list of integers containing the image ids
    use_thumbnails : bool
        whether get the thumbnails (400-width) or not (False)
    profile : str, optional
        one of the profiles specified in the AWS credentials file. The default is used if None is
        given.
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    df : `pandas.DataFrame(index='id', columns=['s3cmd_url', 'local_filepath', 'image_type', 'image_width', 'image_height'])`
        A dataframe containing the corresponding list of s3cmd urls, list of image local_filepaths
        and list of image types (None to represent an invalid image). Some image ids may be
        skipped if they do not exist in the database. Duplicate image ids are removed.

    Notes
    -----
    This function combines the power of multiprocessing and asyncio. It shines when you have
    millions of files to inspect.
    """

    return aio.srun(
        get_image_files_asyn,
        image_id_list,
        use_thumbnails=use_thumbnails,
        profile=profile,
        logger=logger,
    )


async def load_asyn(
    image_id: int,
    image_url: tp.Optional[str] = None,
    plugin: tp.Optional[str] = None,
    extension: tp.Optional[str] = None,
    format_hint: tp.Optional[str] = None,
    plugin_kwargs: dict = {},
    context_vars: dict = {},
    logger=None,
) -> np.ndarray:
    """Loads an image from file.
    Parameters
    ----------
    image_id : int
        the image id
    image_url : str, optional
        the image url, if known. Local filepaths, s3cmd urls, http urls and https urls are
        accepted. If not provided, the url is extracted from the database, incurring some time to
        process.
    plugin : str, optional
        keyword argument to be passed as-is to :func:`wml.core.imageio.imread_asyn`
    extension : str, optional
        keyword argument to be passed as-is to :func:`wml.core.imageio.imread_asyn`
    format_hint : str, optional
        keyword argument to be passed as-is to :func:`wml.core.imageio.imread_asyn`
    plugin_kwargs : dict
        keyword argument to be passed as-is to :func:`wml.core.imageio.imread_asyn`
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
        Variable 's3_client' must exist and hold an enter-result of an async with statement
        invoking :func:`mt.base.s3.create_s3_client`. In asynchronous mode, variable
        'http_session' must exist and hold an enter-result of an async with statement invoking
        :func:`mt.base.http.create_http_session`. You can use
        :func:`wml.core.s3.create_context_vars` to create a dictionary like this.
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    numpy.ndarray
        the loaded image

    Raises
    ------
    OSError
        when it is unable to load an image file

    See Also
    --------
    wml.core.imageio.imread_asyn
        the wrapped function for loading an image file
    """

    if image_url is None:
        image_url = get_attributes([image_id], logger=logger)["url"].iloc[0]
        if logger:
            logger.debug("Image ({}) url: {}".format(image_id, image_url))

    try:
        image = imageio.imread(
            image_url,
            plugin=plugin,
            extension=extension,
            format_hint=format_hint,
            plugin_kwargs=plugin_kwargs,
            logger=logger,
        )
    except:
        if logger:
            logger.warn_last_exception()
            logger.warn("Unable to load wml image file:")
            logger.warn("  Id: {}".format(image_id))
            logger.warn("  Url: {}".format(image_url))
        raise OSError(
            "Unable to load wml image file ({}) at '{}'.".format(image_id, image_url)
        )

    return image


def load(
    image_id: int,
    image_url: tp.Optional[str] = None,
    plugin: tp.Optional[str] = None,
    extension: tp.Optional[str] = None,
    format_hint: tp.Optional[str] = None,
    plugin_kwargs: dict = {},
    context_vars: dict = {},
    logger=None,
) -> np.ndarray:
    """Loads an image from file.
    Parameters
    ----------
    image_id : int
        the image id
    image_url : str, optional
        the image url, if known. Local filepaths, s3cmd urls, http urls and https urls are
        accepted. If not provided, the url is extracted from the database, incurring some time to
        process.
    plugin : str, optional
        keyword argument to be passed as-is to :func:`wml.core.imageio.imread_asyn`
    extension : str, optional
        keyword argument to be passed as-is to :func:`wml.core.imageio.imread_asyn`
    format_hint : str, optional
        keyword argument to be passed as-is to :func:`wml.core.imageio.imread_asyn`
    plugin_kwargs : dict
        keyword argument to be passed as-is to :func:`wml.core.imageio.imread_asyn`
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    numpy.ndarray
        the loaded image

    Raises
    ------
    OSError
        when it is unable to load an image file

    See Also
    --------
    wml.core.imageio.imread_asyn
        the wrapped function for loading an image file
    """

    return aio.srun(
        load_asyn,
        image_id,
        image_url=image_url,
        plugin=plugin,
        extension=extension,
        format_hint=format_hint,
        plugin_kwargs=plugin_kwargs,
        logger=logger,
    )
