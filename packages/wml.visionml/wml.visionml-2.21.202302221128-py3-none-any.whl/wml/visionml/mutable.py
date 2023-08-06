"""Module dealing with muv1db tables containing the 'updated' field."""


import sqlalchemy as sa

from mt import pd, logg
import mt.sql.sqlite as ss

from .base import engine_execute
from .conn import muv1rl_engine, winnow_engine
from .sqlite import engine


__all__ = ["get_last_updated_timestamp", "readsync", "vacuum"]


# TODO: currently limited to single-indexed tables only
# list: [schema, table, index_col, chunk_size, updated_col]
mutable_map = {
    "ml_installation_details": [
        "ml",
        "v6_installation_details",
        "installation_id",
        10000,
        None,
    ],
    "winnow_weather": ["winnow_db", "weather_info", "id", 100000, "timeCode"],
    #    'metadata_segmentation': ['metadata', 'segmentation', 'event_id', 1000, 'updated'],
    "ml_event_with_prev": ["ml", "v7_event_with_prev", "event_id", 100000, None],
    "ml_events": [
        "ml",
        "v7_annotation_state_events_compact",
        "event_id",
        100000,
        "updated",
    ],
    "ml_event": ["ml", "v7_event_merged", "event_id", 100000, "updated"],
    "ml_edge_bin_crop": ["ml", "v7_edge_bin_crop", "image_id", 100000, None],
    "ml_event_image": [
        "ml",
        "v7_event_image_minimal",
        "event_image_id",
        200000,
        "updated",
    ],
    "ml_event_special_image": [
        "ml",
        "v7_event_special_image_compact",
        "event_id",
        200000,
        "updated",
    ],
    "ml_image": ["ml", "v7_image_compact", "id", 200000, "updated"],
}


def get_last_updated_timestamp(
    mutable_name: str, updated_col: str = "updated"
) -> pd.Timestamp:
    """Gets the last updated timestamp from all records of an sqlite table reflecting a muv1db table containing the 'updated' field.

    Parameters
    ----------
    mutable_name : str
        one of the muv1db tables containing the 'updated' field. Must be a key of `mutable_map`
        module variable.
    updated_col : str
        name of the 'updated' field if it is other than 'updated.

    Returns
    -------
    last_uts : pandas.Timestamp
        the last updated timestamp in the table, or '2017-01-01 00:00:00' if the table does not exist
    """

    if mutable_name not in mutable_map:
        raise ValueError("Unknown mutable with name '{}'.".format(mutable_name))

    # check if the sqlite table exists
    if not mutable_name in ss.list_tables(engine):
        if mutable_map[mutable_name][0] != "winnow_db":
            first_ts = pd.Timestamp("2017-01-01")
        else:
            first_ts = pd.Timestamp("2014-09-01")
        return first_ts

    query_str = "SELECT MAX({updated_col}) AS last_updated FROM {};".format(
        mutable_name, updated_col=updated_col
    )
    df = pd.read_sql_query(query_str, engine)

    return pd.Timestamp(df["last_updated"][0])


def get_new_updated_timestamps(
    mutable_name: str, last_uts: pd.Timestamp, limit: int = 10000
) -> pd.Timestamp:
    """Obtains all new timestamps and their counts from the 'updated' field of a muv1db table.

    Parameters
    ----------
    mutable_name : str
        one of the muv1db tables containing the 'updated' field. Must be a key of `mutable_map`
        module variable.
    last_uts : pandas.Timestamp
        the last updated timestamp of the corresponding sqlite table
    limit : int
        maximum number of timestamps to be queried

    Returns
    -------
    df : pd.DataFrame
        dataframe containing 'updated', 'count' columns. The 'updated' field is sorted in ascending
        order
    """

    if mutable_name not in mutable_map:
        raise ValueError("Unknown mutable with name '{}'.".format(mutable_name))

    schema, table, index_col, chunk_size, updated_col = mutable_map[mutable_name]
    remote_engine = muv1rl_engine if schema != "winnow_db" else winnow_engine
    frame_str = ss.frame_sql(table, schema=schema)

    query_str = "SELECT {updated_col}, COUNT(*) AS count FROM {} WHERE {updated_col} > '{}' GROUP BY {updated_col} ORDER BY {updated_col} LIMIT {};".format(
        frame_str, str(last_uts), limit, updated_col=updated_col
    )
    df = pd.read_sql_query(query_str, remote_engine)

    return df


