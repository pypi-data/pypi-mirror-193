# pylint: disable=import-outside-toplevel

"""Modules dealing with image pairs.

An image pair within Winnow's context is a pair of images, identified by their ids
`(before_image_id, after_image_id)` such that the before image is designed to cover as much of old
food as possible, and the after image contains as much information about the new food as possible.
"""


from mt import pd

from wml.core.datatype.image_pair import ImagePair

from .sqlite import engine


__all__ = ["ImagePair", "guess"]


def guess(event_id_list: list):
    """For each event id, guess what the corresponding image pair is, via wml tables.

    Parameters
    ----------
    event_id_list : list
        list of event ids to guess from

    Returns
    -------
    `pandas.Series(index.name='event_id', columns=['before_image_id', 'after_image_id'])`
        a series that maps each found event id to an image pair. The series length may be shorter
        than that of the event id list.
    """

    values = ",".join((str(x) for x in event_id_list))

    df1 = pd.read_sql_query(
        "SELECT id AS event_id, before_image_id AS segm_bid, after_image_id AS segm_aid FROM event_segm WHERE id IN ({});".format(
            values
        ),
        engine,
        index_col="event_id",
    )
    df2 = pd.read_sql_query(
        "SELECT id AS event_id, before_image_id AS bid, after_image_id AS aid FROM event_segm WHERE id IN ({});".format(
            values
        ),
        engine,
        index_col="event_id",
    )
    df1 = df1.join(df2, how="outer")
    df1["before_image_id"] = df1["segm_bid"].fillna(df1["bid"])
    df1["after_image_id"] = df1["segm_aid"].fillna(df1["aid"])
    df1 = df1.drop(["segm_bid", "segm_aid", "bid", "aid"], axis=1)
    df1 = df1[df1["before_image_id"].notnull()]
    df1 = df1[df1["after_image_id"].notnull()]

    return df1
