# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

from mt import tp, pd, path, logg

from wml.core import s3, datatype

from .taxcode import ensure_field_slice_code
from .taxcode_list import load_taxcode_list_asyn


async def load_fr_problem_asyn(
    filepath,
    context_vars: dict = {},
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
) -> tp.Tuple[tp.Optional[list], tp.Optional[datatype.FRProblem]]:
    """An asyn function that loads the FR problem from disk.

    Parameters
    ----------
    filepath : str
        local filepath to a dataframe file equivalent to the data team's
        target_taxcode_distribution.csv file
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    l_taxcodes : list, optional
        the loaded taxcode list or None if no file is not found
    frp : wml.core.datatype.FRProblem, optional
        the food recognition problem, or None if the file does not exist

    Notes
    -----
    As of 2022/09/13, this function assumes that the user has downloaded all necessary files from
    S3.
    """

    filepath2 = path.join(path.dirname(filepath), "taxcode_list.csv")
    l_taxcodes = await load_taxcode_list_asyn(
        filepath2, context_vars=context_vars, logger=logger
    )

    if not path.exists(filepath):
        msg = "File 'target_taxcode_distribution.csv' not found at: '{}'.".format(
            filepath
        )
        logg.warn(msg, logger=logger)
        return l_taxcodes, None

    with logg.scoped_info("Loading FR problem", logger=logger):
        msg = "Loading opmode-taxcode distribution dataframe '{}'".format(filepath)
        with logg.scoped_info(msg, logger=logger):
            df = await pd.dfload_asyn(
                filepath, show_progress=logger is not None, context_vars=context_vars
            )
            df = ensure_field_slice_code(df, drop_old=True, logger=logger)
            if l_taxcodes is not None:
                msg = "Restricting the target taxcodes to those in the taxcode list."
                logg.info(msg, logger=logger)
                df = df[df["slice_code"].isin(l_taxcodes)]
            else:
                l_taxcodes = df["slice_code"].drop_duplicates().tolist()
                l_taxcodes = sorted(l_taxcodes)
            if "client_region_id" in df:
                df["client_region_id"] = df["client_region_id"].astype(int)

        # make an opmode mapper if 'prediction_context_list.csv' file exists locally
        predctx_list_filepath = path.join(
            path.dirname(filepath), "prediction_context_list.csv"
        )
        if path.exists(predctx_list_filepath):
            # prediction context list
            predctx_list_df = await pd.dfload_asyn(
                predctx_list_filepath, context_vars=context_vars
            )
            l_gpcs = predctx_list_df["prediction_context"].drop_duplicates().tolist()
            opmode_mapper = datatype.Predctx2OpmodeMapper(l_gpcs)
        else:
            opmode_mapper = None

        frp = datatype.FRProblem.from_df(
            df, l_taxcodes=l_taxcodes, opmode_mapper=opmode_mapper, eps=0, logger=logger
        )
        msg = "Detected {} taxcodes and {} non-neutral opmodes.".format(
            frp.n_taxcodes(), frp.n_opmodes()
        )
        logg.info(msg, logger=logger)
    return l_taxcodes, frp


def load_fr_problem(
    filepath: str,
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
) -> tp.Tuple[tp.Optional[list], tp.Optional[datatype.FRProblem]]:
    """Loads the FR problem from an equivalent target_taxcode_distribution.csv file from disk.

    Parameters
    ----------
    filepath : str
        local filepath to a dataframe file equivalent to the data team's
        target_taxcode_distribution.csv file
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    l_taxcodes : list, optional
        the loaded taxcode list or None if no file is not found
    frp : wml.core.datatype.FRProblem, optional
        the food recognition problem, or None if the file does not exist
    """

    return s3.run_main(load_fr_problem_asyn, filepath, logger=logger)
