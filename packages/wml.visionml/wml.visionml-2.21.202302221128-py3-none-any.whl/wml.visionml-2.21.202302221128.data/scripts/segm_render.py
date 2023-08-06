#!python

import argparse
import subprocess
from tqdm import tqdm

from mt import np, pd, cv
import mt.base.concurrency as _bc
import mt.base.path as _p
from mt.geond import Dlt
from mt.geo import transform

from wml.core import logger, s3, imageio as ci
from wml.visionml import sqlite, segm, image
import wml.visionml.muv1 as vm


def get_input_event_id_list(args):
    """Returning a list of qualified event ids."""
    if args.auto:
        event_id_list = segm.get_event_id_list()
    else:
        if args.in_url is None:
            raise ValueError("Please provide an input event_munet.csv.")

        with logger.scoped_info(
            "Loading the dataframe of selected events for rendering", curly=False
        ):
            if s3.is_s3cmd_url(args.in_url):
                csv_filepath = s3.cache(args.in_url, verbose_check=False, logger=logger)
            else:
                csv_filepath = args.in_url
            df = pd.dfload(csv_filepath, show_progress=True)
            logger.info("The dataframe has {} events.".format(len(df)))
            logger.info("Columns: {}".format(df.columns))
            df["event_id"] = df["event_id"].astype(int)

        # update after_ fields to the database if we can
        can_update_after = True
        for postfix in ["id", "url", "width", "height"]:
            field = "after_image_" + postfix
            if not field in df.columns:
                can_update_after = False
                break
        if can_update_after:
            with logger.scoped_info(
                "Updating table wml.event with afer image ids", curly=False
            ):
                df2 = df[["event_id", "after_image_id"]]
                field_map = {"event_id": "id", "after_image_id": "after_image_id"}
                sqlite.merge_fields(
                    df2,
                    table="event",
                    field_map=field_map,
                    if_exists="replace",
                    logger=logger,
                )

        if "use_segmentation" in df.columns:
            df = df[df["use_segmentation"] == 1]
            logger.info(
                "After filtering via the 'use_segmentation' field, there are {} segmented events.".format(
                    len(df)
                )
            )
        event_id_list = df["event_id"].drop_duplicates().tolist()

    # find out which events can be uploaded
    event_cnt = len(event_id_list)
    logger.info("{} wanted segmented events.".format(event_cnt))
    new_event_id_list = []
    for event_id in event_id_list:
        if segm.has_cached(event_id):
            new_event_id_list.append(event_id)
    event_id_list = new_event_id_list
    event_cnt = len(event_id_list)
    logger.info("{} segmented events can be uploaded.".format(event_cnt))

    # make a dataframe with columns ['event_id', 'after_image_url'] from sqlite
    id_name = sqlite.id_key(table="event_segm")
    values = ",".join((str(x) for x in event_id_list))
    query_str = "SELECT event_segm.{id} AS event_id FROM event_segm LEFT JOIN image ON event_segm.after_image_id=image.id WHERE event_segm.{id} IN ({values}) AND image.url IS NOT NULL;".format(
        id=id_name, values=values
    )
    df = pd.read_sql(query_str, sqlite.engine, chunksize=100000)
    event_id_list = df["event_id"].tolist()
    logger.info(
        "{} segmented events can be rendered and uploaded.".format(len(event_id_list))
    )

    if not args.override:
        event_id_set = set(event_id_list)
        logger.info("Determining segmented events that have been uploaded.")
        s3cmd_url_list = s3.list_objects("ml://web/segm/", show_progress=True)
        uploaded_event_id_list = [int(x[-13:-4]) for x in s3cmd_url_list]
        uploaded_event_id_set = set(uploaded_event_id_list)
        common_event_id_set = uploaded_event_id_set & event_id_set
        if len(common_event_id_set) > 0:
            logger.info(
                "{} segmented events have already been uploaded.".format(
                    len(common_event_id_set)
                )
            )
            event_id_list = list(event_id_set - uploaded_event_id_set)
            logger.info(
                "Restricted further to {} events that can be rendered and uploaded.".format(
                    len(event_id_list)
                )
            )

    return event_id_list


def list_s3_objects():
    logger.info("Listing objects uploaded to S3:")
    s3urls = s3.list_objects("ml://web/segm", show_progress=True)
    https_urls = [s3.as_https_url(x) for x in s3urls]
    df = pd.Series(https_urls).to_frame("url")
    logger.info("Saving {} urls to 'segm_s3url.csv':".format(len(https_urls)))
    pd.dfsave(df, "segm_s3url.csv", show_progress=True)


def main(args):
    if args.list:
        return list_s3_objects()

    event_id_list = get_input_event_id_list(args)

    if len(event_id_list) == 0:
        logger.info("No event to render. Quitting.")
        return

    if args.test:
        n = 100
        logger.info("Reducing to first {} events.".format(n))
        event_id_list = event_id_list[:n]

    df = segm.render_images(event_id_list, logger=logger)
    pd.dfsave(df, args.out_csv)

    if args.upload:
        segm.upload_to_s3(df["event_id"].tolist(), logger=logger)

    logger.info("Finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Render after images with segmentation data from our cache."
    )
    parser.add_argument(
        "-a",
        "--auto",
        action="store_true",
        help="Automatically determine the segmented events to be rendered. This option will override '-i'.",
    )
    parser.add_argument(
        "-i",
        "--in_url",
        type=str,
        help="S3cmd url to the input event_munet.csv file containing the data of the events for rendering.",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List of events whose segmentation has been uploaded to S3.",
    )
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="In test mode, we limit the number of events to 100.",
    )
    parser.add_argument(
        "-o",
        "--out_csv",
        type=str,
        default="event_segm.parquet",
        help="Output parquet file containing urls to the rendered after images.",
    )
    parser.add_argument(
        "-u",
        "--upload",
        action="store_true",
        help="Upload rendered results to our S3 bucket upon completion.",
    )
    parser.add_argument(
        "-w",
        "--override",
        action="store_true",
        help="Whether to override existing events on S3.",
    )
    args = parser.parse_args()
    main(args)
