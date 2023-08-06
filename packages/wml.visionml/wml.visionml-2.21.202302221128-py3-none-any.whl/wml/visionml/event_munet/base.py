# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

import json
import shutil

from mt import tp, pd, path, logg

from wml.core import s3

from ..params import EventMunetLoadingOptions
from ..event import ensure_field_menu_id
from ..image import get_attributes
from .reweight import ensure_field_ml_weight
from .menu import extract_slice2menu_code_mappings
from .taxcode import (
    ensure_field_menu_code,
    ensure_field_slice_codes,
)
from .kind import ensure_field_ml_kind
from .prediction_context import ensure_field_prediction_context
from .after_image import ensure_field_after_image_id
from .before_image import ensure_field_before_image_id
from .segm import ensure_field_use_segmentation
from .target_taxcode_distribution import load_fr_problem_asyn


async def load(
    path_or_url,
    options: EventMunetLoadingOptions = EventMunetLoadingOptions(),
    context_vars: dict = {},
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """An asyn function that loads an equivalent event_munet.csv file from disk or S3.

    Apart from loading it preprocesses some key fields, like making some fields integer.

    Parameters
    ----------
    path_or_url : str
        local filepath (or s3cmd url) to a dataframe file equivalent to the data team's
        event_munet.csv file
    options : EventMunetLoadingOptions
        options to load the file
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
        Variable 's3_client' must exist and hold an enter-result of an async with statement
        invoking :func:`mt.base.s3.create_s3_client`. In asynchronous mode, variable
        'http_session' must exist and hold an enter-result of an async with statement invoking
        :func:`mt.base.http.create_http_session`. You can use
        :func:`wml.core.s3.create_context_vars` to create a dictionary like this.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    event_munet_df : pandas.DataFrame
        the loaded and preprocessed event_munet dataframe
    l_taxcodes : list, optional
        the loaded taxcode list or None if no file is not found
    frp : wml.core.datatype.FRProblem, optional
        the food recognition problem, or None if the file does not exist
    slice2menu_df : pandas.DataFrame
        the dataframe containing the mappings. It has 3 columns
        ``['menu_id', 'slice_code', 'menu_code']`` but each slice code is a unique string.
    slice2menu_conflicts_df : pandas.DataFrame or None
        If there is a conflict in the slice2menu mappings, this output argument is a dataframe with
        5 columns ``['event_id', 'menu_id', 'slice_code', 'menu_code', 'count']``. If there is no
        conflict, `conflicts_df` is None.
    """

    msg = "Loading event_munet dataframe '{}'".format(path_or_url)
    with logg.scoped_info(msg, logger=logger):
        filepath = (
            await s3.cache_asyn(path_or_url, context_vars=context_vars, logger=logger)
            if "://" in path_or_url
            else path_or_url
        )
        df = await pd.dfload_asyn(
            filepath, show_progress=logger is not None, context_vars=context_vars
        )

    filepath2 = path.join(path.dirname(filepath), "target_taxcode_distribution.csv")
    l_taxcodes, frp = await load_fr_problem_asyn(
        filepath2, context_vars=context_vars, logger=logger
    )

    # check for duplicate events
    event_cnt = len(df)
    distinct_event_cnt = len(df["event_id"].drop_duplicates())
    if distinct_event_cnt < event_cnt:
        if logger:
            msg = "Duplicate events detected. Restricted to {}/{} distinct events.".format(
                distinct_event_cnt, event_cnt
            )
            logger.error(msg)
        df = df.groupby("event_id").head(1).reset_index(drop=False)
        event_cnt = len(df)

    df["event_id"] = df["event_id"].astype(int)
    event_id_list = df["event_id"].tolist()

    df = ensure_field_ml_weight(df, missing="warn", logger=logger)

    df = ensure_field_ml_kind(df, logger=logger)

    df = ensure_field_prediction_context(df, logger=logger)

    df = ensure_field_menu_id(df, logger=logger)
    df1 = df[df["menu_id"] >= 0]
    if len(df1) < len(df):
        msg = "Removed {} records without a menu.".format(len(df) - len(df1))
        logg.warn(msg)
        df = df1

    df = ensure_field_menu_code(df, drop_old=False, logger=logger)

    df = ensure_field_slice_codes(df, drop_old=True, logger=logger)
    s = df["slice_codes"].isnull()
    if s.sum() > 0:
        if logger:
            logger.warn("Removed {} events with null slice_codes:".format(s.sum()))
            logger.warn("  {}".format(df[s]))
    df = df[~s]

    slice2menu_df, slice2menu_conflicts_df = extract_slice2menu_code_mappings(
        df, l_sliceCodes=l_taxcodes, handle_conflicts="warn", logger=logger
    )

    df = ensure_field_after_image_id(df, options=options, logger=logger)

    df = ensure_field_before_image_id(df, options=options, logger=logger)

    df = ensure_field_use_segmentation(df, options=options, logger=logger)

    # determine fields to be cleaned up
    drop_fields = []
    for prefix in [None, "system", "theoretical"]:
        for midfix in ["before", "after"]:
            for postfix in ["id", "url", "width", "height", "taken_at", "valid"]:
                field_name = midfix if prefix is None else prefix + "_" + midfix
                field_name += "_image_" + postfix
                if field_name in [
                    "before_image_id",
                    "before_image_valid",
                    "after_image_id",
                ]:
                    continue
                if field_name in df.columns:
                    drop_fields.append(field_name)

    df = df.drop(drop_fields, axis=1)

    # fill in image columns using :func:`wml.visionml.image.get_attributes`.
    # MT-TODO: fix me. Do not use missing='warn' and then join with 'inner'.
    # We lose the original ml_weights distribution due to the missing events.
    image_columns = ["width", "height", "url", "taken_at"]
    for prefix in ["before", "after"]:
        msg = "Filling missing '{}_image_...' fields".format(prefix)
        with logg.scoped_info(msg, logger=logger):
            field_name = prefix + "_image_id"
            df1 = df[df[field_name].notnull()]
            image_id_list = df1[field_name].astype(int).drop_duplicates().tolist()
            image_df = get_attributes(image_id_list, missing="warn", logger=logger)
            column_map = {x: prefix + "_image_" + x for x in image_columns}
            image_df = image_df.rename(columns=column_map)
            df = df.join(image_df, on=prefix + "_image_id", how="inner")
            msg = "Inserted columns {} for {} images.".format(image_columns, prefix)
            logg.info(msg, logger=logger)

    # make some fields integer
    columns = [
        "event_id",
        "menu_id",
        "before_image_id",
        "before_image_valid",
        "before_image_width",
        "before_image_height",
        "after_image_id",
        "after_image_width",
        "after_image_height",
        "client_region_id",
        "use_segmentation",
    ]
    for x in columns:
        if x not in df.columns:
            continue
        df[x] = df[x].astype(int)

    return df, l_taxcodes, frp, slice2menu_df, slice2menu_conflicts_df


def process_taxcodes(
    taxcode_str: str, logger: tp.Optional[logg.IndentedLoggerAdapter] = None
) -> tp.List[str]:
    """Converts a json string representing a taxcode or a list of taxcodes into a list.

    TBC MT-TODO
    """

    if isinstance(taxcode_str, bytes):
        taxcode_str = taxcode_str.decode()

    if (not isinstance(taxcode_str, str)) or (not taxcode_str):
        return []

    if taxcode_str[0] != "[":
        return [taxcode_str]

    try:
        item = json.loads(taxcode_str)
    except json.decoder.JSONDecodeError:
        if logger:
            logger.warn_last_exception()
            logger.warn("Unable to decode taxcode string '{}'.".format(taxcode_str))
        raise

    return item


def extract_taxcode_list(
    s: pd.Series, logger: tp.Optional[logg.IndentedLoggerAdapter] = None
) -> tp.List[str]:
    """Extracts a sorted list of taxcodes from a series.

    Each item of the series can be a string a or a list of strings representing the true taxcodes.
    """

    the_set = {}
    for _, l_taxcodes in s.iteritems():
        l_taxcodes = process_taxcodes(l_taxcodes, logger=logger)
        the_set = the_set.union(l_taxcodes)
    return sorted(list(the_set))


def download_from_s3(event_munet_s3cmd_url: str, model_family: str, logger=None):
    """Downloads event_munet.csv from an s3cmd url and optionally the target_...csv files.

    Parameters
    ----------
    event_munet_s3cmd_url : str
        http/https url or s3cmd url to the 'event_munet.csv' file. If the url ends up with '/', it
        will be appended with 'event_munet.csv'.
    model_family : {'vfr', 'munet', 'ffe'}
        model family
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    src_dirurl : str
        s3cmd url to the folder containing the 'event_munet.csv' file
    data_dirpath : str
        local path to the directory containing the downloaded data
    """

    if not "://" in event_munet_s3cmd_url:
        raise ValueError(
            "The provided url is invalid: {}".format(event_munet_s3cmd_url)
        )

    if event_munet_s3cmd_url.startswith("http"):
        event_munet_s3cmd_url = s3.as_s3cmd_url(event_munet_s3cmd_url)

    prefix = "s3://vision-ml-datasets/training_data/munet/"
    if not event_munet_s3cmd_url.startswith(prefix):
        raise ValueError(
            "Invalid s3 path. It must start with s3://vision-ml-datasets/training_data/munet. Got '{}'.".format(
                event_munet_s3cmd_url
            )
        )
    if event_munet_s3cmd_url.endswith("/"):
        event_munet_s3cmd_url += "event_munet.csv"
    if not event_munet_s3cmd_url.endswith("event_munet.csv"):
        raise ValueError(
            "Invalid s3 path. It must end with event_munet.csv. Got '{}'.".format(
                event_munet_s3cmd_url
            )
        )

    # figure the directories
    src_dirurl = path.dirname(event_munet_s3cmd_url)
    model_tag = path.basename(src_dirurl)
    dst_dirpath = "/data/{}_training/{}".format(model_family, src_dirurl[len(prefix) :])
    data_dirpath = path.join(dst_dirpath, "data")
    if logger:
        logger.info("Src dirurl: {}".format(src_dirurl))
        logger.info("Model tag: {}".format(model_tag))
        logger.info("Dst dirpath: {}".format(dst_dirpath))

    # copy files
    path.make_dirs(data_dirpath)
    src_filepath = s3.cache(event_munet_s3cmd_url, logger=logger)
    dst_filepath = path.join(data_dirpath, "event_munet.csv")
    shutil.copyfile(src_filepath, dst_filepath)
    target_files = [
        "target_taxcode_distribution.csv",
        "prediction_context_list.csv",
        "taxcode_list.csv",
    ]
    if s3.exists(path.join(src_dirurl, target_files[0])):
        src2_dirurl = src_dirurl
    else:
        base_dirurl = path.dirname(src_dirurl)
        if s3.exists(path.join(base_dirurl, target_files[0])):
            src2_dirurl = base_dirurl
        else:
            src2_dirurl = None

    if src2_dirurl is None:
        msg = "No target_taxcode_distribution.csv file detected. Skipping copying target_...csv files."
        logg.warn(msg, logger=logger)
    else:
        for x in target_files:
            url = path.join(src2_dirurl, x)
            if s3.exists(url, local_check=True):
                src_filepath = s3.cache(url, logger=logger)
                dst_filepath = path.join(data_dirpath, x)
                shutil.copyfile(src_filepath, dst_filepath)
            else:
                logg.warn("Remote fle '{}' does not exist.".format(x), logger=logger)

    return src_dirurl, data_dirpath
