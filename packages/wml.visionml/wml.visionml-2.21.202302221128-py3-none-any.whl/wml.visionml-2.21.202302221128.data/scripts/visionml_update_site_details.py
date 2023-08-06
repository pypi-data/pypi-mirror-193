#!python

"""Updates the v6_site_details table in muv1 db's ML schema."""

import argparse

from mt import pd, path

import mt.sql.psql as sp
import wml.visionml as wv
from wml.core import logger, temp_dirpath


def main(args):
    if args.csv_file is None:
        # load the table from Winnow db
        # MySQL query to get the localised time of 2000-01-01 00:00 at every single location:
        query_str = """
            SELECT
                t1.id AS location_guid,
                CONVERT_TZ(TIMESTAMP("2000-01-01"), 'UTC', t1.timezone) AS millenium_localised_time,
                t1.timezone,
                t2.lat,
                t2.lng,
                t1.updated
              FROM winnow_db.location t1
              LEFT JOIN winnow_db.mig_view_site_details t2 ON t1.id=t2.siteGuid
        ;"""
        logger.info("Loading site details from Winnow DB.")
        df = sp.read_sql(query_str, wv.winnow_engine, chunksize=10000, logger=logger)
    else:
        df = pd.dfload(args.csv_file, show_progress=True)
        for x in ["millenium_localised_time"]:
            df[x] = pd.to_datetime(df[x])

    for x in ["location_guid"]:
        df[x] = df[x].astype(int)

    # processing
    df["timezone"] = df["timezone"].apply(
        lambda x: None if x is None else x.decode() if isinstance(x, bytes) else x
    )
    df["utc"] = (
        df["millenium_localised_time"] - pd.Timestamp("2000-01-01")
    ).dt.total_seconds() / 3600
    df = df.drop("millenium_localised_time", axis=1)

    # save temporarily
    csv_filepath = path.join(temp_dirpath, "site_details.csv")
    pd.dfsave(df, csv_filepath, show_progress=True)

    # now sync to muv1 db
    logger.info("Saving site details to muv1db.")
    sp.writesync_table(
        wv.muv1rw_engine,
        csv_filepath,
        "v6_site_details",
        "location_guid",
        schema="ml",
        engine_ro=wv.muv1ro_engine,
        drop_cascade=True,
        logger=logger,
    )

    logger.info("Finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to update the site_details table from winnow_db to muv1_db."
    )
    parser.add_argument(
        "-f",
        "--csv_file",
        type=str,
        default=None,
        help="CSV/parquet/pdh5 file containing the exported site_details view. "
        "If not provided then we load from winnow_db.",
    )
    args = parser.parse_args()
    main(args)
