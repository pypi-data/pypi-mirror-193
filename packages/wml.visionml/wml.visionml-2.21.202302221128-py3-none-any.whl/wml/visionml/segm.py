# pylint: disable=import-outside-toplevel

"""Module dealing with the ground truth segmentation data of each event in the muv1 db.
"""

import sqlalchemy as sa
from copy import copy
from tqdm import tqdm
from io import BytesIO

from mt import np, pd, cv, iio, path, aio, logg
from mt.base import concurrency
from mt.geond import Dlt
from mt.geo import transform
import mt.sql.base as sb

from wml.core import home_dirpath, s3, imageio

from .sqlite import engine, id_key, merge_fields
from .conn import muv1rl_engine


__all__ = [
    "event_path",
    "s3cmd_url",
    "has_cached",
    "get_event_id_list",
    "load",
    "load_asyn",
    "save",
    "save_asyn",
    "update_from_muv1db",
    "sync_locally",
    "render_images",
]


_base_dirpath = path.join(home_dirpath, "segm")
path.make_dirs(_base_dirpath)


def event_path(event_id):
    """Dedicated filepath to the mask contours of a given event."""
    return path.join(_base_dirpath, "event{:09d}.npz".format(event_id))


def s3cmd_url(event_id):
    """Dedicated s3cmd url to the segm image of a given event."""
    return "ml://web/segm/" + "event{:09d}.jpg".format(event_id)


def has_cached(event_id):
    """Returns whether a segmented event has cached its segmentation."""
    return path.exists(event_path(event_id))


def get_event_id_list(logger=None):
    """Returns the list of all segment event ids."""
    id_name = id_key(table="event_segm")
    query_str = "SELECT {id} FROM event_segm;".format(id=id_name)
    return sb.read_sql(query_str, engine, logger=logger)[id_name].tolist()


async def load_asyn(event_id, context_vars: dict = {}):
    """An asyn function that loads the mask contours of a segmented event from a dedicated file location."""
    try:
        data = await aio.read_binary(event_path(event_id), context_vars=context_vars)
        mask_contours = np.load(BytesIO(data))
    except FileNotFoundError as e:
        raise FileNotFoundError(
            e.errno,
            "Event with id {} has no segmentation. Maybe run `segm_sync_from_muv1db.py` to refresh?".format(
                event_id
            ),
        )
    return [mask_contours[x] for x in mask_contours]


def load(event_id):
    """Loads the mask contours of a segmented event from a dedicated file location."""
    return aio.srun(load_asyn, event_id)


async def save_asyn(event_id, mask_contours=[], context_vars: dict = {}):
    """An asyn function that saves the mask contours of a segmented event to a dedicated file location."""
    filepath = event_path(event_id)
    data = BytesIO()
    np.savez_compressed(data, *mask_contours)
    return await aio.write_binary(filepath, data.getvalue(), context_vars=context_vars)


def save(event_id, mask_contours=[]):
    """Saves the mask contours of a segmented event to a dedicated file location."""
    return aio.srun(save_asyn, even_id, mask_contours=mask_contours)


def check_before_after_ids(logger=None):
    """Internal function. TBC"""

    id_name = id_key(table="event_segm")

    # determine the list of ids that need updating
    query_str = "SELECT {id} FROM event_segm WHERE before_image_id IS NULL or after_image_id IS NULL;".format(
        id=id_name
    )
    local_df = sb.read_sql(query_str, engine, logger=None)
    id_list = local_df[id_name].drop_duplicates().tolist()
    if len(id_list) == 0:
        if logger:
            logger.info(
                "All events in wml.event_segm have a before image id or an after image id."
            )
        return

    if logger:
        logger.warn(
            "Detected {} events in wml.event_segm without a before image id or an after image id.".format(
                len(id_list)
            )
        )

    while len(id_list) > 0:
        selected_id_list = id_list[:10000]
        id_list = id_list[10000:]

        if logger:
            logger.info(
                "Querying {} segmented events from ml.v6_segmentation_latest, {} remaining.".format(
                    len(selected_id_list), len(id_list)
                )
            )

        values = ",".join((str(x) for x in selected_id_list))
        query_str = "SELECT event_id, last_updated, before_image_id, after_image_id FROM ml.v6_segmentation_latest WHERE event_id IN ({});".format(
            values
        )
        df = sb.read_sql(query_str, muv1rl_engine, chunksize=100000, logger=logger)

        field_map = {
            "event_id": id_name,
            "last_updated": "last_updated",
            "before_image_id": "before_image_id",
            "after_image_id": "after_image_id",
        }
        merge_fields(
            df,
            table="event_segm",
            field_map=field_map,
            if_exists="replace",
            logger=None,
        )


