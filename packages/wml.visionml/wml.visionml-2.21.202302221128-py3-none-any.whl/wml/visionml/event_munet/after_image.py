# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

from mt import tp, pd, logg

from ..params import EventMunetLoadingOptions
from ..event import get_best_images, get_prediction_images


def ensure_field_after_image_id(
    df: pd.DataFrame,
    options: EventMunetLoadingOptions = EventMunetLoadingOptions(),
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Ensures that the field 'after_image_id' exists in a dataframe.

    The function returns immediately if field 'after_image_id' exists. If not, it tries to fill
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
        the processed dataframe where field 'after_image_id' is available
    """

    if "after_image_id" in df.columns:
        logg.info("Field 'after_image_id' exists.")
        return df

    event_id_list = df["event_id"].drop_duplicates().tolist()

    # load theoretical_after_image_id if needed
    if (not "theoretical_after_image_id" in df.columns) and options.mode_after in (
        "theoretical",
        "system",
    ):
        best_image_df = get_best_images(event_id_list, missing="warn", logger=logger)
        best_image_df = best_image_df.groupby("event_id").head(1)
        best_image_df = best_image_df.set_index("event_id", drop=True)
        best_image_df.columns = [
            "theoretical_after_image_id",
            "theoretical_after_image_type",
        ]
        df = df.join(best_image_df, on="event_id", how="left")

    # load system_after_image_id if needed
    # override 'system_after_image_id' even if it exists
    if options.mode_after in ("system", "system_only"):
        if "system_after_image_id" in df.columns:
            s = df[df["system_after_image_id"].isnull()]["event_id"]
            event_id_list2 = s.drop_duplicates().tolist()
            old_pred_image_df = df[df["system_after_image_id"].notnull()]
            old_pred_image_df = df[["event_id", "system_after_image_id"]]
            old_pred_image_df = old_pred_image_df.set_index("event_id", drop=True)
            old_pred_image_df["system_after_image_type"] = "PREDICTION_IMAGE"
            df = df.drop("system_after_image_id", axis=1)
            if logger:
                logger.debug(
                    "Temporarily dropped field 'system_after_image_id' to regenerate it."
                )
                logger.debug(
                    "Retained {} prediction images.".format(len(old_pred_image_df))
                )
        else:
            event_id_list2 = event_id_list
            old_pred_image_df = None

        if len(event_id_list2) > 0:
            pred_image_df = get_prediction_images(
                event_id_list2, missing="warn", logger=logger
            )
            pred_image_df = pred_image_df.groupby("event_id").head(1)
            pred_image_df = pred_image_df.set_index("event_id", drop=True)
            pred_image_df.columns = ["system_after_image_id", "system_after_image_type"]
            if old_pred_image_df is not None:
                pred_image_df = pd.concat(
                    [old_pred_image_df, pred_image_df], sort=False
                )
        else:
            pred_image_df = old_pred_image_df
        df = df.join(pred_image_df, on="event_id", how="left")

    # select after images
    if options.mode_after == "pass":
        logg.debug("Standard after images.", logger=logger)
    elif options.mode_after == "theoretical":
        logg.debug("Theoretical after images.", logger=logger)
        df["after_image_id"] = df["theoretical_after_image_id"]
    elif options.mode_after == "system_only":
        if logger:
            logger.debug("System after images only, maybe for error analysis.")
        df["after_image_id"] = df["system_after_image_id"]
    elif options.mode_after == "system":
        logg.debug("System after images.", logger=logger)
        if "theoretical_after_image_id" in df.columns:
            df["after_image_id"] = df["system_after_image_id"].where(
                df["system_after_image_id"].notnull(), df["theoretical_after_image_id"]
            )
        else:
            logg.warn(
                "Field 'theoeretical_after_image_id' does not exist.", logger=logger
            )
            df["after_image_id"] = df["system_after_image_id"]
    else:
        raise ValueError(
            "Unknown value for 'mode_after': '{}'.".format(options.mode_after)
        )
    s = df["after_image_id"].isnull()
    if s.sum() > 0:
        df = df[~s]
        msg = "Rejected {} events due to lack of after image id.".format(s.sum())
        logg.warn(msg, logger=logger)

    return df
