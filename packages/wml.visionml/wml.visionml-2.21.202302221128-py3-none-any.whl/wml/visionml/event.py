# pylint: disable=import-outside-toplevel

"""Module dealing with getting event information from the muv1 database to the sqlite database
"""

from turbojpeg import TurboJPEG

from mt import tp, np, pd, cv, path, aio, logg
from mt.base import locket, http
import mt.sql.base as sb

from wml.core import home_dirpath, s3, dataframe_processing

from .sqlite import engine
from .conn import muv1rl_engine
from .image import get_parent as image_get_parent

jp = TurboJPEG()


__all__ = [
    "get_weight_g",
    "get_parent",
    "get_menu_id",
    "get_best_images",
    "get_after_images",
    "get_before_images",
    "get_prediction_images",
    "get_data",
    "rectify_thumbnails",
    "visit_events",
    "ensure_field_event_id",
    "ensure_field_menu_id",
]


def get_weight_g(
    event_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets the weight (in gram) of each event from a list of event ids.

    The 'weight_g' field of each event is taken from the muv1db 'public.event' table.

    Parameters
    ----------
    event_id_list : list
        list of integers containing distinct event ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='event_id', columns=['weight_g'])`
        the output dataframe. Some image ids may be missing if they do not exist in the 'event'
        table. Duplicate event ids are removed.
    """

    event_id_list = list(set(event_id_list))
    msg = "Querying {} events for weight_g from muv1db".format(len(event_id_list))
    with logg.scoped_info(msg, logger=logger):
        query_str = ",".join((str(x) for x in event_id_list))
        query_str = "SELECT id AS event_id, weight_g FROM public.event WHERE id IN ({});".format(
            query_str
        )

        return sb.read_sql(
            query_str,
            muv1rl_engine,
            index_col="event_id",
            chunksize=100000,
            logger=logger,
        )


def get_field_data(
    event_id_list: list,
    query_format_str: str,
    table_name: str,
    index_col: str = "event_id",
    missing: str = "warn",
    logger=None,
):
    """TBC"""

    if not isinstance(event_id_list, list):
        raise ValueError(
            "Expected a 'event_id_list' to be a list. Got '{}'.".format(
                type(event_id_list)
            )
        )
    event_id_list = list(set(event_id_list))  # to remove duplicate records
    values = ",".join((str(x) for x in event_id_list))
    query_str = query_format_str.format(values=values)
    if logger:
        logger.info(
            "Querying {} records from wml table '{}'.".format(
                len(event_id_list), table_name
            )
        )
    df = sb.read_sql(
        query_str,
        engine,
        index_col=index_col,
        chunksize=100000,
        logger=logger,
    )

    if len(df) < len(event_id_list):
        if missing == "raise":
            raise ValueError(
                "Requested {} events but returned only {} events.".format(
                    len(event_id_list), len(df)
                )
            )
        elif missing == "warn":
            if logger:
                logger.warn(
                    "Requested {} events but returned only {} events.".format(
                        len(event_id_list), len(df)
                    )
                )
                if len(df) < len(event_id_list) * 0.95:
                    logger.warn(
                        "Maybe run 'mutable_sync.py' or 'mutable_merge_from.py' to update?"
                    )
        else:
            raise ValueError(
                "Unknown value for 'missing' argument: '{}'.".format(missing)
            )

    return df


def get_parent(event_id_list: list, missing: str = "warn", logger=None) -> pd.DataFrame:
    """Gets the installation id of each event from a list of event ids.

    The installation id of each event is taken from the wml 'ml_event_with_prev' table.

    Parameters
    ----------
    event_id_list : list
        list of integers containing distinct event ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='event_id', columns=['installation_id'])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_event_with_prev' table. Duplicate event ids are removed.
    """

    return get_field_data(
        event_id_list,
        "SELECT event_id, installation_id FROM ml_event_with_prev WHERE event_id IN ({values});",
        "ml_event_with_prev",
        index_col="event_id",
        missing=missing,
        logger=logger,
    )


def get_approval_status(
    event_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets the approval status of each event from a list of event ids.

    The approval status of each event is taken from the 'approved' field of the wml
    'ml_event_with_prev' table.

    Parameters
    ----------
    event_id_list : list
        list of integers containing distinct event ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='event_id', columns=['approved'])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_event_with_prev' table. Duplicate event ids are removed.
    """

    return get_field_data(
        event_id_list,
        "SELECT event_id, approved FROM ml_event_with_prev WHERE event_id IN ({values});",
        "ml_event_with_prev",
        index_col="event_id",
        missing=missing,
        logger=logger,
    )


def get_menu_id(
    event_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets the menu id of each event from a list of event ids.

    The menu id of each event is taken from the wml 'ml_event' table.

    Parameters
    ----------
    event_id_list : list
        list of integers containing distinct event ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='event_id', columns=['menu_id'])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_event_with_prev' table. Duplicate event ids are removed.
    """

    return get_field_data(
        event_id_list,
        "SELECT event_id, menu_id FROM ml_event WHERE event_id IN ({values});",
        "ml_event",
        index_col="event_id",
        missing=missing,
        logger=logger,
    )


def get_best_images(
    event_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets all the best/theoretical after image ids of each event from a list of event ids.

    A best image id of each event is taken from the wml 'ml_events' table.

    Parameters
    ----------
    event_id_list : list
        list of integers containing distinct event ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(columns=['event_id', 'best_image_id', 'best_image_type'])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_events' table. It is impossible for an event has more than 1 best image. Duplicate
        event ids are removed.
    """

    msg = "Finding theoretical after images for {} events".format(len(event_id_list))
    with logg.scoped_info(msg, logger=logger):
        return get_field_data(
            event_id_list,
            "SELECT event_id, best_image_id, best_image_type FROM ml_events WHERE event_id IN ({values});",
            "ml_events",
            index_col=None,
            missing=missing,
            logger=logger,
        )


def get_after_images(
    event_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets all the after image ids of each event from a list of event ids.

    A after image id of each event is taken from the wml 'ml_event_image' table.

    Parameters
    ----------
    event_id_list : list
        list of integers containing distinct event ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(columns=['event_id', 'after_image_id'])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_event_image' table. It is very rare, but not impossible, that an event has more than 1
        after image. Duplicate event ids are removed.
    """

    return get_field_data(
        event_id_list,
        "SELECT event_id, image_id AS after_image_id FROM ml_event_image WHERE event_id IN ({values}) AND is_after;",
        "ml_event_image",
        index_col=None,
        missing=missing,
        logger=logger,
    )


def get_before_images(
    event_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets all the before image ids of each event from a list of event ids.

    A before image id of each event is taken from the wml 'ml_event_image' table.

    Parameters
    ----------
    event_id_list : list
        list of integers containing distinct event ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(columns=['event_id', 'before_image_id'])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_event_image' table. It is very rare, but not impossible, that an event has more than 1
        before image. Duplicate event ids are removed.
    """

    msg = "Finding before images for {} events".format(len(event_id_list))
    with logg.scoped_info(msg, logger=logger):
        return get_field_data(
            event_id_list,
            "SELECT event_id, image_id AS before_image_id FROM ml_event_image WHERE event_id IN ({values}) AND is_before;",
            "ml_event_image",
            index_col=None,
            missing=missing,
            logger=logger,
        )


def get_prediction_images(
    event_id_list: list, missing: str = "warn", logger=None
) -> pd.DataFrame:
    """Gets all the prediction image ids of each event from a list of event ids.

    A prediction image id of each event is taken from the wml 'ml_event_image' table. If it does
    not exist, we get the after image.

    Parameters
    ----------
    event_id_list : list
        list of integers containing distinct event ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(columns=['event_id', 'prediction_image_id', 'prediction_image_type'])`
        the output dataframe. Some image ids may be missing if they do not exist in the wml
        'ml_event_image' table. It is very rare, but not impossible, that an event has more than 1
        prediction image. Duplicate event ids are removed.
    """

    event_cnt = len(event_id_list)
    msg = "Finding prediction images for {} events".format(event_cnt)
    with logg.scoped_info(msg, logger=logger):
        df = get_field_data(
            event_id_list,
            "SELECT event_id, image_id AS prediction_image_id FROM ml_event_image WHERE event_id IN ({values}) AND is_prediction;",
            "ml_event_image",
            index_col=None,
            missing="warn",
            logger=logger,
        )
        df["prediction_image_type"] = "PREDICTION_IMAGE"

        event_id_list2 = list(set(event_id_list) - set(df["event_id"].tolist()))
        if not event_id_list2:
            return df

        if logger:
            logger.info(
                "Attempting to fill in {}/{} events without a prediction image with their "
                "associated after images.".format(len(event_id_list2), event_cnt)
            )
        df2 = get_after_images(event_id_list2, missing=missing, logger=logger)
        df2.columns = ["event_id", "prediction_image_id"]
        df2["prediction_image_type"] = "AFTER_IMAGE"

        return pd.concat([df, df2], sort=False)


# ----- event data -----


def get_data_filepath(installation_id: int, event_id: int) -> str:
    dirpath = path.join(
        home_dirpath, "event_data", "inst_{:05d}".format(installation_id)
    )
    path.make_dirs(dirpath)
    return path.join(dirpath, "event_{:09d}.pdh5".format(event_id))


async def get_thumbnail(
    event_id: int, image_id: int, url: str, context_vars: dict = {}, logger=None
) -> bytes:
    thumb_url = url + ".400"
    s3_filepath = s3.cache_localpath(s3.as_s3cmd_url(thumb_url))
    if path.exists(s3_filepath):
        if logger:
            logger.debug(
                "make_dataframe(event_id={event_id})'s thumbnail {image_id}: from S3 cache".format(
                    event_id=event_id, image_id=image_id
                )
            )
        data = await aio.read_binary(s3_filepath, context_vars=context_vars)
        if len(data) > 1000:
            return data

    phong_filepath = path.join(
        "/data/phong/data/sam-remastered/images",
        str(event_id),
        "{}.jpg".format(image_id),
    )
    if path.exists(phong_filepath):
        if logger:
            logger.debug(
                "make_dataframe(event_id={event_id})'s thumbnail {image_id}: from Phong's cache".format(
                    event_id=event_id, image_id=image_id
                )
            )
        data = await aio.read_binary(phong_filepath, context_vars=context_vars)
        if len(data) > 1000:
            return data

    if logger:
        logger.debug(
            "make_dataframe(event_id={event_id})'s thumbnail {image_id}: from web".format(
                event_id=event_id, image_id=image_id
            )
        )
    return await http.download(
        thumb_url, context_vars=context_vars
    )  # TODO: check for server disconnection here


async def make_dataframe(
    installation_id: int,
    event_id: int,
    context_vars: dict = {},
    logger=None,
    verbosity: int = 0,
):
    if verbosity == 0:
        if logger:
            logger.debug(
                "Making the data of event {} of installation {}.".format(
                    event_id, installation_id
                )
            )

    # get all images and their records
    query_str = "SELECT image_id FROM ml_event_image WHERE event_id={};".format(
        event_id
    )
    df = sb.read_sql(query_str, engine, logger=logger)
    if len(df) == 0:
        raise ValueError(
            "There is no record of any image for event {}. Maybe run script 'mutable_sync.py' or 'mutable_merge_from.py'?".format(
                event_id
            )
        )

    image_id_list = df["image_id"].drop_duplicates().tolist()
    query_str = ",".join((str(x) for x in image_id_list))
    query_str = (
        "SELECT id AS image_id, url, taken_at FROM ml_image WHERE id IN ({})".format(
            query_str
        )
    )
    df = sb.read_sql(query_str, engine, chunksize=100000, logger=logger)
    df = df.sort_values("taken_at").groupby("image_id").head(1)
    if len(df) != len(image_id_list):
        raise ValueError(
            "Requested {} image records but {} returned.".format(
                len(image_id_list), len(df)
            )
        )

    thumbnail_list = []
    for _, row in df.iterrows():
        data = await get_thumbnail(
            event_id,
            row["image_id"],
            row["url"],
            context_vars=context_vars,
            logger=logger if verbosity > 0 else None,
        )
        arr = np.frombuffer(data, dtype=np.uint8)
        thumbnail_list.append(arr)
    df["thumbnail"] = thumbnail_list

    return df


async def get_data(
    event_id: int,
    level: int = 3,
    installation_id: tp.Optional[int] = None,
    context_vars: dict = {},
    logger=None,
    verbosity: int = 0,
) -> pd.DataFrame:
    """An asyn function that gets the event data, depending on the level of details.

    Parameters
    ----------
    event_id : int
        event id
    level : int
        Level of details to be returned. Level 0 justs makes sure the data is available. Level 1
        includes image ids. Level 2 includes image ids and their urls. Level 3 includes image ids,
        their urls and their acquisition times. Level 4 includes level 3 and all the thumbnails
        jpeg-formatted bytes wrapped in numpy arrays.
    installation_id : int, optional
        the id of the installation/site containing the event. If not provided, :func:`get_parent`
        is invoked, which may cost some time.
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
        Variable 's3_client' must exist and hold an enter-result of an async with statement
        invoking :func:`mt.base.s3.create_s3_client`. In asynchronous mode, variable
        'http_session' must exist and hold an enter-result of an async with statement invoking
        :func:`mt.base.http.create_http_session`. You can use
        :func:`wml.core.s3.create_context_vars` to create a dictionary like this.
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes
    verbosity : int
        level of verbosity if the logger is provided. 0 for brief. 1 for full.

    Returns
    -------
    pandas.DataFrame
        list of image records, each of which contains 'image_id', 'url', 'taken_at' and 'thumbnail'
        fields according to the level of interest.

    Notes
    -----
    The full data of an event is in the form of a pdh5 file. If the data does not exist, it will
    take some time to make the pdh5 file by downloading from S3. Hence async is needed so things
    can be done in parallel.
    """

    if installation_id is None:
        event_df = get_parent(
            [event_id], missing="raise", logger=logger if verbosity > 0 else None
        )
        installation_id = event_df.iloc[0]["installation_id"]

    filepath = get_data_filepath(installation_id, event_id)

    with locket.lock_file(
        filepath + ".LCK"
    ):  # make sure only one process/atask accesses the event
        if path.exists(filepath):
            if level == 0:
                return
            df = await pd.dfload_asyn(
                filepath, file_read_delayed=(level <= 3), context_vars=context_vars
            )
        else:
            df = await make_dataframe(
                installation_id,
                event_id,
                context_vars=context_vars,
                logger=logger,
                verbosity=verbosity,
            )
            await pd.dfsave_asyn(df, filepath, context_vars=context_vars)

        # df is expected to have columns: image_id, url, taken_at, and thumbnail
        # but thumbnail might be delay-loaded
        if level == 0:
            return
        if level == 1:
            return df[["image_id"]]
        if level == 2:
            return df[["image_id", "url"]]
        if level == 3:
            return df[["image_id", "url", "taken_at"]]
        if level == 4:
            return df

        raise ValueError("Unknown level value {}.".format(level))


def rectify_thumbnails(s: pd.Series) -> pd.Series:
    """Rectifies all thumbls in a pandas.Series to be loaded and to have 400x300 resolution.

    Parameters
    ----------
    s : pandas.Series
        a series of thumbnails, loaded or not, in numpy.array containers of jpeg-formatted bytes

    Returns
    -------
    pandas.Series
        another series where each cell is a 400x300 numpy.array
    """

    def func(item):
        if isinstance(item, pd.Pdh5Cell):
            item = item.value

        if not isinstance(item, np.ndarray):
            raise ValueError("Item is not a numpy array. Got: {}.".format(type(item)))

        item = bytes(item.data)  # ndarray to bytes
        item = jp.decode(item)  # jpeg-decode

        if not isinstance(item, np.ndarray):
            raise ValueError("Item is not a numpy array. Got: {}.".format(type(item)))
        if len(item.shape) != 3 and item.shape[2] != 3:
            raise ValueError("Item is not an image. Got: {}.".format(item.shape))

        if item.shape[0] != 300 and item.shape[1] != 400:
            item = cv.resize(item, (400, 300))

        return item

    return s.apply(func)


async def visit_events(
    event_id_list: list,
    max_concurrency: int = 16,
    context_vars: dict = {},
    logger=None,
    verbosity: int = 0,
) -> list:
    """An asyn function that visits all events of an event list to make sure their data are available.

    Parameters
    ----------
    event_id_list : list
        list of integers containing the event ids
    max_concurrency : int
        the maximum number of concurrent works in each context at any time, good for managing
        memory allocations. If None is given, all works in each context will be scheduled to run at
        once.
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
        Variable 's3_client' must exist and hold an enter-result of an async with statement
        invoking :func:`mt.base.s3.create_s3_client`. In asynchronous mode, variable
        'http_session' must exist and hold an enter-result of an async with statement invoking
        :func:`mt.base.http.create_http_session`. You can use
        :func:`wml.core.s3.create_context_vars` to create a dictionary like this.
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes
    verbosity : int
        level of verbosity if the logger is provided. 0 for progress bar. 1 for brief. 2 for full.

    Returns
    -------
    list
        a list of unvisitable events
    """

    event_cnt = len(event_id_list)

    if verbosity > 0:
        if logger:
            logger.info(
                "Obtaining the installation ids of {} events.".format(event_cnt)
            )
    df = get_parent(
        event_id_list, missing="raise", logger=logger if verbosity > 0 else None
    )
    df = df.reset_index(
        drop=False
    )  # to have 'event_id' and 'installation_id' as columns
    if len(df) != event_cnt:
        raise ValueError(
            "Requested the installation ids of {} events but got {} records.".format(
                event_cnt, len(df)
            )
        )

    async def preprocess(
        s: pd.Series,
        iter_id: int,
        rng_seed: int,
        *args,
        context_vars: dict = {},
        logger=None,
        verbosity: int = 0,
        **kwargs
    ):
        event_id = s["event_id"]
        installation_id = s["installation_id"]
        try:
            await get_data(
                event_id,
                level=0,
                installation_id=installation_id,
                context_vars=context_vars,
                logger=logger,
                verbosity=verbosity,
            )
            res = True
        except:
            if logger:
                logger.warn_last_exception()
                logger.warn(
                    "Skipped visiting event {} due to the above exception.".format(
                        event_id
                    )
                )
            res = False
        return pd.Series(data={"event_id": event_id, "done": res})

    if verbosity == 0:
        func_kwargs = {"logger": None, "verbosity": 0}
    else:
        func_kwargs = {"logger": logger, "verbosity": verbosity - 1}

    for i in range(3):
        df2 = await dataframe_processing.process_dataframe(
            df,
            preprocess,
            preprocess_kwargs=func_kwargs,
            max_concurrency=8,
            context_vars=context_vars,
            logger=logger,
        )
        done_cnt = df2["done"].sum()
        if done_cnt < event_cnt:
            if logger:
                logger.info(
                    "At round {}, {} events have been visited.".format(i + 1, done_cnt)
                )
            df2 = df2[~df2["done"]].set_index("event_id", drop=True)
            df = df.join(df2, on="event_id", how="inner")
            event_cnt = len(df)
        else:
            event_cnt = 0
            break  # job done

    if event_cnt == 0:
        return []

    return df["event_id"].drop_duplicates().tolist()


def ensure_field_event_id(
    df: pd.DataFrame, image_id_field: str = "image_id", logger=None
):
    """Ensures that the dataframe has field 'event_id'.

    The function checks if there is a field 'event_id' in the input dataframe. If there is not, it
    requires the dataframe have an image id field specified by argument 'image_id_field' and then
    it generates the field 'event_id' with data from the wml database. Null event ids will be set
    to -1.

    Parameters
    ----------
    df : pandas.DataFrame
        input dataframe
    image_id_field : str
        name of the field containing the image ids
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        output dataframe
    """

    if "event_id" in df.columns:
        return df

    with logg.scoped_warn(
        "Making field 'event_id' with data from wml database", logger=logger
    ):
        event_df = image_get_parent(
            df[image_id_field].drop_duplicates().tolist(), logger=logger
        )
        df = df.join(event_df, on=image_id_field, how="left")
        df["event_id"] = df["event_id"].fillna(-1).astype(int)
    return df


def ensure_field_menu_id(
    df: pd.DataFrame, image_id_field: str = "image_id", logger=None
):
    """Ensures that the dataframe has field 'menu_id'.

    The function checks if there is a field 'menu_id' in the input dataframe. If there is not, it
    requires the dataframe have field 'event_id' and then it generates the field 'menu_id' with
    data from the wml database. Null menu ids will be set to -1.

    Parameters
    ----------
    df : pandas.DataFrame
        input dataframe
    image_id_field : str
        name of the field containing the image ids, in case we need to generate field 'event_id'
        via invoking :func:`ensure_field_event_id`
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        output dataframe
    """

    if "menu_id" in df.columns:
        return df

    df = ensure_field_event_id(df, image_id_field=image_id_field, logger=logger)

    with logg.scoped_warn(
        "Making field 'menu_id' with data from wml database.", logger=logger
    ):
        menu_df = get_menu_id(df["event_id"].drop_duplicates().tolist(), logger=logger)
        df = df.join(menu_df, on="event_id", how="left")
        df["menu_id"] = df["menu_id"].fillna(-1).astype(int)
    return df
