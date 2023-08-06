# pylint: disable=import-outside-toplevel

"""Reweighting events.
"""

from mt import tp, pd, logg


def ensure_field_ml_weight(
    df: pd.DataFrame,
    missing: str = "warn",
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
) -> pd.DataFrame:
    """Ensures that the field 'ml_weight' exists in the dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        an event munet dataframe
    missing : {'raise', 'warn'}
        behaviour when NaN or negative weights are detected. 'raise' means a ValueError is raised.
        'warn' means some warning messages are printed and the vilotating rows are removed.

    Returns
    -------
    pandas.DataFrame
        the same dataframe as the input dataframe, but with field 'ml_weight' available
    """

    # check for NaN or negative weights
    if "ml_weight" in df.columns:
        s = df["ml_weight"].isnull()
        if s.sum() > 0:
            if missing == "warn":
                logg.warn("Events with NaN weight:", logger=logger)
                logg.warn(df[s], logger=logger)
                df = df[~s]
            else:
                msg = "{} events. each of which with a NaN weight, detected.".format(
                    s.sum()
                )
                raise ValueError(msg)

        s = df["ml_weight"] < 0
        if s.sum() > 0:
            if missing == "warn":
                logg.warn("Events with negative weight:", logger=logger)
                logg.warn(df[s], logger=logger)
                df = df[s]
            else:
                msg = (
                    "{} events. each of which with a negative weight, detected.".format(
                        s.sum()
                    )
                )
                raise ValueError(msg)
    else:  # make one if missing
        df["ml_weight"] = 1.0

    return df


def reweight(
    df: pd.DataFrame,
    mul_s: tp.Optional[pd.Series] = None,
    key_columns: list = ["ml_kind", "prediction_context", "taxcode"],
    msg_format: str = "Reweighting {event_count} events",
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
) -> pd.DataFrame:
    """Multiplies the 'ml_weight' series with a factor series, then normalises the output series.

    Normalising here means that the total weight of all events of a particular index is preserved.
    Every event with a non-positive weight after the reweighting is removed.

    Parameters
    ----------
    df : pandas.DataFrame
        a dataframe related to event-munet. Every event must have a positive weight.
    mul_s : pandas.Series, optional
        a float series of the same index as that of `df`, telling how much the weight of each event
        should be multiplied with. Each factor must be non-negative.
    key_columns : list
        list of field names to define an index. The total weight of events for each index is
        preserved. Note that this index is different from the index that comes with the dataframe.
    msg_format : str, optional
        message format taking keyword argument 'event_count' as input
    logger : logging.Logger or equivalent
        logger for debugging purposes

    Returns
    -------
    out_df : pandas.DataFrame
        the same df with some rows dropped and the 'ml_weight' field is updated
    """

    event_cnt0 = len(df)
    with logg.scoped_info(msg_format.format(event_count=event_cnt0), logger=logger):
        df = df.copy()  # just copy because we will modify the dataframe

        dfa = (
            df.groupby(keys, dropna=False)["ml_weight"].sum().to_frame("old_sum_weight")
        )
        df["ml_weight"] *= mul_s
        dfb = (
            df.groupby(keys, dropna=False)["ml_weight"].sum().to_frame("new_sum_weight")
        )
        dfa = dfa.join(dfb)

        def func(row):
            return (
                0.0
                if row["new_sum_weight"] == 0
                else row["old_sum_weight"] / row["new_sum_weight"]
            )

        dfa["factor"] = dfa.apply(func, axis=1)
        df = df.join(dfa[["factor"]], on=keys)
        df["ml_weight"] *= df["factor"]
        df = df.drop("factor", axis=1)

        df = df[df["ml_weight"] > 0].copy()
        event_cnt1 = len(df)
        if event_cnt1 < event_cnt0:
            if logger:
                logger.info(
                    "Retained {}/{} reweighted events.".format(event_cnt1, event_cnt0)
                )
            event_cnt0 = event_cnt1

    return df


def normalise_weights(
    src_df: pd.DataFrame,
    dst_df: pd.DataFrame,
    l_keys: list = ["ml_kind", "prediction_context", "taxcode"],
    weight_key: str = "ml_weight",
) -> pd.DataFrame:
    """Reweights the weight field so that the sum of weights per index is preserved.

    The function takes as input two dataframes containing all the key fields listed in the 'l_keys'
    argument plus a weight field defined in argument 'weight_key'. The key fields define an index
    for the normalisation operation, which is different from the indices provided to both
    dataframes. The function then rescales the values in the weight field of source dataframe so
    that, for each index, the total weight in the source dataframe equals the total weight in the
    target dataframe, unless the total weight in the source dataframe is non-positive, in which
    case no rescaling is applied, or unless the total weight in the target dataframe is
    non-positive, in which case rescaling is set to 0.

    Parameters
    ----------
    src_df : pandas.DataFrame
        the source dataframe
    dst_df : pandas.DataFrame
        the target dataframe
    l_keys : list
        list of keys/column names defining the joint space where the weights are applied on
    weight_key : str
        key/column name of the field defining the weight for each record. Default is 'ml_weight'.

    Returns
    -------
    out_df : pandas.DataFrame
        a copy of the source dataframe where the weight field has been normalised
    """

    sum_src_df = (
        src_df.groupby(l_keys, dropna=False)[weight_key].sum().to_frame("src_ml_weight")
    )
    sum_dst_df = (
        dst_df.groupby(l_keys, dropna=False)[weight_key].sum().to_frame("dst_ml_weight")
    )
    sum_df = sum_src_df.join(sum_dst_df, how="left")

    def func(row):
        if pd.isnull(row["src_ml_weight"]) or (row["src_ml_weight"] <= 0):
            return 1.0  # degenerate source, do not change
        if pd.isnull(row["dst_ml_weight"]) or (row["dst_ml_weight"] <= 0):
            return 0.0  # degenerate target, set to 0
        return row["dst_ml_weight"] / row["src_ml_weight"]

    sum_df["ml_weight_scale"] = sum_df.apply(func, axis=1)

    out_df = src_df.join(sum_df[["ml_weight_scale"]], on=l_keys)
    out_df[weight_key] *= out_df["ml_weight_scale"]
    out_df = out_df.drop("ml_weight_scale", axis=1)

    return out_df
