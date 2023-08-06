# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

from mt import tp, pd, path, logg

from .taxcode import ensure_field_slice_code


async def load_taxcode_list_asyn(
    filepath: str,
    context_vars: dict = {},
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
):
    """An asyn function that loads an equivalent taxcode_list.csv file from disk.

    Parameters
    ----------
    filepath : str
        local filepath to a dataframe file equivalent to the data team's taxcode_list.csv file
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    l_taxcodes : list, optional
        the loaded taxcode list or None if the file is not found
    """

    if not path.exists(filepath):
        msg = "File 'taxcode_list.csv' not found at: '{}'.".format(filepath)
        logg.warn(msg, logger=logger)
        return None

    msg = "Loading taxcode list at: '{}'".format(filepath)
    logg.info(msg, logger=logger)
    df = await pd.dfload_asyn(
        filepath, show_progress=logger is not None, context_vars=context_vars
    )

    df = ensure_field_slice_code(df, logger=logger)
    l_taxcodes = df["slice_code"].drop_duplicates().tolist()
    l_taxcodes = sorted(l_taxcodes)

    return l_taxcodes
