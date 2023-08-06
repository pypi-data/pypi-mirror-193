# pylint: disable=import-outside-toplevel

"""Our very own SQLite database.

The sole reason for using an sqlite database instead of having multiple dataframe files on disk is
so that multiple processes can access the database concurrently. The latter approach has racing
conditions we do not want to deal with.

Check out SQLAlchemy's support for the SQLite database: https://docs.sqlalchemy.org/en/14/dialects/sqlite.html
"""


import sqlalchemy as sa

from mt import tp, pd, path, logg
import mt.sql.base as sb

from wml.core import home_dirpath

from .base import engine_execute


__all__ = [
    "engine",
    "recreate_all_tables",
    "id_key",
    "add_ids",
    "merge_fields",
    "get_subtable",
]


db_filepath = path.join(home_dirpath, "wml_db.sqlite")
db_conn_str = "sqlite:///{}".format(db_filepath)
engine = sa.create_engine(db_conn_str)
engine_execute(
    engine, "PRAGMA max_page_count = 2147483646;"
)  # increase the max page count

metadata = sa.MetaData()
image = sa.Table(
    "image",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),  # image id from the muv1 db
    sa.Column("url", sa.String),  # url to the image in https format
    sa.Column("width", sa.Integer),  # image width
    sa.Column("height", sa.Integer),  # image height
    sa.Column("nchannels", sa.Integer),  # number of channels
    sa.Column("taken_at", sa.DateTime),  # time at which the image was taken, in UTC+0
    sa.Column(
        "type", sa.String
    ),  # image type, output of imghdr.what(). 'invalid' for an invalid image.
)
event = sa.Table(
    "event",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),  # event id from the muv1 db
    sa.Column(
        "prev_event_id", sa.Integer
    ),  # None: unknown, -1: does not exist, >=0: previous event id in the same device
    sa.Column("before_image_id", sa.Integer),  # current before image id
    sa.Column("after_image_id", sa.Integer),  # current after image id
    sa.Column("weight_g", sa.Integer),  # food weight in gram
    sa.Column("installation_id", sa.Integer),  # installation id
    sa.Column("taxcode", sa.String(length=8)),  # current true taxcode
)
event_segm = sa.Table(
    "event_segm",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),  # event id from the muv1 db
    sa.Column("last_updated", sa.DateTime),  # time at which the event was last updated
    sa.Column("before_image_id", sa.Integer),  # before image id
    sa.Column("after_image_id", sa.Integer),  # after image id
)
installation = sa.Table(
    "ml_installation_details",
    metadata,
    sa.Column(
        "installation_id", sa.Integer, primary_key=True
    ),  # installation id from muv1 db
    sa.Column("lat", sa.Float),  # latitude
    sa.Column("lng", sa.Float),  # longitude
    sa.Column("utc", sa.Float),  # utc offset (in hours)
    sa.Column(
        "updated", sa.String
    ),  # should be datetime but right now text for backward compatibility
)
tables = {
    "image": image,
    "event": event,
    "event_segm": event_segm,
    "installation": installation,
}


def id_key(table="image"):
    """Returns the primary key of a given table.

    Parameters
    ----------
    table : str
        name of the input table

    Returns
    -------
    str
        name of the primary key of the table
    """
    return tables[table].primary_key.columns.keys()[0]


def recreate_all_tables():
    """Recreate all tables in the database."""
    metadata.create_all(engine)


def init():
    if not path.exists(db_filepath):
        from pathlib import Path

        Path(db_filepath).touch(mode=0o664, exist_ok=True)

    recreate_all_tables()

    with engine.begin() as conn:
        # check event
        df = pd.read_sql(sa.text("SELECT * FROM event LIMIT 0;"), conn)
        if not "prev_event_id" in df.columns:
            conn.execute(sa.text("ALTER TABLE event ADD prev_event_id INTEGER;"))


init()


