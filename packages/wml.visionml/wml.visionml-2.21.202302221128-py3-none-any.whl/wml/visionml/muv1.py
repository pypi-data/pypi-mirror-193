import json

from mt import np, pd, path, logg
import mt.sql.psql as sp
import mt.sql.base as sb

from wml.core import home_dirpath

from .conn import muv1rl_engine, muv1rw_engine
from .sqlite import engine


__all__ = [
    "read_muv1db_frame",
    "read_v6_segmentation_valid",
    "read_v6_segmentation_valid_image_attrs",
    "read_v6_segmentation_convex",
]


def read_muv1db_frame(
    frame_name,
    id_name,
    hash_name="hash",
    schema=None,
    cache_only=False,
    file_read_delayed: bool = False,
    logger=None,
):
    """Reads a muv1db frame that contains an indexing column, but sync the frame locally to a pdh5 file. Use this function for small or medium-sized frames only.

    Parameters
    ----------
    frame_name : str
        name of the table/view/matview to read
    id_name: str
        index column name. Assumption is only one column for indexing for now.
    hash_name : str
        name of the hash field. See :func:`mt.sql.psql.comparesync_table` for more details.
    schema : str, optional
        the schema at which the frame is located. If None is given, we assume 'public'
    cache_only : bool
        whether or not to load the frame from cache only.
    file_read_delayed : bool
        whether or not to delay reading columns with complex data types like 'json', 'ndarray',
        'Image' and 'SparseNdarray'. Only valid when `cache_only` is True and the file type is
        '.pdh5'.
    logger : logging.Logger or equivalent
        logger for debugging purposes

    Returns
    -------
    pandas.DataFrame
        the frame that has been read from the muv1db

    Raises
    ------
    RuntimeError
        if 'cache_only' is on but there is no cache image
    """
    if not schema:
        schema = "public"

    dirpath = path.join(home_dirpath, "muv1db", schema)
    path.make_dirs(dirpath)

    filepath = path.join(dirpath, frame_name + ".pdh5")

    if cache_only:
        if not path.exists(filepath):
            raise RuntimeError(
                "Flag 'cache_only' is ON but file '{}' does not exist.".format(filepath)
            )
        logg.info("Loading from cache '{}'...".format(filepath), logger=logger)
        return pd.dfload(
            filepath, show_progress=bool(logger), file_read_delayed=file_read_delayed
        )

    return sp.readsync_table(
        muv1rl_engine,
        filepath,
        frame_name,
        id_name,
        hash_name=hash_name,
        schema=schema,
        logger=logger,
        raise_exception_upon_mismatch=False,
    )


def read_v6_segmentation_valid(
    cache_only=False, file_read_delayed: bool = False, logger=None
):
    """Reads the ml.v6_segmentation_valid view, but sync the frame locally to a pdh5 file.

    Parameters
    ----------
    cache_only : bool
        whether or not to load the frame from cache only.
    file_read_delayed : bool
        whether or not to delay reading columns with complex data types like 'json', 'ndarray',
        'Image' and 'SparseNdarray'. Only valid when `cache_only` is True and the file type is
        '.pdh5'.
    logger : logging.Logger or equivalent
        logger for debugging

    Returns
    -------
    pandas.DataFrame
        the frame that has been read from the muv1db

    Raises
    ------
    RuntimeError
        if 'cache_only' is on but there is no cache image

    Notes
    -----
    This functions wraps :func:`read_muv1db_frame`.
    """
    return read_muv1db_frame(
        "v6_segmentation_valid",
        "event_id",
        hash_name="last_updated",
        schema="ml",
        cache_only=cache_only,
        file_read_delayed=file_read_delayed,
        logger=logger,
    )


def read_v6_segmentation_valid_image_attrs(cache_only=False, logger=None):
    """Reads the ml.v6_segmentation_valid_image_attrs view, but sync the frame locally to a pdh5 file.

    Parameters
    ----------
    cache_only : bool
        whether or not to load the frame from cache only.
    logger : logging.Logger or equivalent
        logger for debugging

    Returns
    -------
    pandas.DataFrame
        the frame that has been read from the muv1db

    Raises
    ------
    RuntimeError
        if 'cache_only' is on but there is no cache image

    Notes
    -----
    This functions wraps :func:`read_muv1db_frame`.
    """
    return read_muv1db_frame(
        "v6_segmentation_valid_image_attrs",
        "event_id",
        hash_name="last_updated",
        schema="ml",
        cache_only=cache_only,
        logger=logger,
    )


def read_v6_segmentation_convex(cache_only=False, logger=None):
    """Reads the ml.v6_segmentation_convex view, but sync the frame locally to a pdh5 file.

    Parameters
    ----------
    cache_only : bool
        whether or not to load the frame from cache only.
    logger : logging.Logger or equivalent
        logger for debugging

    Returns
    -------
    pandas.DataFrame
        the frame that has been read from the muv1db

    Raises
    ------
    RuntimeError
        if 'cache_only' is on but there is no cache image

    Notes
    -----
    This functions wraps :func:`read_muv1db_frame`.
    """
    return read_muv1db_frame(
        "v6_segmentation_convex",
        "event_id",
        hash_name="last_updated",
        schema="ml",
        cache_only=cache_only,
        logger=logger,
    )


def convert_mask_contours_to_mask_convex_xy(mask_contours):
    """Converts a 'mask_contours' object into a 'mask_convex_xy' object.

    Parameters
    ----------
    mask_contours : None or iterable
        a 'mask_contours' cell value from pdh5, csv or muv1db. If not None, it can be a nested numpy array or a nested list, representing a collection of polygon points in [x,y] coordinates. The coordinates can be relative or absolute.

    Returns
    -------
    mask_convex_xy : None or str
        a json-compatible string representing a list of 2d vertices of the convex hull polygon of the 'mask_contours'
    """
    import shapely.geometry as _sg

    if mask_contours is None:
        return None
    if len(mask_contours) == 0:
        return "[]"
    multipoint = sg.MultiPoint(
        np.concatenate([y for x in mask_contours for y in x]).reshape(-1, 2)
    )
    coords = (
        np.array(multipoint.convex_hull.exterior.coords.xy).reshape(2, -1).T.tolist()
    )
    return json.dumps(coords)