def update(
    df: pd.DataFrame, mutable_name: str, index_col: str, is_new_table: bool
) -> int:
    with engine.begin() as conn:  # to make sure all our read/write ops are viewed as an atomic op
        # remove old records that need updating
        if not is_new_table:
            query_str = ",".join((str(x) for x in df[index_col].tolist()))
            query_str = "DELETE FROM {} WHERE {} IN ({});".format(
                mutable_name, index_col, query_str
            )
            conn.execute(sa.text(query_str))

        # append new records
        df = df.set_index(index_col, drop=True)
        df.to_sql(mutable_name, conn, if_exists="append")

        return len(df)


def readsync_via_id(mutable_name: str, logger=None):
    """Read-sync a muv1db table containing the 'updated' field.

    Parameters
    ----------
    mutable_name : str
        one of the muv1db tables containing the 'updated' field. Must be a key of `mutable_map`
        module variable.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes
    """

    schema, table, index_col, chunk_size, _ = mutable_map[mutable_name]
    remote_engine = muv1rl_engine if schema != "winnow_db" else winnow_engine
    frame_str = ss.frame_sql(table, schema=schema)

    if mutable_name in ss.list_tables(engine):
        is_new_table = False
        query_str = "SELECT MAX({index_col}) AS last_id FROM {mutable_name}".format(
            index_col=index_col, mutable_name=mutable_name
        )
        last_id = pd.read_sql_query(query_str, engine)["last_id"][0]
    else:
        is_new_table = True
        last_id = 0

    msg = "Read-syncing mutable '{}' with last id {}".format(mutable_name, last_id)
    with logg.scoped_info(msg, logger=logger):
        first_id = last_id
        query_str = "SELECT MAX({index_col}) AS last_id FROM {frame_str}".format(
            index_col=index_col, frame_str=frame_str
        )
        last_id = pd.read_sql_query(query_str, remote_engine)["last_id"][0]
        if logger:
            logger.debug("Remote has last id {}.".format(last_id))

        query_str = "SELECT COUNT(*) AS cnt FROM {frame_str} WHERE {index_col} > {first_id} AND {index_col} <= {last_id};".format(
            index_col=index_col, frame_str=frame_str, first_id=first_id, last_id=last_id
        )
        count = pd.read_sql_query(query_str, remote_engine)["cnt"][0]
        if count == 0:
            return

        # determine new fold
        fold = (count // chunk_size) + 1
        if logger:
            logger.info(
                "  Found {} records to be downloaded in {} chunks.".format(count, fold)
            )

        for i in range(fold):
            start_ofs = first_id + (last_id - first_id) * i // fold
            end_ofs = first_id + (last_id - first_id) * (i + 1) // fold

            query_str = "SELECT * FROM {frame_str} WHERE {index_col}>{first_id} and {index_col}<={last_id};".format(
                frame_str=frame_str,
                index_col=index_col,
                first_id=start_ofs,
                last_id=end_ofs,
            )
            df = pd.read_sql_query(query_str, remote_engine)

            if len(df) == 0:
                continue

            if logger:
                logger.info(
                    "  {}: Downloaded {} records with id in [{},{}].".format(
                        i + 1, len(df), start_ofs, end_ofs
                    )
                )

            update(df, mutable_name, index_col, is_new_table)


def readsync(mutable_name: str, logger=None):
    """Read-sync a muv1db table containing the 'updated' field.

    Parameters
    ----------
    mutable_name : str
        one of the muv1db tables containing the 'updated' field. Must be a key of `mutable_map`
        module variable.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes
    """

    if mutable_map[mutable_name][4] is None:
        return readsync_via_id(mutable_name, logger=logger)

    schema, table, index_col, chunk_size, updated_col = mutable_map[mutable_name]
    remote_engine = muv1rl_engine if schema != "winnow_db" else winnow_engine
    frame_str = ss.frame_sql(table, schema=schema)

    last_uts = get_last_updated_timestamp(mutable_name, updated_col=updated_col)
    is_new_table = last_uts < pd.Timestamp("2017-01-02")

    msg = "Read-syncing mutable '{}' with timestamp '{}'".format(
        mutable_name, str(last_uts)
    )
    with logg.scoped_info(msg, logger=logger):
        count = 0
        while True:
            thresh_uts = pd.Timestamp.utcnow().tz_localize(None) - pd.Timedelta(
                1, "hours"
            )
            if last_uts > thresh_uts:
                break

            # large enough so that the probing+sorting op is neglible compared to the downloading op
            fold = 16

            if logger:
                logger.info(
                    "Investigating maximum {} timestamps after '{}':".format(
                        chunk_size * fold, str(last_uts)
                    )
                )
            df0 = get_new_updated_timestamps(
                mutable_name, last_uts, limit=chunk_size * fold
            )
            if len(df0) == 0:
                break

            # determine new fold
            count_sum = df0["count"].sum()
            fold = (count_sum // chunk_size) + 1
            if logger:
                logger.info(
                    "  Found {} records to be downloaded in {} chunks.".format(
                        count_sum, fold
                    )
                )

            df0_cnt = len(df0)
            for i in range(fold):
                start_ofs = df0_cnt * i // fold
                end_ofs = (df0_cnt * (i + 1)) // fold

                df = df0.iloc[start_ofs:end_ofs]

                first_uts = last_uts
                last_uts = df[updated_col].max()
                chunk_cnt = df["count"].sum()

                if logger:
                    logger.info(
                        "  {}: Downloading {} records timestamped in ['{}','{}'].".format(
                            i + 1, chunk_cnt, str(first_uts), str(last_uts)
                        )
                    )
                query_str = "SELECT * FROM {frame_str} WHERE {updated_col}>'{first_uts}' and {updated_col}<='{last_uts}';".format(
                    frame_str=frame_str,
                    updated_col=updated_col,
                    first_uts=str(first_uts),
                    last_uts=str(last_uts),
                )
                df = pd.read_sql_query(query_str, remote_engine)

                count += update(df, mutable_name, index_col, is_new_table)

        if logger:
            logger.info(
                "Downloaded {} records and updated timestamp to '{}'.".format(
                    count, str(last_uts)
                )
            )


def merge_from(mutable_name: str, other_engine, logger=None):
    """Merges a mutable from another sqlite database to this database.

    Parameters
    ----------
    mutable_name : str
        mutable to merge. Must be a key of `mutable_map` module variable.
    other_engine : sqlalchemy.engine.Engine
        connection engine to an sqlite3 wml database that contains the mutable to merge from
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    bool
        whether the table has been successfully merged
    """

    if not mutable_name in mutable_map:
        raise ValueError(
            "First argument must be a valid mutable name in the 'mutable_map'. Got: '{}'.".format(
                mutable_name
            )
        )

    msg = "Merging mutable '{}' from '{}'".format(mutable_name, other_engine.url)
    with logg.scoped_info(msg, logger):
        if not mutable_name in ss.list_tables(other_engine):
            if logger:
                logger.info("Remote mutable does not exist.")
            return False

        # merge structure
        remote_sql_str = ss.get_table_sql_code(mutable_name, other_engine)
        if mutable_name in ss.list_tables(engine):  # local table exists
            local_sql_str = ss.get_table_sql_code(mutable_name, engine)
            if local_sql_str != remote_sql_str:
                if logger:
                    logger.debug(
                        "Remote table has a different sql definition from the local one:"
                    )
                    logger.debug("  Local : {}".format(local_sql_str))
                    logger.debug("  Remote: {}".format(remote_sql_str))
                    logger.info("Skipping.")
                return False
        else:  # local table does not exist
            if logger:
                logger.info("Creating local mutable.")
                logger.debug("  SQL: {}".format(remote_sql_str))
            engine_execute(engine, remote_sql_str)

        # merge index
        remote_indices = ss.list_indices(other_engine)
        remote_indices = getattr(remote_indices, mutable_name, {})
        local_indices = ss.list_indices(engine)
        local_indices = getattr(local_indices, mutable_name, {})
        for index_col in remote_indices:
            if index_col in local_indices:
                continue
            index_sql_str = remote_indices[index_col]
            if logger:
                logger.info("Creating index '{}'.".format(index_col))
                logger.debug("  SQL: {}".format(index_sql_str))
            engine_execute(engine, index_sql_str)

        # identify duplicate records
        schema, table, index_col, chunk_size, updated_col = mutable_map[mutable_name]
        with logg.scoped_info("Comparing local <-> remote headers", logger=logger):
            if updated_col is None:
                if logger:
                    logger.info("Loading local ids:")
                query_str = "SELECT {index_col} FROM {mutable_name}".format(
                    index_col=index_col, mutable_name=mutable_name
                )
                local_id_df = pd.read_sql_query(query_str, engine)
                local_id_list = local_id_df[index_col].tolist()
                if logger:
                    logger.debug("  {} ids loaded.".format(len(local_id_df)))
                    logger.info("Loading remote ids:")

                query_str = "SELECT {index_col} FROM {mutable_name}".format(
                    index_col=index_col, mutable_name=mutable_name
                )
                remote_id_df = pd.read_sql_query(query_str, other_engine)
                remote_id_list = remote_id_df[index_col].tolist()
                if logger:
                    logger.debug("  {} ids loaded.".format(len(remote_id_df)))

                local_set = set(local_id_list)
                remote_set = set(remote_id_list)
                drop_list = []
                insert_list = list(remote_set - local_set)

                if logger:
                    logger.info(
                        "{} remote records to be inserted.".format(len(insert_list))
                    )
            else:
                if logger:
                    logger.info("Loading local headers:")
                query_str = "SELECT {index_col}, {updated_col} AS local_updated FROM {mutable_name}".format(
                    index_col=index_col,
                    updated_col=updated_col,
                    mutable_name=mutable_name,
                )
                local_id_df = pd.read_sql_query(query_str, engine, index_col=index_col)
                if logger:
                    logger.debug("  {} headers loaded.".format(len(local_id_df)))
                    logger.info("Loading remote headers:")

                query_str = "SELECT {index_col}, {updated_col} AS remote_updated FROM {mutable_name}".format(
                    index_col=index_col,
                    updated_col=updated_col,
                    mutable_name=mutable_name,
                )
                remote_id_df = pd.read_sql_query(
                    query_str, other_engine, index_col=index_col
                )
                if logger:
                    logger.debug("  {} headers loaded.".format(len(remote_id_df)))

                # records in local but not in remote
                id_df = local_id_df.join(remote_id_df, how="outer").reset_index(
                    drop=False
                )
                drop_list = []
                insert_list = []
                the_list = id_df[id_df["remote_updated"].isnull()][index_col].tolist()
                if logger:
                    logger.debug(
                        "{} local records not in remote.".format(len(the_list))
                    )

                # records in remote but not in local
                id_df = id_df[id_df["remote_updated"].notnull()]
                the_list = id_df[id_df["local_updated"].isnull()][index_col].tolist()
                insert_list.extend(the_list)
                if logger:
                    logger.debug(
                        "{} remote records not in local.".format(len(the_list))
                    )

                # duplicate records
                id_df = id_df[id_df["local_updated"].notnull()]
                common_list = id_df[id_df["local_updated"] == id_df["remote_updated"]][
                    index_col
                ].tolist()
                if logger:
                    logger.info(
                        "{} common records to be kept.".format(len(common_list))
                    )

                # new local records
                id_df = id_df[id_df["local_updated"] != id_df["remote_updated"]]
                the_list = id_df[id_df["local_updated"] > id_df["remote_updated"]][
                    index_col
                ].tolist()
                if logger:
                    logger.debug("{} new local records detected.".format(len(the_list)))

                # new remote records
                id_df = id_df[id_df["local_updated"] < id_df["remote_updated"]]
                the_list = id_df[index_col].tolist()
                drop_list.extend(the_list)
                insert_list.extend(the_list)
                if logger:
                    logger.debug(
                        "{} new remote records detected.".format(len(the_list))
                    )
                    logger.info(
                        "{} local records to be dropped.".format(len(drop_list))
                    )
                    logger.info(
                        "{} remote records to be inserted.".format(len(insert_list))
                    )

        # drop records
        if drop_list:
            if logger:
                logger.info("Dropping {} local records.".format(len(drop_list)))
            query_str = ",".join((str(x) for x in drop_list))
            query_str = (
                "DELETE FROM {mutable_name} WHERE {index_col} IN ({values});".format(
                    mutable_name=mutable_name, index_col=index_col, values=query_str
                )
            )
            engine_execute(engine, query_str)

        # insert remote records
        if insert_list:
            msg = "Upserting {} remote records".format(len(insert_list))
            with logg.scoped_info(msg, logger=logger):
                while insert_list:
                    the_list = insert_list[:1000000]
                    insert_list = insert_list[1000000:]

                    query_str = ",".join((str(x) for x in the_list))
                    query_str = "SELECT * FROM {mutable_name} WHERE {index_col} IN ({values});".format(
                        mutable_name=mutable_name, index_col=index_col, values=query_str
                    )
                    if logger:
                        logger.info(
                            "Loading {} remote records, {} remaining.".format(
                                len(the_list), len(insert_list)
                            )
                        )
                    df = ss.read_sql_query(query_str, other_engine, logger=logger)
                    if logger:
                        logger.info("Inserting {} new records.".format(len(df)))
                    df.to_sql(mutable_name, engine, index=False, if_exists="append")

        if logger:
            logger.info("Merge completed.")

    return True


def vacuum(level: str = "full", logger=None):
    """Cleans up duplicate records in mutables and then make the wml database compact.

    Parameters
    ----------
    level : {'full', 'minimal'}
        If 'minimal', only the mutables are vacuumed. Otherwise, in addition to 'minima', the whole
        wml database is vacuumed.
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes
    """

    wml_tables = ss.list_tables(engine)

    for mutable_name in mutable_map:
        if mutable_name not in wml_tables:
            continue

        msg = "Vacuuming mutable '{}'".format(mutable_name)
        with logg.scoped_info(msg, logger=logger):
            schema, table, index_col, chunk_size, updated_col = mutable_map[
                mutable_name
            ]
            query_str = """WITH t1 AS (SELECT {index_col}, COUNT(*) AS id_cnt FROM {mutable_name} GROUP BY {index_col})
                SELECT {mutable_name}.* FROM {mutable_name}
                    LEFT JOIN t1 ON {mutable_name}.{index_col}=t1.{index_col}
                  WHERE t1.id_cnt > 1
                ;""".format(
                mutable_name=mutable_name,
                index_col=index_col,
            )
            df = ss.read_sql_query(query_str, engine, logger=logger)
            if len(df) == 0:
                if logger:
                    logger.info("The table is clean.")
                continue

            id_list = df[index_col].drop_duplicates().tolist()
            if logger:
                logger.info(
                    "Detected {} duplicate ids spanning over {} records.".format(
                        len(id_list), len(df)
                    )
                )

            query_str = ",".join((str(x) for x in id_list))
            query_str = (
                "DELETE FROM {mutable_name} WHERE {index_col} IN ({values});".format(
                    mutable_name=mutable_name,
                    index_col=index_col,
                    values=query_str,
                )
            )
            engine_execute(engine, query_str)
            if logger:
                logger.info("Deleted {} duplicate records.".format(len(df)))

            if updated_col is None:
                df = df.groupby(index_col).head(1)
            else:
                df = (
                    df.sort_values([index_col, updated_col], ascending=[True, False])
                    .groupby(index_col)
                    .head(1)
                )
            df = df.set_index(index_col, drop=True)
            df.to_sql(mutable_name, engine, if_exists="append")
            if logger:
                logger.info("Reinserted {} clean records.".format(len(df)))

    if level == "full":
        if logger:
            logger.info("Vacuuming the wml database.")
        ss.vacuum(engine)

    if logger:
        logger.info("Done.")
