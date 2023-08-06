# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

import json

from mt import tp, np, pd, logg

import wml.prediction as wp


def extract_slice2menu_code_mappings(
    df: pd.DataFrame,
    l_sliceCodes: tp.Optional[list] = None,
    handle_conflicts: str = "error",
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """Extracts ``(menu_id, slice_code) -> (menu_id, menu_code)`` mappings.

    This function extracts slice2menu mappings from an event munet table.

    Parameters
    ----------
    df : pandas.DataFrame
        a dataframe consisting of at least 3 columns ``['menu_id', 'slice_codes', 'menu_code']``
        where each cell of ``slice_codes`` represents a set of slice codes.
    l_sliceCodes : list, optional
        list of valid slice codes, if known
    handle_conflicts : {"warn", "raise"}
        How to handle a conflict in which a ``('menu_id', 'slice_code')`` pair corresponds to many
        menu codes. "raise" means raising a value error. "warn means logging some warning messages
        and then selecting the first menu code in alphabetical order to resolve each conflict. This
        is a policy agreed with Clem and davidbo on 2023/02/21. In this case, an additional
        dataframe containing the conflict(s) is returned.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    slice2menu_df : pandas.DataFrame
        the dataframe containing the mappings. It has 3 columns
        ``['menu_id', 'slice_code', 'menu_code']`` but each slice code is a unique string.
    conflicts_df : pandas.DataFrame, optional
        the dataframe containing the conflicting mappings. This second returning argument is only
        available if `conflict` is set to 'warn'. If there is a conflict, `conflicts_df` is a
        dataframe with 5 columns ``['event_id', 'menu_id', 'slice_code', 'menu_code', 'count']``.
        If there is no conflict, `conflicts_df` is None.

    Raises
    ------
    ValueError
        if any conflict is detected.
    """

    logg.info(
        "Extracting distinct (menu_id, slice_code, menu_code) tuples...", logger=logger
    )
    data = []
    df1 = df.groupby(["menu_id", "slice_codes", "menu_code"]).head(1)
    for _, row in df1.iterrows():
        event_id = row["event_id"]
        menu_id = row["menu_id"]
        slice_codes = json.loads(row["slice_codes"])
        if l_sliceCodes is not None:
            slice_codes = [x for x in slice_codes if x in l_sliceCodes]
        menu_code = row["menu_code"]
        for slice_code in slice_codes:
            rec = (event_id, menu_id, slice_code, menu_code)
            data.append(rec)
    df = pd.DataFrame(
        columns=["event_id", "menu_id", "slice_code", "menu_code"], data=data
    )
    df = df.sort_values(["menu_id", "slice_code", "menu_code"])

    size_df = df.groupby(["menu_id", "slice_code"]).size().to_frame("count")
    df1 = df.join(size_df, on=["menu_id", "slice_code"], how="left")
    df2 = df1[df1["count"] > 1]
    if len(df2) > 0:
        if handle_conflicts == "error":
            logg.error("Conflicting records detected:", logger=logger)
            logg.error(df2, logger=logger)
            raise ValueError("Conflicting slice code -> menu code mappings detected.")
        elif handle_conflicts == "warn":
            logg.warn("Conflicting records detected:", logger=logger)
            logg.warn(df2, logger=logger)
            conflicts_df = df2
            logg.warn("Selecting the first menu code of each conflict to resolve it.")
            df = df.groupby(["menu_id", "slice_code"]).head(1)
        else:
            raise ValueError(
                "Unknown value for argument 'handle_conflicts': '{}'.".format(
                    handle_conflicts
                )
            )
    elif handle_conflicts == "warn":
        conflicts_df = None
    slice2menu_df = df[["menu_id", "slice_code", "menu_code"]]
    df["menu_id"] = df["menu_id"].astype(int)

    if handle_conflicts == "warn":
        return slice2menu_df, conflicts_df
    return slice2menu_df


def deserialise_label_transformers(
    df: pd.DataFrame,
    l_sliceCodes: list,
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
) -> tp.Dict[int, wp.LabelTransformer]:
    """Deserialises all LabelTransformers from a dataframe.

    Parameters
    ----------
    slice2menu_df : pandas.DataFrame
        the dataframe containing the ``(menu_id, slice_code) -> (menu_id, menu_code)`` mappings. It
        has 3 columns ``['menu_id', 'slice_code', 'menu_code']`` but each slice code is a unique
        string.
    l_sliceCodes : list
        list of global slice codes, likely obtained from a model
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    d_transformers : dict
        a ``{menu_id: wml.prediction.LabelTransformer}`` dictionary
    dl_menuCodes : dict
        a ``{menu_id: list_of_menu_codes}`` dictionary

    See Also
    --------
    wml.prediction.LabelTransformer
        for the definition of a label transformer
    extract_slice2menu_code_mappings
        for how the label transformers are serialised
    """

    # detect slice codes not available in the global taxcode list
    l_dfSliceCodes = df["slice_code"].drop_duplicates().tolist()
    l_outlierSliceCodes = set(l_dfSliceCodes) - set(l_sliceCodes)
    if len(l_outlierSliceCodes):
        msg = "Detected {} slice codes non-existent in the global taxcode list.".format(
            len(l_outlierSliceCodes)
        )
        logg.warn(msg, logger=logger)
        logg.warn(l_outlierSliceCodes, logger=logger)

    # first parse: create lists
    dl_menuCodes = {}
    for _, row in df.iterrows():
        menu_id = int(row["menu_id"])
        menu_code = row["menu_code"]
        if menu_id in dl_menuCodes:
            dl_menuCodes[menu_id].append(menu_code)
        else:
            dl_menuCodes[menu_id] = [menu_code]

    for menu_id in dl_menuCodes:
        dl_menuCodes[menu_id] = sorted(list(set(dl_menuCodes[menu_id])))

    # second parse: make mappings
    dl_menuCodeIds = {
        menu_id: -np.ones(len(l_sliceCodes), dtype=np.int32) for menu_id in dl_menuCodes
    }
    for _, row in df.iterrows():
        slice_code = row["slice_code"]
        try:
            slice_id = l_sliceCodes.index(slice_code)
        except ValueError:
            continue
        menu_id = int(row["menu_id"])
        menu_code = row["menu_code"]
        menu_code_id = dl_menuCodes[menu_id].index(menu_code)
        dl_menuCodeIds[menu_id][slice_id] = menu_code_id

    # make LabelTransformers
    d_transformers = {
        menu_id: wp.LabelTransformer(
            len(dl_menuCodes[menu_id]), dl_menuCodeIds[menu_id]
        )
        for menu_id in dl_menuCodes
    }

    return d_transformers, dl_menuCodes
