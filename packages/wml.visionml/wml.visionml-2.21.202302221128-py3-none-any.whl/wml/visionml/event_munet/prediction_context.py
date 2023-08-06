# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

from mt import tp, pd, logg


def ensure_field_prediction_context(
    df: pd.DataFrame,
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Ensures that the field 'prediction_context' exists in a dataframe.

    The function returns immediately if field 'prediction_context' exists. If not, it tries to fill
    in the field using existing information from the database.

    Parameters
    ----------
    df : pandas.DataFrame
        the dataframe to process, which may be modified by the function
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        the processed dataframe where field 'prediction_context' is available
    """

    if "prediction_context" in df.columns:
        logg.info("Field 'prediction_context' exists.")
        return df

    if "client_region_id" in df.columns:
        logg.info("Field 'client_region_id' exists.")
        return df

    df["prediction_context"] = "{}"
    logg.info("Created field 'prediction_context' with value '{}'.", logger=logger)
    return df