async def update_from_muv1db(
    event_id_list=None, chunk_size=10000, context_vars: dict = {}, logger=None
):
    """An asyn function that updates the segmentation data from muv1db of a list of events.

    Parameters
    ----------
    event_id_list : list, optional
        list of integers containing the event ids. If not provided, all events from muv1db will be used.
    chunk_size : int, optional
        maximum number of events to update per atomic transaction
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
        Variable 's3_client' must exist and hold an enter-result of an async with statement
        invoking :func:`mt.base.s3.create_s3_client`. In asynchronous mode, variable
        'http_session' must exist and hold an enter-result of an async with statement invoking
        :func:`mt.base.http.create_http_session`. You can use
        :func:`wml.core.s3.create_context_vars` to create a dictionary like this.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    unchanged_list : list
        sublist of the input list which contain local events that are unchanged
    removed_list : list
        sublist of the input list which contain local events that have been removed
    inserted_list : list
        sublist of the input list which contain new local events
    updated_list : list
        sublist of the input list which contain local events that have been updated
    """

    check_before_after_ids(logger=logger)

    id_name = id_key(table="event_segm")

    # make sure the event list contains unique keys
    if event_id_list is not None:
        event_id_list = list(set(event_id_list))

    # make sure this op is atomic in the eyes the local database, but not in the eyes of the remote database to avoid holding up other users
    with engine.begin() as local_conn:
        if event_id_list is None:
            if logger:
                logger.info("Querying the remote status of all events.")
            query_str = "SELECT event_id, last_updated AS remote_last_updated FROM ml.v6_segmentation_latest;"
            remote_id_df = sb.read_sql(
                query_str,
                muv1rl_engine,
                index_col="event_id",
                chunksize=100000,
                logger=logger,
            )

            if logger:
                logger.info("Querying the local status of all events.")
            query_str = "SELECT {id} AS event_id, last_updated AS local_last_updated FROM event_segm;".format(
                id=id_name
            )
            local_id_df = pd.read_sql(query_str, local_conn, index_col="event_id")
        else:
            if logger:
                logger.info(
                    "Querying the remote status of {} events.".format(
                        len(event_id_list)
                    )
                )
            values = ",".join((str(x) for x in event_id_list))
            query_str = "SELECT event_id, last_updated AS remote_last_updated FROM ml.v6_segmentation_latest WHERE event_id IN ({values});".format(
                values=values
            )
            remote_id_df = sb.read_sql(
                query_str,
                muv1rl_engine,
                index_col="event_id",
                chunksize=100000,
                logger=logger,
            )

            if logger:
                logger.info(
                    "Querying the local status of {} events.".format(len(event_id_list))
                )
            query_str = "SELECT {id} AS event_id, last_updated AS local_last_updated FROM event_segm WHERE {id} IN ({values});".format(
                id=id_name, values=values
            )
            local_id_df = sb.read_sql(
                query_str, local_conn, index_col="event_id", logger=logger
            )

        # join both tables into one
        df = remote_id_df.join(local_id_df, how="outer")

        # determine events which exist locally but no longer existent remotely
        s = df["remote_last_updated"].isnull()
        removed_local_event_id_list = df[s].index.drop_duplicates().tolist()
        df = df[~s]
        if removed_local_event_id_list:
            if logger:
                logger.info(
                    "Removing {} local events which no longer exist remotely.".format(
                        len(removed_local_event_id_list)
                    )
                )
            for event_id in removed_local_event_id_list:
                path.remove(event_path(event_id))
            values = ",".join((str(x) for x in removed_local_event_id_list))
            query_str = "DELETE FROM event_segm WHERE {id} IN ({values});".format(
                id=id_name, values=values
            )
            local_conn.execute(sa.text(query_str))

        # determine events which do not exist locally but available remotely
        s = df["local_last_updated"].isnull()
        inserted_local_event_id_list = df[s].index.drop_duplicates().tolist()
        if inserted_local_event_id_list:
            if logger:
                logger.info(
                    "New {} remote events detected.".format(
                        len(inserted_local_event_id_list)
                    )
                )
            df = df[~s]

        # determine local events which are not new remotely
        s = df["local_last_updated"] >= df["remote_last_updated"]
        unchanged_local_event_id_list = df[s].index.drop_duplicates().tolist()
        if unchanged_local_event_id_list:
            if logger:
                logger.info(
                    "{} unchanged events detected.".format(
                        len(unchanged_local_event_id_list)
                    )
                )
            df = df[~s]

        # the remaining ones must be events to be updated
        updated_local_event_id_list = df.index.drop_duplicates().tolist()
        if updated_local_event_id_list:
            if logger:
                logger.info(
                    "Found {} events to be updated.".format(
                        len(updated_local_event_id_list)
                    )
                )

        # now delete old events for updating from the local database
        if updated_local_event_id_list:
            values = ",".join((str(x) for x in updated_local_event_id_list))
            query_str = "DELETE FROM event_segm WHERE {id} IN ({values});".format(
                id=id_name, values=values
            )
            local_conn.execute(sa.text(query_str))

        # get new and updated events from muv1 db
        dfs = []

        def download(local_list, msg):
            if logger:
                logger.info(msg.format(len(local_list)))
            values = ",".join((str(x) for x in local_list))
            query_str = "SELECT event_id, last_updated, before_image_id, after_image_id, mask_contours FROM ml.v6_segmentation_latest WHERE event_id IN ({values});".format(
                values=values
            )
            return sb.read_sql(
                query_str,
                muv1rl_engine,
                chunksize=10000,
                exception_handling="warn",
                logger=logger,
            )  # no index_col

        if inserted_local_event_id_list:
            df = download(
                inserted_local_event_id_list, "Inserting {} new events from muv1 db."
            )
            dfs.append(df)
        if updated_local_event_id_list:
            df = download(
                updated_local_event_id_list, "Updating {} events from muv1 db."
            )
            dfs.append(df)
        df = (
            pd.concat(dfs, sort=False)
            if len(dfs) > 0
            else pd.DataFrame(columns=["event_id"])
        )

        # determine lost events
        new_event_id_list = (
            df["event_id"].drop_duplicates().tolist() if len(df) > 0 else []
        )
        new_inserted_local_event_id_list = list(
            set(inserted_local_event_id_list) & set(new_event_id_list)
        )
        new_updated_local_event_id_list = list(
            set(updated_local_event_id_list) & set(new_event_id_list)
        )
        if len(new_inserted_local_event_id_list) < len(inserted_local_event_id_list):
            if logger:
                logger.info(
                    "Lost {} events while inserting.".format(
                        len(inserted_local_event_id_list)
                        - len(new_inserted_local_event_id_list)
                    )
                )
            inserted_local_event_id_list = new_inserted_local_event_id_list
        if len(new_updated_local_event_id_list) < len(updated_local_event_id_list):
            if logger:
                logger.info(
                    "Lost {} events while updating.".format(
                        len(updated_local_event_id_list)
                        - len(new_updated_local_event_id_list)
                    )
                )
            updated_local_event_id_list = new_updated_local_event_id_list

    # update the local database
    if len(df) > 0:
        # update the local files
        with logg.scoped_info(
            "Caching {} events to disk".format(len(df)), logger=logger
        ), tqdm(total=len(df), unit="event") as progress_bar:
            for _, row in df.iterrows():
                event_id = row["event_id"]
                mask_contours = row["mask_contours"]
                if not isinstance(mask_contours, list):
                    mask_contours = []
                else:
                    mask_contours = [np.array(x) for x in mask_contours]
                await save_asyn(event_id, mask_contours, context_vars=context_vars)
                progress_bar.update()

        # update the event_segm database
        field_map = {
            "event_id": id_name,
            "last_updated": "last_updated",
            "before_image_id": "before_image_id",
            "after_image_id": "after_image_id",
        }
        merge_fields(
            df,
            table="event_segm",
            field_map=field_map,
            if_exists="replace",
            logger=None,
        )

    return (
        unchanged_local_event_id_list,
        removed_local_event_id_list,
        inserted_local_event_id_list,
        updated_local_event_id_list,
    )


