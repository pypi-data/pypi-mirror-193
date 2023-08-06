# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

import json

from mt import tp, pd, logg


def ensure_field_slice_codes(
    df: pd.DataFrame,
    drop_old: bool = False,
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Ensures that there is a field called 'slice_codes' in the dataframe.

    The function checks for the existence of field 'slice_codes'. If it does not exist, the
    function first searches for field 'taxcode' and transforms field 'taxcode' to field
    'slice_codes'. If field 'taxcode' does not exist, it searches for field 'slice_code' and
    transforms field 'slice_code' to field 'slice_codes'.

    Parameters
    ----------
    df : pandas.DataFrame
        a dataframe equivalent to the event munet dataframe. It should field 'taxcode' or
        'slice_code' or 'slice_codes'.
    drop_old : bool
        in the case that another field is used to generate 'slice_codes', whether to remove
        the old field or not
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        the same dataframe as the input dataframe, but with field 'slice_codes' available

    Raises
    ------
    ValueError
        if any conflict is detected.
    """

    if "slice_codes" in df.columns:
        return df

    def func(x):
        return None if x is None else json.dumps([x])

    if "taxcode" in df.columns:
        logg.info(
            "Tranforming field 'taxcode' to field 'slice_codes'...", logger=logger
        )

        df["slice_codes"] = df["taxcode"].apply(func)
        if drop_old:
            logg.info("Dropping field 'taxcode'.", logger=logger)
            df = df.drop("taxcode", axis=1)
        return df

    if "slice_code" in df.columns:
        if len(df) == 0:
            raise ValueError("The dataframe is empty.")
        logg.info(
            "Tranforming field 'slice_code' to field 'slice_codes'...", logger=logger
        )

        x = df.iloc[0]["slice_code"]
        if x[0] == "[":
            df["slice_codes"] = df["slice_code"]
        else:
            df["slice_codes"] = df["slice_code"].apply(func)
        if drop_old:
            logg.info("Dropping field 'slice_code'.", logger=logger)
            df = df.drop("slice_code", axis=1)
        return df

    raise ValueError(
        "None of fields 'taxcode', 'slice_code', 'slice_codes' detected from the dataframe "
        "with columns {}.".format(list(df.columns))
    )


def ensure_field_slice_code(
    df: pd.DataFrame,
    drop_old: bool = False,
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Ensures that there is a field called 'slice_code' in the dataframe.

    The function checks for the existence of field 'slice_code'. If it does not exist, the
    function searches for field 'taxcode' and copies field 'taxcode' to field
    'slice_code'.

    Parameters
    ----------
    df : pandas.DataFrame
        a dataframe equivalent to the event munet dataframe. It should field 'taxcode' or
        'slice_code'.
    drop_old : bool
        in the case that another field is used to generate 'slice_code', whether to remove
        the old field or not
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        the same dataframe as the input dataframe, but with field 'slice_code' available

    Raises
    ------
    ValueError
        if any conflict is detected.
    """

    if "slice_code" in df.columns:
        if len(df) == 0:
            raise ValueError("The dataframe is empty.")
        if df.iloc[0]["slice_code"][0] == "[":
            df["slice_code"] = df["slice_code"].apply(lambda x: json.loads(x)[0])
        return df

    if "taxcode" in df.columns:
        logg.info("Copying field 'taxcode' to field 'slice_code'...", logger=logger)

        df["slice_code"] = df["taxcode"]
        if drop_old:
            logg.info("Dropping field 'taxcode'.", logger=logger)
            df = df.drop("taxcode", axis=1)
        return df

    raise ValueError(
        "Neither field 'taxcode' nor 'slice_code' detected from the dataframe with columns "
        "{}.".format(list(df.columns))
    )


def ensure_field_menu_code(
    df: pd.DataFrame,
    drop_old: bool = False,
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Ensures that there is a field called 'menu_code' in the dataframe.

    The function checks for the existence of field 'menu_code'. If it does not exist, the
    function first searches for field 'taxcode' and copies field 'taxcode' to field
    'menu_code'.

    Parameters
    ----------
    df : pandas.DataFrame
        a dataframe equivalent to the event munet dataframe. It should field 'taxcode' or
        'menu_code'.
    drop_old : bool
        in the case that another field is used to generate 'menu_code', whether to remove
        the old field or not
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        the same dataframe as the input dataframe, but with field 'menu_code' available

    Raises
    ------
    ValueError
        if any conflict is detected.
    """

    if "menu_code" in df.columns:
        return df

    if "taxcode" in df.columns:
        logg.info("Copying field 'taxcode' to field 'menu_code'...", logger=logger)

        df["menu_code"] = df["taxcode"]
        if drop_old:
            logg.info("Dropping field 'taxcode'.", logger=logger)
            df = df.drop("taxcode", axis=1)
        return df

    raise ValueError(
        "Neither field 'taxcode' nor 'menu_code' detected from the dataframe with columns "
        "{}".format(list(df.columns))
    )
