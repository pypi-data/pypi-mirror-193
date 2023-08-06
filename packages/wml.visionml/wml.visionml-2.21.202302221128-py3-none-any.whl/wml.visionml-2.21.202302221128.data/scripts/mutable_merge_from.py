#!python

import argparse as _ap

import sqlalchemy as sa

from mt import np
from wml.core import logger, s3
from wml.visionml import mutable


async def main(args, context_vars: dict = {}):
    tables = list(mutable.mutable_map.keys())
    if args.list:
        logger.info("Valid table names:")
        logger.info(tables)
        return
    if args.table is not None:
        tables = [args.table]

    logger.warn("The script can take hours to run. Be patient!")

    db_conn_str = "sqlite:///{}".format(args.db_file)
    engine = sa.create_engine(db_conn_str)

    for table in tables:
        try:
            mutable.merge_from(table, engine, logger=logger)
        except:
            logger.warn_last_exception()
            logger.warn("Skipping table '{}'.".format(table))

    level = "full" if args.vacuum_database else "minimal"
    mutable.vacuum(level=level, logger=logger)

    logger.info("Finished.")


if __name__ == "__main__":
    parser = _ap.ArgumentParser(
        description="Utility script to merge mutables from a given sqlite3 database to the wml database of the user."
    )
    parser.add_argument(
        "-l", "--list", action="store_true", help="Just list all mutable names."
    )
    parser.add_argument(
        "-t",
        "--table",
        type=str,
        help="The name of the mutable to be merged. If not specified, all tables will be merged.",
    )
    parser.add_argument(
        "-v",
        "--vacuum_database",
        action="store_true",
        help="Whether or not to vacuum the database after merging everything.",
    )
    parser.add_argument(
        "db_file", type=str, help="Filepath to the sqlite3 database to merge from."
    )
    args = parser.parse_args()

    s3.run_main(main, args)
