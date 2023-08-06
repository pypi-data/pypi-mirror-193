# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

from mt import tp, pd, logg

from ..params import EventMunetLoadingOptions
from ..event import get_before_images


def ensure_field_before_image_id(
    df: pd.DataFrame,
    options: EventMunetLoadingOptions = EventMunetLoadingOptions(),
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Ensures that the field 'before_image_id' exists in a dataframe.

    The function returns immediately if field 'before_image_id' exists. If not, it tries to fill
    in the field using existing information from the database.

    Parameters
    ----------
    df : pandas.DataFrame
        the dataframe to process, which may be modified by the function
    options : EventMunetLoadingOptions
        options to load the file
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        the processed dataframe where field 'before_image_id' is available
    """

    if "before_image_id" in df.columns:
        logg.info("Field 'before_image_id' exists.")
        if "before_image_valid" not in df.columns:
            logg.info("Setting field 'before_image_valid' to 0.")
            df["before_image_valid"] = 0
        return df

    # load system_before_image_id if needed
    if (not "system_before_image_id" in df.columns) and options.mode_before in (
        "system",
        "system_only",
    ):
        event_id_list = df["event_id"].drop_duplicates().tolist()
        before_image_df = get_before_images(
            event_id_list, missing="warn", logger=logger
        )
        before_image_df = before_image_df.groupby("event_id").head(1)
        before_image_df = before_image_df.set_index("event_id", drop=True)
        before_image_df.columns = ["system_before_image_id"]
        df = df.join(before_image_df, on="event_id", how="left")

    # select before images
    if options.mode_before == "pass":
        if logger:
            logger.debug("Standard before images.")
    elif options.mode_before == "theoretical":
        if logger:
            logger.debug("Theoretical before images.")
        if not "theoretical_before_image_id" in df.columns:
            df["theoretical_before_images_id"] = None
        df["before_image_id"] = df["theoretical_before_image_id"]
        df["before_image_valid"] = (
            df["theoretical_before_image_valid"]
            if "theoretical_before_image_valid" in df.columns
            else 1
        )
    elif options.mode_before == "system":
        if logger:
            logger.debug("System before images.")
        if not "theoretical_before_image_id" in df.columns:
            df["theoretical_before_image_id"] = None
        df["before_image_id"] = df["system_before_image_id"].where(
            df["system_before_image_id"].notnull(), df["theoretical_before_image_id"]
        )
        df["before_image_valid"] = (
            df["theoretical_before_image_valid"]
            if "theoretical_before_image_valid" in df.columns
            else 1
        )  # 1 is very wrong here. but no choice
        df["before_image_valid"] = df["before_image_valid"].where(
            df["system_before_image_id"].isnull(), 1
        )
    elif options.mode_before == "system_only":
        if logger:
            logger.debug("System before images only, maybe for error analysis.")
        df["before_image_id"] = df["system_before_image_id"]
        df["before_image_valid"] = (
            df["system_before_image_id"].notnull().astype(int)
        )  # 1 is very wrong here. but no choice
    else:
        raise ValueError(
            "Unknown value for 'mode_before': '{}'.".format(options.mode_before)
        )
    s = df["before_image_id"].isnull()
    if s.sum() > 0:
        df = df[~s]
        if logger:
            logger.warn(
                "Rejected {} events due to lack of before image id.".format(s.sum())
            )

    return df


def remove_events_with_an_invalid_before_image(df, logger=None):
    """Removes events with an invalid before image from the dataframe.

    And removes the 'before_image_valid' field from the dataframe.

    Parameters
    ----------
    event_munet_df : pandas.DataFrame
        the loaded and preprocessed event_munet dataframe
        via :func:`load`
    Returns
    -------
    filtered_event_munet_df : pandas.DataFrame
        either the same input dataframe or one where the events with an invalid before image have
        been removed and the 'before_image_valid' field has been removed
    """

    if not "before_image_valid" in df:
        logg.info("No event with an invalid before image is detected.", logger=logger)
        return df

    event_cnt = len(df)
    df = df[df["before_image_valid"] == 1]
    df = df.drop("before_image_valid", axis=1)
    df = df.reset_index(drop=True)
    if logger:
        event_cnt2 = len(df)
        if event_cnt2 < event_cnt:
            msg = "Removed {}/{} events with an in valid before image from the event_munet dataframe.".format(
                event_cnt - event_cnt2, event_cnt
            )
            logger.warn(msg)
        else:
            logger.info("No event with an invalid before image is detected.")
    return df
