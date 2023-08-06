# pylint: disable=import-outside-toplevel

"""Module dealing with getting installation information from the muv1 database to the sqlite database
"""

import sqlalchemy as sa

from mt import pd
import mt.sql.base as sb

from .sqlite import engine, id_key, add_ids, merge_fields, tables
from .conn import muv1rl_engine
from .event import get_parent, ensure_field_event_id


__all__ = [
    "get_attributes",
    "ensure_field_installation_id",
    "ensure_field_installation_weight",
    "ensure_field_installation_active",
]


def get_attributes(inst_id_list: list, missing: str = "warn", logger=None):
    """Gets the attributes of each installation from a list of installation ids.

    The installation attributes are taken from the 'ml_installation_details' table of the wml
    database.

    Parameters
    ----------
    inst_id_list : list
        list of integers containing the installation ids
    missing : {'raise', 'warn'}
        behaviour when missing ids are detected. 'raise' means a ValueError is raised. 'warn' means
        some warning messages are printed
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='installation_id', columns=['lat', 'lng', 'utc'])`
        the dataframe of all metadata for the given installation ids. Some installation ids may be
        missing if they do not exist in the 'ml_installation_details' table. Duplicate installation
        ids are removed.
    """

    if not isinstance(inst_id_list, list):
        raise ValueError(
            "Expected an 'inst_id_list' to be a list. Got '{}'.".format(
                type(inst_id_list)
            )
        )
    inst_id_list = list(set(inst_id_list))
    tbl = tables["installation"]
    stmt = sa.select(tbl).where(tbl.c["installation_id"].in_(inst_id_list))
    msg = "Querying {} records from table 'ml_installation_details' of wml database.".format(
        len(inst_id_list)
    )
    logg.debug(msg, logger=logger)
    df = pd.read_sql(stmt, engine)

    # make it unique for each installation id
    df = (
        df.sort_values(["installation_id", "updated"])
        .groupby("installation_id")
        .tail(1)
    )
    df = df.drop("updated", axis=1)
    df = df.set_index("installation_id", drop=True)

    if len(df) < len(inst_id_list):
        if missing == "raise":
            raise ValueError(
                "Requested {} installations but returned only {} installations.".format(
                    len(inst_id_list), len(df)
                )
            )
        elif missing == "warn":
            if logger:
                logger.warn(
                    "Requested {} installations but returned only {} installations.".format(
                        len(inst_id_list), len(df)
                    )
                )
                logger.warn("Maybe run 'visionml_update_site_details.py' to update?")
        else:
            raise ValueError(
                "Unknown value for 'missing' argument: '{}'.".format(missing)
            )

    return df


def ensure_field_installation_id(
    df: pd.DataFrame, image_id_field: str = "image_id", logger=None
):
    """Ensures that the event munet dataframe has field 'installation_id'.

    The function checks if there is a field 'installation_id' in the input dataframe. If there is
    not, it invokes :func:`wml.visionml.event.ensure_field_event_id` to ensure that the dataframe
    has field 'event_id' and then it generates the field 'installation_id' with data from the wml
    database. Null installation ids will be set to -1.

    Parameters
    ----------
    df : pandas.DataFrame
        input dataframe
    image_id_field : str
        name of the field containing the image ids, in case we need to generate field 'event_id'
    logger : mt.base.logging.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        output dataframe
    """

    if "installation_id" in df.columns:
        return df

    df = ensure_field_event_id(df, image_id_field=image_id_field, logger=logger)

    if "installation_id" in df.columns:
        return df

    logger.info("Making field 'installation_id' with data from wml database.")
    event_df = get_parent(df["event_id"].drop_duplicates().tolist(), logger=logger)
    df = df.join(event_df, on="event_id", how="left")
    df["installation_id"] = df["installation_id"].fillna(-1).astype(int)
    return df


def ensure_field_installation_weight(
    df: pd.DataFrame, min_n_items: int = 400, logger=None
):
    """Ensures that the event munet dataframe has field 'installation_weight'.

    The function checks if there is a field 'installation_weight' in the input dataframe. If not,
    it invokes :func:`ensure_field_installation_id` to make sure field 'installation_id' exists,
    and then it generates the field 'installation_weight' in the following manner:

    1. For installations with id -1, the weight is 0.0.
    2. For an installation with number of items `N`, if `N >= min_n_items`, the weight is 1.0,
       else `N/min_n_items`.

    Parameters
    ----------
    df : pandas.DataFrame
        input dataframe
    logger : mt.base.logging.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        output dataframe
    """

    if "installation_weight" in df.columns:
        return df

    df = ensure_field_installation_id(df, logger=logger)
    inst_df = (
        df.groupby("installation_id").size().to_frame("n_items").reset_index(drop=False)
    )

    def func(row):
        if row["installation_id"] < 0:
            return 0.0
        n_items = row["n_items"]
        return 1.0 if n_items >= min_n_items else n_items / min_n_items

    inst_df["installation_weight"] = inst_df.apply(func, axis=1)
    inst_df = inst_df[["installation_id", "installation_weight"]].set_index(
        "installation_id"
    )
    df = df.join(inst_df, on="installation_id", how="left")
    return df


def ensure_field_installation_active(
    df: pd.DataFrame,
    age_thresh: pd.Timedelta = pd.Timedelta(180, "days"),
    logger=None,
):
    """Ensures that the event munet dataframe has field 'installation_active'.

    An installation is defined as active if there is at least one event/after image whose
    acquisition time is below 'age_thresh'. The function checks if there is a field
    'installation_active' in the input dataframe. If not, it invokes
    :func:`ensure_field_installation_id` to make sure field 'installation_id' exists,
    and then it generates the field 'installation_active' in the following manner:

    1. It assumes field 'after_image_taken_at' exists. Otherwise an exception is raised.
    2. For installations with id -1 or there is no record detected, the installation is inactive.
    3. For other installations, the latest value of 'after_image_taken_at' is compared against the
       threshold.

    Parameters
    ----------
    df : pandas.DataFrame
        input dataframe
    logger : mt.base.logging.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        output dataframe
    """

    if "installation_active" in df.columns:
        return df

    df = ensure_field_installation_id(df, logger=logger)

    if "after_image_taken_at" not in df.columns:
        raise ValueError(
            "Cannot make field 'installation_active' without field 'after_image_taken_at'."
        )
    df["after_image_taken_at"] = pd.to_datetime(df["after_image_taken_at"])

    inst_df = (
        df.groupby("installation_id")["after_image_taken_at"]
        .max()
        .to_frame("last_taken_at")
        .reset_index(drop=False)
    )
    now = pd.Timestamp.now()

    def func(row):
        if row["installation_id"] < 0:
            return 0
        last_taken_at = row["last_taken_at"]
        return int(last_taken_at + age_thresh > now)

    inst_df["installation_active"] = inst_df.apply(func, axis=1)
    inst_df = inst_df[["installation_id", "installation_active"]].set_index(
        "installation_id"
    )
    df = df.join(inst_df, on="installation_id", how="left")
    df["installation_active"] = df["installation_active"].fillna(0)
    return df