def sync_locally(logger=None):
    """Removes segmented events that are available in sqlite but have no segmentation data.

    Parameters
    ----------
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    removed_list : list
        list of event ids that have been removed from table wml.event_segm.
    """

    id_name = id_key(table="event_segm")

    query_str = "SELECT {id} FROM event_segm;".format(id=id_name)
    event_id_list = (
        sb.read_sql(query_str, engine, logger=logger)[id_name]
        .drop_duplicates()
        .tolist()
    )
    event_cnt = len(event_id_list)

    removed_list = []
    with logg.scoped_info(
        "Checking {} events from disk".format(event_cnt), logger=logger
    ), tqdm(total=event_cnt, unit="event") as progress_bar:
        for event_id in event_id_list:
            if not has_cached(event_id):
                removed_list.append(event_id)
            progress_bar.update()

    if not removed_list:
        if logger:
            logger.info("The database is clean.")
        return removed_list

    if logger:
        logger.info(
            "Removing {} events from table wml.event_segm.".format(len(removed_list))
        )
    values = ",".join(str(x) for x in removed_list)
    query_str = "DELETE FROM event_segm WHERE {id} IN ({values});".format(
        id=id_name, values=values
    )
    engine_execute(engine, query_str)
    return removed_list


def render_images(event_id_list, batch_size=16, logger=None):
    """Renders segmented events into images in a given event list.

    Parameters
    ----------
    event_id_list : list or int
        list of integers containing the event ids
    batch_size : int, optional
        the number of items per batch. Each batch may be processed in parallel.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    df : pandas.DataFrame
        a dataframe with columns ['event_id', 'after_image_url', 'segm_image_url'] where the
        'segm_image_url' field contains https urls to the rendered images. The actual images are
        rendered locally only. The user is expected to invoke :func:`upload_to_s3` to upload new
        images to S3.

    Notes
    -----
    If an after image url of an event does not exist in wml.event, the event cannot be rendered.
    If the segmentation is empty, the after_image_url is reused as segm_image_url.
    """

    id_name = id_key(table="event_segm")

    # populate after_image_url from wml.event and wml.image
    values = ",".join((str(x) for x in event_id_list))
    query_str = "SELECT event_segm.{id} AS event_id, image.url AS after_image_url FROM event_segm JOIN image ON image.id=event_segm.after_image_id WHERE event_segm.{id} IN ({values});".format(
        id=id_name, values=values
    )
    df1 = sb.read_sql(query_str, engine, chunksize=100000, logger=logger)
    if logger:
        logger.info(
            "Populated the after image urls of {}/{} events.".format(
                len(df1), len(event_id_list)
            )
        )

    s3_dirpath = "ml://web/segm"
    segm_dir = s3.cache_localpath(s3_dirpath)
    path.make_dirs(segm_dir)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

    def render(work_id):
        if work_id >= len(df1):
            return None

        row = df1.iloc[work_id]

        event_id = int(row["event_id"])
        event_name = "event{:09d}".format(event_id)
        event_filename = event_name + ".jpg"
        event_filepath = path.join(segm_dir, event_filename)
        segm_url = s3.as_https_url(path.join(s3_dirpath, event_filename))

        after_url = row["after_image_url"]
        mask_contours = load(event_id)
        if not mask_contours:
            return (work_id, event_id, after_url, after_url)  # no mask to generate

        after_image = imageio.imread(after_url, logger=logger)
        if after_image is None:
            if logger:
                logger.warn(
                    "In event {}: Loaded an empty after image at '{}'.".format(
                        event_id, after_url
                    )
                )
            return (work_id, False)
        height, width = after_image.shape[:2]

        dst_imgres = [width, height]
        dlt = Dlt(
            offset=np.zeros(2), scale=np.array(dst_imgres)
        )  # dlt1: [0,1]^2 -> image space
        mask_contours = [transform(dlt, np.array(x)) for x in mask_contours]

        mask_image = cv.render_mask(mask_contours, dst_imgres, thickness=3, debug=False)
        mask3_image = cv.dilate(mask_image, kernel)
        mask5_image = cv.dilate(mask3_image, kernel)
        mask3_image *= 0.5
        mask5_image *= 0.25
        mask_image = np.maximum(mask_image, mask3_image)
        mask_image = np.maximum(mask_image, mask5_image)
        mask_image = mask_image[..., np.newaxis]

        after_image = cv.im_ubyte2float(after_image)
        blur_image = cv.blur(1 - after_image, (7, 7))
        new_image = after_image * (1 - mask_image) + blur_image * mask_image
        new_image = cv.im_float2ubyte(new_image)
        iio.imwrite(event_filepath, new_image)

        return (work_id, event_id, after_url, segm_url)

    event_cnt = len(df1)

    if event_cnt == 0:
        return pd.DataFrame(columns=["event_id", "after_image_url", "segm_image_url"])

    with logg.scoped_info(
        "Rendering {} events".format(event_cnt), logger=logger
    ), concurrency.WorkIterator(
        render,
        buffer_size=batch_size * 4,
        skip_null=True,
        serial_mode=event_cnt < batch_size * 10,
        logger=logger,
    ) as renderer, tqdm(
        total=event_cnt, unit="event"
    ) as progress_bar:
        data = []
        for work_id in range(event_cnt):
            res = next(renderer)
            progress_bar.update()
            if res[1] is False:
                continue
            data.append(res[1:])
    return pd.DataFrame(
        columns=["event_id", "after_image_url", "segm_image_url"], data=data
    )