def add_ids(
    id_list, table="image", logger: tp.Optional[logg.IndentedLoggerAdapter] = None
):
    """Adds a list of new indices to a wml table, skipping the existing ones.

    Parameters
    ----------
    id_list : list
        list of new ids to be added, skipping any existing one.
    table : str
        target table name
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes
    """
    id_name = id_key(table)

    # determine existing ones
    query_str = "SELECT {id} FROM {table};".format(id=id_name, table=table)
    cur_id_list = pd.read_sql(query_str, engine)[id_name].tolist()

    new_id_list = list(set(id_list) - set(cur_id_list))
    if len(new_id_list) > 0:
        if logger:
            logger.info(
                "Adding new {}/{} ids to {}.".format(
                    len(new_id_list), len(id_list), table
                )
            )

        s1 = ",NULL" * (len(tables[table].columns.keys()) - 1)
        values = ["({}{})".format(x, s1) for x in new_id_list]
        values = ",\n  ".join(values)
        query_str = "INSERT INTO {} VALUES {};".format(table, values)
        sb.exec_sql(query_str, engine, logger=logger)
    else:
        if logger:
            logger.info("All {} ids are existing.".format(len(id_list)))


def merge_fields(df, table="image", field_map={}, if_exists="skip", logger=None):
    """Merges the some fields of a source dataframe to a target wml table.

    Parameters
    ----------
    df : pandas.DataFrame
        the source, unindexed dataframe
    table : str
        target wml table
    field_map : dict
        a dictionary of (key, value) pairs mapping each source field (key) to a target field (value). The dictionary must include a source field mapping to the target index.
    if_exists : {'replace', 'skip'}
        policy to handle the case where a cell has a non-null value. Value 'replace' means the cell will be replaced with a new value. Value 'skip' means doing nothing.
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes
    """
    # find source id name
    dst_id_key = id_key(table)
    for src_key, dst_key in field_map.items():
        if dst_key == dst_id_key:
            src_id_key = src_key
            break
    else:
        raise ValueError(
            "Unable to determine the source index mapping to target index '{}' in the field map.".format(
                dst_id_key
            )
        )

    total_id_list = df[src_id_key].drop_duplicates().tolist()
    add_ids(total_id_list, table=table, logger=logger)

    for src_key, dst_key in field_map.items():
        if dst_key == dst_id_key:
            continue

        with engine.begin() as conn:  # to make sure all our read/write ops are viewed as an atomic op
            if if_exists == "skip":
                # find images whose corresponding field has not been filled
                values = ", ".join((str(x) for x in total_id_list))
                query_str = "SELECT {id} FROM {table} WHERE {key} IS NULL AND {id} in ({values});".format(
                    id=dst_id_key, table=table, key=dst_key, values=values
                )
                new_id_list = pd.read_sql(query_str, conn)[dst_id_key].tolist()
            elif if_exists == "replace":
                new_id_list = total_id_list
            else:
                raise ValueError(
                    "Unknown value '{}' for keyword argument 'if_exists'.".format(
                        if_exists
                    )
                )

            # prepare a temporary table
            df2 = df[[src_id_key, src_key]]
            df2 = df2[df2[src_id_key].isin(new_id_list)]
            df2.columns = [dst_id_key, dst_key]

            if len(df2) > 0:
                # write it to our db
                if logger:
                    logger.info(
                        "Updating {cnt} {key}s to table wml.{table}.".format(
                            cnt=len(df2), key=dst_key, table=table
                        )
                    )
                df2.to_sql("temp_temp", conn, if_exists="replace")

                # update the table
                # Source: https://stackoverflow.com/questions/19270259/update-with-join-in-sqlite
                query_str = """
                    INSERT INTO {table} ({id}, {key})
                    SELECT a.{id}, b.{key} FROM {table} AS a INNER JOIN temp_temp AS b ON a.{id}=b.{id}
                    ON CONFLICT({id}) DO UPDATE SET {key}=excluded.{key}
                    ;""".format(
                    table=table, id=dst_id_key, key=dst_key
                )
                conn.execute(query_str)

                conn.execute("DROP TABLE IF EXISTS temp_temp;")


def get_subtable(id_list, table="image", sql_keys="*", logger=None):
    """Gets the content of an wml table restricted to a set of ids.

    Parameters
    ----------
    id_list : list
        list of ids that likely exist in the table
    table : str
        target wml table
    sql_keys : str
        part of the SELECT query string that specifies the list of columns to extract. Default is all columns.
    logger : mt.base.logging.IndentedLoggerAdapter
        logger for debugging purposes
    """
    values = "(" + ",".join((str(x) for x in id_list)) + ")"
    query_str = "SELECT {keys} FROM {table} WHERE {id} IN {values};".format(
        keys=sql_keys, table=table, id=id_key(table), values=values
    )
    return sb.read_sql(query_str, engine, chunksize=100000, logger=logger)
