# pylint: disable=import-outside-toplevel

"""Dealing with ml_kind field.
"""

from mt import tp, pd, logg


def parse_ml_kinds(df: pd.DataFrame, ml_kind: str = "auto") -> str:
    """Parses the '--ml_kind' argument to produce a list of ml kinds.

    Parameters
    ----------
    df : pandas.DataFrame
        a dataframe related to event-munet containing the 'ml_kind' field.
    ml_kind : {'training', 'validation', 'prediction', 'all', 'auto'}
        event ml_kind to restrict to. Apart from the specific kinds, additional values are 'all'
        and 'auto'. Value 'all' means no restriction. Value 'auto' (default) means only remove
        'training' events.

    Returns
    -------
    ml_kind_list : list
        list of `ml_kind` values detected from the dataframe that matches with the argument
    """

    if ml_kind == "auto":
        ml_kind_list = df["ml_kind"].drop_duplicates().tolist()
        ml_kind_list = [x for x in ml_kind_list if x != "training"]
    elif ml_kind == "all":
        ml_kind_list = df["ml_kind"].drop_duplicates().tolist()
        if "validation" in ml_kind_list:
            ml_kind_list.remove("validation")
            ml_kind_list = ["validation"] + ml_kind_list
    else:
        ml_kind_list = [ml_kind]

    return ml_kind_list


def split_trainval(
    df: pd.DataFrame, mix_list: list = [1, 0, 0], split_ratio: float = 0.75
) -> pd.Series:
    """Splits the events of a dataframe into training and validation events.

    Parameters
    ----------
    df : pandas.DataFrame
        a dataframe containing columns '["event_id", "before_image_id", "after_image_id"]'.
    mix_list : iterable
        a collection of 3 non-negative integers, representing the multiplying coefficient for
        'event_id', 'before_image_id' and 'after_image_id' respectively. The default is only using
        'event_id' for making the split.
    split_ratio : float
        the trainval splitting ratio. The default is 75% for training and 25% for validation.

    Returns
    -------
    s : pandas.Series
        a series that can act as the 'ml_kind' column of the dataframe
    """

    def split_func(row):
        x = (
            (row["event_id"] % 1000) * mix_list[0]
            + (row["before_image_id"] % 1000) * mix_list[1]
            + (row["after_image_id"] % 1000) * mix_list[2]
        ) % 1000
        return "training" if x < split_ratio * 1000 else "validation"

    return df.apply(split_func, axis=1)


def ensure_field_ml_kind(
    df: pd.DataFrame,
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Ensures that the field 'ml_kind' exists in a dataframe.

    The function returns immediately if field 'ml_kind' exists. If not, it tries to fill
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
        the processed dataframe where field 'ml_kind' is available
    """

    if "ml_kind" in df.columns:
        logg.info("Field 'ml_kind' exists.")
    else:
        df["ml_kind"] = "prediction"
        logg.info("Created field 'ml_kind' with value 'prediction'.", logger=logger)
    return df
