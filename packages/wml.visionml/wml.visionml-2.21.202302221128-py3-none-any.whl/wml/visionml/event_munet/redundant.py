# pylint: disable=import-outside-toplevel

"""Loading an event_munet.csv file from S3 and pre-processing key fields therein.
"""

import shutil
import yaml

from mt import tp, np, pd, path

from wml.core import s3, datatype

from ..params import EventMunetLoadingOptions
from ..sqlite import merge_fields
from ..event import (
    get_before_images,
    get_prediction_images,
    get_best_images,
    get_parent,
)
from ..image import get_attributes


def has_columns(df, columns):
    """Checks if the dataframe has all the given columns.

    Parameters
    ----------
    df : pandas.DataFrame
        the input dataframe
    columns : list
        list of columns to check

    Returns
    -------
    bool
        whether or not all the columns exist in the dataframe
    """
    for column in columns:
        if column not in df.columns:
            return False
    return True


def weight_hist(df, key="taxcode", value_list=[], logger=None):
    s = df[key].isin(value_list)
    if s.sum() < len(df):
        if logger:
            unused_list = df[~s][key].drop_duplicates().tolist()
            logger.warn(
                "Detected unused {} values for key '{}':".format(len(unused_list), key)
            )
            logger.warn("  {}".format(unused_list))
        df = df[s]

    arr = np.zeros(len(value_list))
    for _, row in df.iterrows():
        class_id = value_list.index(row[key])
        arr[class_id] += row["weight"]
    return arr