def upload_to_s3(event_id_list, logger=None):
    """Upload a list of segmented events that have been rendered to S3.

    Parameters
    ----------
    event_id_list : list or int
        list of integers containing the event ids corresponding segmented events that have been
        rendered
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    int
        the actual number of images that have been uploaded
    """

    event_cnt = len(event_id_list)
    if event_cnt == 0:
        return 0

    webs3_dirpath_expanded = s3.as_s3cmd_url(
        s3.as_https_url("ml://web/segm"), expanded=True
    )
    bucket_name, s3_dirpath = s3.split(webs3_dirpath_expanded)
    local_dirpath = s3.cache_localpath(webs3_dirpath_expanded)
    if logger:
        logger.debug("S3 dirpath: '{}'".format(webs3_dirpath_expanded))
        logger.debug("Local dirpath: '{}'".format(local_dirpath))

    filepath2key_map = {}
    miss_cnt = 0
    for event_id in event_id_list:
        filename = "event{:09d}.jpg".format(event_id)
        local_filepath = path.join(local_dirpath, filename)
        if not path.exists(local_filepath):
            miss_cnt += 1
            if logger:
                logger.warn("Event {} has not been rendered.".format(event_id))
            continue
        s3key = path.join(s3_dirpath, filename)
        filepath2key_map[local_filepath] = s3key

    if logger:
        if miss_cnt > 0:
            logger.info("Missing {} events in total.".format(miss_cnt))
        logger.info(
            "Uploading {} files to S3. Be patient. It will take a while.".format(
                len(filepath2key_map)
            )
        )
    s3.put_files(bucket_name, filepath2key_map, show_progress=bool(logger))
