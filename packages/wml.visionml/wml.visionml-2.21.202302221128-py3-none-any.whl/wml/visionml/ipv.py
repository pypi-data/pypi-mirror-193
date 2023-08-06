"""Image-Pair Verification"""

from mt import pd, logg
import mt.sql.base as sb

from .sqlite import engine


__all__ = ["verify_after_images", "verify_before_images"]


def verify_after_images(
    in_df: pd.DataFrame, missing: str = "skip", logger=None
) -> pd.DataFrame:
    """Verifies if the after images contain new-food.

    We classify whether an after image id has new-food in the following way:

    - If the event has a best image:

      - The event has been rejected during annotation -> 0
      - The event has been accepted and the image id is the same as the best image -> 1
      - Otherwise, treat it as not having a best image.
    - If the event has no best image:

      - The image in the event is approved -> 1
      - The image in the event is rejected -> 0
      - Otherwise -> 0 or skip.

    Parameters
    ----------
    in_df : pandas.DataFrame
        a dataframe consisting of columns ['event_id', 'image_id']
    missing : {'reject', 'skip'}
        whether or not to reject images with missing attributes, no best image or no approval
        rating.
    logger : mt.logg.IndentedLoggerAdapter
        logger for debugging purposes

    Returns
    -------
    `pandas.DataFrame(index='image_id', columns=['after_is_good'])`
        the dataframe of all metadata for the given image ids. Some image ids may be missing if
        they do not exist in the 'ml_image' table of the wml database.
    """

    image_id_list = in_df["image_id"].drop_duplicates().tolist()
    with logg.scoped_info(
        "Verifying whether {} after images/{} events contain new food".format(
            len(image_id_list), len(in_df)
        ),
        logger=logger,
    ):
        with logg.scoped_info("Checking against best images", logger=logger):
            query_str = ",".join((str(x) for x in in_df["event_id"].tolist()))
            query_str = (
                "SELECT event_id, best_image_id, phase FROM ml_events WHERE event_id IN "
                "({});".format(query_str)
            )
            best_df = sb.read_sql(query_str, engine, chunksize=100000, logger=logger)
            best_df = best_df.groupby("event_id").head(1)
            best_df = best_df.set_index("event_id", drop=True)
            df = in_df[["event_id", "image_id"]].join(
                best_df, on="event_id", how="left"
            )

            done_dfs = []
            dfs = []

            s = df["best_image_id"].isnull()
            if s.sum() > 0:
                if logger:
                    logger.info("Found {} events without a best image.".format(s.sum()))
                df1 = df[s][["event_id", "image_id"]].copy()
                dfs.append(df1)
                df = df[~s]

            s = df["phase"].isin(["EVENT_REJECTED", "EVENT_UNKNOWN"])
            if s.sum() > 0:
                if logger:
                    logger.info("Found {} rejected events.".format(s.sum()))
                df1 = df[s][["event_id", "image_id"]].copy()
                df1["after_is_good"] = 0
                done_dfs.append(df1)
                df = df[~s]

            s = ~(
                df["phase"].isin(
                    ["EVENT_APPROVED", "EVENT_BYPASSED", "EVENT_VALIDATED"]
                )
            )
            if s.sum() > 0:
                if logger:
                    logger.info(
                        "Found {} events pending for labelling.".format(s.sum())
                    )
                df1 = df[s][["event_id", "image_id"]].copy()
                dfs.append(df1)
                df = df[~s]

            s = df["best_image_id"] == df["image_id"]
            if s.sum() > 0:
                if logger:
                    logger.info(
                        "Among the {} approved events, {} events have image id matched with "
                        "best image id.".format(len(df), s.sum())
                    )
                df1 = df[s][["event_id", "image_id"]].copy()
                df1["after_is_good"] = 1
                done_dfs.append(df1)
                df = df[~s]

            dfs.append(df[["event_id", "image_id"]].copy())

        if dfs:
            df = pd.concat(dfs)
            with logg.scoped_info(
                "Checking {} events against approved images".format(len(df)),
                logger=logger,
            ):
                df["event_image_id"] = df["event_id"] * 10000 + (df["image_id"] % 10000)
                query_str = ",".join((str(x) for x in df["event_image_id"].tolist()))
                query_str = """
                SELECT
                    event_image_id,
                    approved
                FROM ml_event_image
                WHERE event_image_id IN ({})
            ;""".format(
                    query_str
                )
                approved_df = sb.read_sql(
                    query_str, engine, chunksize=100000, logger=logger
                )
                approved_df = approved_df.set_index("event_image_id", drop=True)
                df = df.join(approved_df, on="event_image_id", how="left")
                df = df.drop("event_image_id", axis=1)

                s = df["approved"].isnull()
                if s.sum() > 0:
                    if missing == "skip":
                        if logger:
                            logger.info(
                                "Skipped {} images without approval rating.".format(
                                    s.sum()
                                )
                            )
                    elif missing == "reject":
                        if logger:
                            logger.info(
                                "Skipped {} images without approval rating.".format(
                                    s.sum()
                                )
                            )
                        df1 = df[s][["event_id", "image_id"]].copy()
                        df1["after_is_good"] = 0
                        done_dfs.append(df1)
                    else:
                        raise ValueError(
                            "Unknown value for argument 'missing': '{}'.".format(
                                missing
                            )
                        )
                    df = df[~s]

                s = df["approved"] >= 1
                if s.sum() > 0:
                    if logger:
                        logger.info(
                            "Found {}/{} approved images.".format(s.sum(), len(df))
                        )
                df = df[["event_id", "image_id"]].copy()
                df["after_is_good"] = s.astype(int)
                done_dfs.append(df)

        df = pd.concat(done_dfs)
        for x in ["event_id", "image_id"]:
            df[x] = df[x].astype(int)
        df = df.sort_values("event_id")

    if logger:
        logger.info(
            "Summary of field 'after_is_good':\n{}".format(
                df.groupby("after_is_good").size()
            )
        )

    return df


