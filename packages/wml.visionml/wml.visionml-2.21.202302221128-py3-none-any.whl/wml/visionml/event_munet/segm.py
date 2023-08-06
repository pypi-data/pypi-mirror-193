# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

from mt import tp, pd, logg

from ..params import EventMunetLoadingOptions


def ensure_field_use_segmentation(
    df: pd.DataFrame,
    options: EventMunetLoadingOptions = EventMunetLoadingOptions(),
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Ensures that the field 'use_segmentation' exists in a dataframe.

    The function returns immediately if field 'use_segmentation' exists. If not, it tries to fill
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
        the processed dataframe where field 'use_segmentation' is available
    """

    if "use_segmentation" in df.columns:
        logg.info("Field 'use_segmentation' exists.")
        return df

    if "theoretical_use_segmentation" in df.columns and options.mode_after in (
        "theoretical",
        "system",
    ):
        df = df.rename(columns={"theoretical_use_segmentation": "use_segmentation"})
        logg.info("Renamed field 'theoretical_use_segmentation' as 'use_segmentation'.")
    else:
        logg.info("Created field 'use_segmentation' with value 0.")
        df["use_segmentation"] = 0

    return df
