#!python

import argparse as _ap

from mt import np
from wml.core import logger, s3
from wml.visionml import mutable


async def main(args, context_vars: dict = {}):
    tables = list(mutable.mutable_map.keys())
    if args.list:
        logger.info("Valid table names:")
        logger.info(tables)
    else:
        if args.table is not None:
            tables = [args.table]
        for table in tables:
            try:
                mutable.readsync(table, logger=logger)
            except:
                logger.warn_last_exception()
                logger.warn("Skipped syncing table '{}'.".format(table))

    level = "full" if args.vacuum_database else "minimal"
    mutable.vacuum(level=level, logger=logger)

    logger.info("Finished.")


if __name__ == "__main__":
    parser = _ap.ArgumentParser(
        description="Utility script to read-sync mutables from muv1db."
    )
    parser.add_argument(
        "-l", "--list", action="store_true", help="Just list all mutable names."
    )
    parser.add_argument(
        "-t",
        "--table",
        type=str,
        help="The name of the mutable to be updated. If not specified, all tables will be sync'ed.",
    )
    parser.add_argument(
        "-v",
        "--vacuum_database",
        action="store_true",
        help="Whether or not to vacuum the database after read-syncing everything.",
    )
    args = parser.parse_args()

    s3.run_main(main, args)