def verify_before_images(df: pd.DataFrame, logger=None) -> pd.DataFrame:
    """Verifies if the before images are good enough.

     We classify whether a before image id is good enough in the following ways:

    - If it is the segm before image -> good
    - If it is a good after image of the last event -> good
    - Otherwise: -> bad

     Parameters
     ----------
     df : pandas.DataFrame
         a dataframe consisting of columns ['event_id', 'image_id']
     logger : mt.logg.IndentedLoggerAdapter
         logger for debugging purposes

     Returns
     -------
     `pandas.DataFrame(index='image_id', columns=['before_is_good'])`
         the dataframe of all metadata for the given image ids. Some image ids may be missing if
         they do not exist in the 'ml_image' table of the wml database.
    """

    image_id_list = df["image_id"].drop_duplicates().tolist()
    with logg.scoped_info(
        "Verifying whether {} before images/{} events are good enough".format(
            len(image_id_list), len(df)
        ),
        logger=logger,
    ):
        with logg.scoped_info("Checking against segm data", logger=logger):
            query_str = ",".join((str(x) for x in df["event_id"].tolist()))
            query_str = (
                "SELECT id AS event_id, before_image_id AS segm_before_image_id FROM "
                "event_segm WHERE event_id in ({});".format(query_str)
            )
            segm_df = sb.read_sql(query_str, engine, chunksize=100000, logger=logger)
            segm_df = segm_df.groupby("event_id").head(1)
            segm_df = segm_df.set_index("event_id", drop=True)
            df = df.join(segm_df, on="event_id", how="left")

            done_dfs = []

            s = df["segm_before_image_id"] == df["image_id"]
            if s.sum() > 0:
                if logger:
                    logger.info(
                        "Found {} events using the segm before image.".format(s.sum())
                    )
                df1 = df[s][["event_id", "image_id"]].copy()
                df1["before_is_good"] = 1
                done_dfs.append(df1)
                df = df[~s]

        with logg.scoped_info(
            "Working with {} previous events".format(len(df)), logger=logger
        ):
            # get the previous event id
            query_str = ",".join((str(x) for x in df["event_id"].tolist()))
            query_str = """
                SELECT
                    event_id,
                    prev_event_id
                FROM ml_event_with_prev
                WHERE event_id IN ({})
            ;""".format(
                query_str
            )
            prev_df = sb.read_sql(query_str, engine, chunksize=100000, logger=logger)
            prev_df = prev_df[prev_df["prev_event_id"].notnull()]
            prev_df = prev_df.groupby("event_id").head(1)
            prev_df = prev_df.set_index("event_id", drop=True)
            df = df.join(prev_df, on="event_id", how="left")

            s = df["prev_event_id"].isnull()
            if s.sum() > 0:
                if logger:
                    logger.info(
                        "Found {} events without the previous event.".format(s.sum())
                    )
                df1 = df[s][["event_id", "image_id"]].copy()
                df1["before_is_good"] = 0
                done_dfs.append(df1)
                df = df[~s]

            # verify if the before image is good enough as the after image of the previous event
            df1 = df[["prev_event_id", "image_id"]].copy()
            df1.columns = ["event_id", "image_id"]
            df1 = verify_after_images(df1, missing="reject", logger=logger)
            df1 = df1[["event_id", "after_is_good"]]
            df1.columns = ["prev_event_id", "before_is_good"]
            df1 = df1.set_index("prev_event_id", drop=True)
            df = df.join(df1, on="prev_event_id", how="left")
            df = df[["event_id", "image_id", "before_is_good"]]
            done_dfs.append(df)
            if logger:
                logger.info(
                    "Checked in {} events if their before image is good enough as the "
                    "after image of its previous event.".format(len(df))
                )

        df = pd.concat(done_dfs)
        for x in ["event_id", "image_id"]:
            df[x] = df[x].astype(int)
        df = df.sort_values("event_id")

    if logger:
        logger.info(
            "Summary of field 'before_is_good':\n{}".format(
                df.groupby("before_is_good").size()
            )
        )

    return df
