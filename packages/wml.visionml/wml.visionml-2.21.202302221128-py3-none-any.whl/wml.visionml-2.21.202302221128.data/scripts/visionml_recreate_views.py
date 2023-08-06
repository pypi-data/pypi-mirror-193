#!python

"""Recreates all derived views in VisionML DB."""


import argparse as _ap
import wml.visionml as wv
import wml.visionml.view as wvv
import mt.sql.psql as _dp
from wml.core import logger
from wml.visionml.conn import muv1rw_engine, muv1ro_engine

# Key definitions from muv1 db. For every event:
#   - There is a set of images associated with it, defined in the public.event_image table.
#   - An image may or may not be approved, defined in the public.image table.
#   - There may be some before images.
#   - There may be some after images.
#   - There may be an image selected by a reviewer for training, called the reviewer image. The reviewer image is represented as the best image in the exports.event_with_best table.
#   - There may be segmentation, in which case there is a seg before image and a seg after image.
#
# Data team may give some extra events where the before and training image may be updated (viewed as before and after image in the extra data table).
#
# ML redefines their own versions of training image, after image, and before image. They are estimated, in decreasing order of priority, as the followings:
#   - ML after image: last approved after image, after image.
#   - ML training image: seg after image, ext after image, reviewer image, ML after image.
#   - ML before image: seg before image, ext before image, last approved before image, last before image, previous event's ML after image.
# NOTE: Still work in progress. Currently after image is used as training image.


def construct_v6():
    views_v6 = []

    # ---- tables ----

    v6_param = wvv.Table("v6_param")
    v6_bat_box = wvv.Table("v6_bat_box")
    v6_bat_bin_type = wvv.Table("v6_bat_bin_type")
    v6_labelbox_raw = wvv.Table("v6_labelbox_raw")
    v6_bindet_prediction = wvv.Table("v6_bindet_prediction")
    v6_target_group_dist = wvv.Table("v6_target_group_dist")
    v6_target_taxcode_per_group_dist = wvv.Table("v6_target_taxcode_per_group_dist")
    v6_taxonomy_hierarchy_node = wvv.Table("v6_taxonomy_hierarchy_node")
    v6_taxonomy_hierarchy_closure = wvv.Table("v6_taxonomy_hierarchy_closure")
    v6_taxonomy_term = wvv.Table("v6_taxonomy_term")
    v6_taxonomy_taxtree_base = wvv.Table("v6_taxonomy_taxtree_base")
    v6_event_munet_extra_data = wvv.Table("v6_event_munet_extra_data")
    v6_site_details = wvv.Table("v6_site_details")

    # ----- event v6_image base -----

    # MT-NOTE: we go around like this to make sure that images of the same event have the same value with the event's date value

    v6_image_base = wvv.View(
        "v6_image_base",
        False,  # it takes a few minutes to materialize
        create_sql="""
            SELECT t1.image_id, t1.event_id, t2.taken_at, t3.installation_id
                FROM event_image t1
                    INNER JOIN public.image t2 ON t1.image_id=t2.id
                    INNER JOIN event t3 ON t1.event_id=t3.id
                WHERE t3.installation_id IS NOT NULL
                    AND t1.event_id IS NOT NULL
                    AND t1.image_id IS NOT NULL
                    AND t2.path LIKE 'https%%'
                    AND t2.taken_at IS NOT NULL
                    AND t2.width IS NOT NULL
                    AND t2.height IS NOT NULL
                    AND t1.is_before IS NOT NULL
                    AND t1.is_after IS NOT NULL
                    AND t1.approved IS NOT NULL
            ;""",
        parent_frames=[],
    )
    views_v6.append(v6_image_base)

    v6_event_attrs_time = wvv.View(
        "v6_event_attrs_time",
        False,  # it takes a few minutes to materialize
        create_sql="""
            SELECT
                event_id,
                min(taken_at) first_image_taken_at,
                max(taken_at) last_image_taken_at,
                max(image_id) random_image_id,
                COUNT(*) num_images
              FROM ml.v6_image_base
              GROUP BY event_id
            ;""",
        parent_frames=[v6_image_base],
    )
    views_v6.append(v6_event_attrs_time)

    # ----- event v6_image views -----

    v6_image = wvv.View(
        "v6_image",
        False,  # it takes a few minutes to materialize
        create_sql="""
            SELECT i.image_id, i.event_id, t2.path, i.taken_at, i.installation_id, et.last_image_taken_at::date AS date, t2.width, t2.height, t1.is_before, t1.is_after, t1.approved, t1.is_prediction
                FROM ml.v6_image_base i
                    LEFT JOIN event_image t1 ON i.image_id=t1.image_id
                    LEFT JOIN public.image t2 ON i.image_id=t2.id
                    LEFT JOIN ml.v6_event_attrs_time et ON i.event_id=et.event_id
            ;""",
        parent_frames=[v6_image_base, v6_event_attrs_time],
    )
    views_v6.append(v6_image)

    # ----- labelbox views -----

    v6_labelbox_old_primary_bin = wvv.View(
        "v6_labelbox_old_primary_bin",
        False,
        create_sql="""
            WITH t4 AS (
                SELECT t1.name,
                    t1.image_id,
                    t2.installation_id,
                    t2.date,
                    t2.taken_at,
                    t3.bin_type,
                    t3.bin_shape,
                    t3.bin_size,
                    t3.bin_color,
                    GREATEST(0::bigint, LEAST(t1.min_x, t1.max_x)) AS min_x,
                    GREATEST(0::bigint, t2.height - 1 - GREATEST(t1.min_y, t1.max_y)) AS min_y,
                    LEAST(t2.width - 1, GREATEST(t1.min_x, t1.max_x)) AS max_x,
                    LEAST(t2.height - 1, t2.height - 1 - LEAST(t1.min_y, t1.max_y)) AS max_y
                  FROM ml.v6_bat_box t1
                   JOIN ml.v6_image t2 ON t1.image_id = t2.image_id
                   JOIN ml.v6_bat_bin_type t3 ON t3.installation_id = t2.installation_id
                  WHERE t2.taken_at >= t3.start_time AND t2.taken_at < t3.end_time AND t2.width > 320
            ) SELECT DISTINCT * FROM t4;""",
        parent_frames=[v6_bat_box, v6_bat_bin_type, v6_image],
    )
    views_v6.append(v6_labelbox_old_primary_bin)

    v6_labelbox_primary_bin = wvv.View(
        "v6_labelbox_primary_bin",
        False,
        create_sql="""
             SELECT t4.id,
                t5.image_id,
                t5.installation_id,
                t5.date,
                t5.taken_at,
                t4.project_name,
                t4.bin_type,
                t4.bin_shape,
                t4.min_x,
                t4.min_y,
                t4.max_x,
                t4.max_y,
                (t4.project_name IN ('Bin detect evaluation set'))::integer is_eval
               FROM ( SELECT DISTINCT ON (t3.id) t3.project_name,
                        t3.id,
                        t3.image_url,
                        t3.bin_json::json ->> 'bin_type'::text AS bin_type,
                        t3.bin_json::json ->> 'bin_area'::text AS bin_area,
                        t3.bin_json::json ->> 'bin_shape'::text AS bin_shape,
                        (t3.bin_json::json ->> 'min_x'::text)::integer AS min_x,
                        (t3.bin_json::json ->> 'min_y'::text)::integer AS min_y,
                        (t3.bin_json::json ->> 'max_x'::text)::integer AS max_x,
                        (t3.bin_json::json ->> 'max_y'::text)::integer AS max_y
                       FROM ( SELECT t1."ID" AS id,
                                t1."Project Name" AS project_name,
                                t1."Labeled Data" AS image_url,
                                t2.value AS bin_json,
                                ((t2.value::json -> 'if_multiple_bins_in_image'::text) IS NOT NULL)::integer AS is_primary
                               FROM ml.v6_labelbox_raw t1
                                 JOIN LATERAL json_array_elements_text(t1."Label"::json -> 'Bin - aligned (default)'::text) t2(value) ON true
                            UNION
                             SELECT t1."ID" AS id,
                                t1."Project Name" AS project_name,
                                t1."Labeled Data" AS image_url,
                                t2.value AS bin_json,
                                ((t2.value::json -> 'if_multiple_bins_in_image'::text) IS NOT NULL)::integer AS is_primary
                               FROM ml.v6_labelbox_raw t1
                                 JOIN LATERAL json_array_elements_text(t1."Label"::json -> 'Bin - misaligned'::text) t2(value) ON true) t3
                      ORDER BY t3.id, t3.is_primary DESC) t4
                 JOIN ml.v6_image t5 ON t5.path = t4.image_url
            ;""",
        parent_frames=[v6_labelbox_raw, v6_image],
    )
    views_v6.append(v6_labelbox_primary_bin)

    v6_bindet201908_raw = wvv.View(
        "v6_bindet201908_raw",
        False,
        create_sql="""
             SELECT t2.image_id,
                t2.installation_id,
                t2.date,
                t2.taken_at,
                t2.bin_type,
                t2.bin_shape,
                t2.min_x,
                t2.min_y,
                t2.max_x,
                t2.max_y,
                t2.is_eval
               FROM ( SELECT DISTINCT ON (t1.image_id) t1.image_id,
                        t1.installation_id,
                        t1.date,
                        t1.taken_at,
                        t1.bin_type,
                        t1.bin_shape,
                        t1.min_x,
                        t1.min_y,
                        t1.max_x,
                        t1.max_y,
                        t1.is_eval
                       FROM ( SELECT pb.image_id,
                                pb.installation_id,
                                pb.date,
                                pb.taken_at,
                                pb.bin_type,
                                pb.bin_shape,
                                pb.min_x,
                                pb.min_y,
                                pb.max_x,
                                pb.max_y,
                                pb.is_eval
                               FROM ml.v6_labelbox_primary_bin pb
                              WHERE pb.bin_shape = ANY (ARRAY['round'::text, 'square'::text, 'rectangular'::text])
                            UNION
                             SELECT opb.image_id,
                                opb.installation_id,
                                opb.date,
                                opb.taken_at,
                                opb.bin_type,
                                opb.bin_shape,
                                opb.min_x,
                                opb.min_y,
                                opb.max_x,
                                opb.max_y,
                                0 is_eval
                               FROM ml.v6_labelbox_old_primary_bin opb
                              WHERE opb.bin_shape = ANY (ARRAY['round'::text, 'square'::text, 'rectangular'::text])) t1) t2
              ORDER BY t2.installation_id, t2.taken_at
            ;""",
        parent_frames=[v6_labelbox_primary_bin, v6_labelbox_old_primary_bin],
    )
    views_v6.append(v6_bindet201908_raw)

    v6_bindet201908_image_hist_per_siteday = wvv.View(
        "v6_bindet201908_image_hist_per_siteday",
        False,
        create_sql="""
             WITH image_hist_per_siteday AS (
                     SELECT max(raw.installation_id) AS installation_id,
                        max(raw.date) AS date,
                        count(*) AS image_cnt
                       FROM ml.v6_bindet201908_raw raw
                      GROUP BY raw.installation_id, raw.date
                    ), image_hist AS (
                     SELECT avg(image_hist_per_siteday.image_cnt) AS avg_image_cnt
                       FROM image_hist_per_siteday
                    )
             SELECT t2.installation_id,
                t2.date,
                t2.image_cnt,
                t3.avg_image_cnt / t2.image_cnt::numeric AS weight
               FROM image_hist_per_siteday t2
                 JOIN image_hist t3 ON true
            ;""",
        parent_frames=[v6_bindet201908_raw],
    )
    views_v6.append(v6_bindet201908_image_hist_per_siteday)

    # ----- v6_event_best_image ------
    # Best image selected by reviewer. This is the after image for food recognition that has been approved by a reviewer. It is the last-approved image in an event.
    # As of 2021/11/30, there are only 48 events where the best image selected by v6_event_best_image view differs from that selected by v6_event_best_image2 view.

    v6_event_best_image = wvv.View(
        "v6_event_best_image",
        False,
        create_sql="""
            SELECT DISTINCT ON (event_id) event_id, image_id AS best_image_id
              FROM public.event_image
              WHERE approved = 1
              ORDER BY event_id, image_id DESC
            ;""",
        parent_frames=[],
    )
    views_v6.append(v6_event_best_image)

    v6_event_best_image2 = wvv.View(
        "v6_event_best_image2",
        False,
        create_sql="SELECT event_id, image_id AS best_image_id FROM exports.event_best_image;",
        parent_frames=[],
    )
    views_v6.append(v6_event_best_image2)

    # ----- v7_event_with_prev ------
    # The previous event of a given event from the same device. The before image selected by reviewers for food recognition is the best image of the previous event.

    v7_event_with_prev = wvv.View(
        "v7_event_with_prev",
        False,
        create_sql="SELECT id AS event_id, prev_event_id, installation_id, approved FROM exports.event_with_prev;",
        parent_frames=[],
    )
    views_v6.append(v7_event_with_prev)

    # ----- segmentation ------

    # less-strict but faster variant of metadata.segmentation_latest
    v6_segmentation_latest = wvv.View(
        "v6_segmentation_latest",
        False,
        create_sql="""
            WITH seg1 AS (
              SELECT DISTINCT ON(seg.event_id)
                  seg.event_id,
                  seg.before_image_id,
                  seg.after_image_id,
                  seg.before_image_crop,
                  seg.after_image_crop,
                  seg.mask_contours,
                  seg.mask_boxes,
                  seg.markers,
                  seg.review_status,
                  seg.updated AS last_updated
                FROM metadata.segmentation seg
                ORDER BY seg.event_id ASC, seg.updated DESC
            )
            SELECT
                seg1.event_id,
                seg1.before_image_id,
                seg1.after_image_id,
                seg1.before_image_crop,
                seg1.after_image_crop,
                seg1.mask_contours,
                seg1.mask_boxes,
                seg1.last_updated
              FROM seg1
              WHERE seg1.review_status = 1 AND seg1.markers::text <> 'null'::text AND jsonb_array_length(seg1.mask_contours) <> 0
            ;""",
        parent_frames=[],
    )
    views_v6.append(v6_segmentation_latest)

    # less-strict but faster variant of metadata.segmentation_valid
    # MT-TODO: to update later to use v6_segmentation_latest
    v6_segmentation_valid = wvv.View(
        "v6_segmentation_valid",
        False,
        create_sql="""
            SELECT
                seg1.event_id,
                seg1.before_image_id,
                seg1.after_image_id,
                seg1.before_image_crop,
                seg1.after_image_crop,
                seg1.mask_contours,
                seg1.mask_boxes,
                seg1.last_updated
              FROM ml.v6_segmentation_latest seg1
                JOIN event evt ON evt.id = seg1.event_id
                JOIN event_image evtimg ON evtimg.image_id = seg1.after_image_id
              WHERE evtimg.approved = 1 AND evt.approved = 1
            ;""",
        parent_frames=[v6_segmentation_latest],
    )
    views_v6.append(v6_segmentation_valid)

    # complementary to v6_segmentation_valid, but with stuff like image urls, widths and heights and times taken
    v6_segmentation_valid_image_attrs = wvv.View(
        "v6_segmentation_valid_image_attrs",
        False,
        create_sql="""
            SELECT
                seg.event_id,
                seg.last_updated,
                bi.path AS before_image_url,
                bi.width AS before_image_width,
                bi.height AS before_image_height,
                bi.taken_at AS before_image_taken_at,
                ai.path AS after_image_url,
                ai.width AS after_image_width,
                ai.height AS after_image_height,
                ai.taken_at AS after_image_taken_at
              FROM ml.v6_segmentation_valid seg
                JOIN public.image bi ON bi.id = seg.before_image_id
                JOIN public.image ai ON ai.id = seg.after_image_id
            ;""",
        parent_frames=[v6_segmentation_valid],
    )
    views_v6.append(v6_segmentation_valid_image_attrs)

    # status of bin crops in metadata.segmentation
    v6_segmentation_crops = wvv.View(
        "v6_segmentation_crops",
        False,
        create_sql="""
            WITH t1 AS (
                    SELECT
                            event_id,
                            (before_image_crop::json->>0)::float AS bcrop_min_x,
                            (before_image_crop::json->>1)::float AS bcrop_min_y,
                            (before_image_crop::json->>2)::float AS bcrop_max_x,
                            (before_image_crop::json->>3)::float AS bcrop_max_y,
                            (after_image_crop::json->>0)::float AS acrop_min_x,
                            (after_image_crop::json->>1)::float AS acrop_min_y,
                            (after_image_crop::json->>2)::float AS acrop_max_x,
                            (after_image_crop::json->>3)::float AS acrop_max_y
                    FROM metadata.segmentation
            ), t2 AS (
                    SELECT
                            t1.*,
                            (bcrop_min_x < 1 AND bcrop_min_x < bcrop_max_x AND bcrop_max_x > 0 AND bcrop_min_y < 1 AND bcrop_min_y < bcrop_max_y AND bcrop_max_y > 0)::int AS before_crop_has_valid_coordinates,
                            (acrop_min_x < 1 AND acrop_min_x < acrop_max_x AND acrop_max_x > 0 AND acrop_min_y < 1 AND acrop_min_y < acrop_max_y AND acrop_max_y > 0)::int AS after_crop_has_valid_coordinates
                    FROM t1
            ) SELECT
                    t2.*
                    FROM t2
                    WHERE before_crop_has_valid_coordinates = 0 OR after_crop_has_valid_coordinates = 0
            ;""",
        parent_frames=[],
    )
    views_v6.append(v6_segmentation_crops)

    # ----- v6_installation_details views -----

    v6_installation_details = wvv.View(
        "v6_installation_details",
        False,  # it is too small to be a materialized view
        create_sql="""
            SELECT
                t1.id AS installation_id,
                t3.lat,
                t3.lng,
                t3.utc,
                t3.updated
              FROM public.installation t1
                LEFT JOIN public.location t2 ON t1.location_id=t2.id
                LEFT JOIN ml.v6_site_details t3 ON t2.guid=t3.location_guid
              WHERE t3.location_guid is not null
            ;""",
        parent_frames=[v6_site_details],
    )
    views_v6.append(v6_installation_details)

    # ----- v7_event_image_minimal views -----

    v7_event_image_minimal = wvv.View(
        "v7_event_image_minimal",
        False,  # it is too small to be a materialized view
        create_sql="""
            SELECT
                event_id::bigint*10000 + MOD(image_id, 10000) AS event_image_id,
                event_id,
                image_id,
                is_before,
                is_after,
                is_prediction,
                sam_score,
                approved,
                updated
              FROM public.event_image
            ;""",
        parent_frames=[],
    )
    views_v6.append(v7_event_image_minimal)

    # ----- v7_image_compact views -----

    v7_image_compact = wvv.View(
        "v7_image_compact",
        False,  # it is too small to be a materialized view
        create_sql="""
            SELECT
                id,
                path AS url,
                width,
                height,
                taken_at,
                updated
              FROM public.image
            ;""",
        parent_frames=[],
    )
    views_v6.append(v7_image_compact)

    # ----- v7_event_special_image_compact views -----

    v7_event_special_image_compact = wvv.View(
        "v7_event_special_image_compact",
        False,  # it is too small to be a materialized view
        create_sql="""
            SELECT
                event_id,
                before_image_id,
                after_image_id,
                prediction_image_id,
                approved_image_id,
                latest_image_id,
                best_display_image_id,
                updated
              FROM public.event_special_image
            ;""",
        parent_frames=[],
    )
    views_v6.append(v7_event_special_image_compact)

    # ----- v7_annotation_state_events_compact views -----

    v7_annotation_state_events_compact = wvv.View(
        "v7_annotation_state_events_compact",
        False,  # it is too small to be a materialized view
        create_sql="""
            SELECT
                event_id,
                installation_id,
                menu_id,
                best_image AS best_image_id,
                phase,
                rejection_reason,
                best_image_type,
                update_time AS updated
              FROM annotation_state.events
            ;""",
        parent_frames=[],
    )
    views_v6.append(v7_annotation_state_events_compact)

    # ----- v7_merged views -----
    # to replace v7_annotation_state_events_compact

    v7_event_merged = wvv.View(
        "v7_event_merged",
        False,  # it is too small to be a materialized view
        create_sql="""
            SELECT
                event_id,
                events.installation_id,
                events.menu_id,
                best_image AS best_image_id,
                phase,
                rejection_reason,
                best_image_type,
                event.device_id,
                event.weight_g,
                update_time AS updated
              FROM annotation_state.events
                JOIN public.event ON event_id=event.id
            ;""",
        parent_frames=[],
    )
    views_v6.append(v7_event_merged)

    # ----- v7_edge_bin_crop views -----

    # used_bin_crop uses same format as wml.inference.bin_detector (top, left, bottom, right)
    v7_edge_bin_crop = wvv.View(
        "v7_edge_bin_crop",
        False,  # it is too small to be a materialized view
        create_sql="""
            SELECT DISTINCT ON (image_id)
                image_id,
                bin_absent,
                used_bin_crop[2] AS min_x,
                used_bin_crop[1] AS min_y,
                used_bin_crop[4] AS max_x,
                used_bin_crop[3] AS max_y,
                shapes[1] AS shape
              FROM public.site_bin_detector_prediction
            ;""",
        parent_frames=[],
    )
    views_v6.append(v7_edge_bin_crop)

    return views_v6


def main():
    parser = _ap.ArgumentParser(
        description="Utility script to regenerate muv1's ml's views."
    )
    parser.add_argument(
        "command", choices=["draw", "create", "refresh", "recreate", "drop", "drop_all"]
    )
    parser.add_argument(
        "--frame_name",
        default=None,
        type=str,
        help="If provided, the frame name to update, like 'ml.v6_param'",
    )
    args = parser.parse_args()

    views_v6 = construct_v6()

    if args.command == "draw":
        import matplotlib.pyplot as _plt
        import networkx as _nx

        _plt.figure(num=None, figsize=(30, 20), dpi=100)
        _nx.draw(wvv.G, with_labels=True)
        _plt.savefig("graph.jpg")
    elif args.command == "create":
        if not args.frame_name:
            wvv.create(views_v6, muv1rw_engine, logger=logger)
        else:
            raise NotImplementedError("Not done")
    elif args.command == "drop":
        if not args.frame_name:
            raise ValueError("Option '--frame_name' is required but not specified.")
        wvv.drop(args.frame_name, muv1rw_engine, schema="ml", logger=logger)
    elif args.command == "drop_all":
        wvv.drop_all(muv1rw_engine, logger=logger)
    elif args.command == "refresh":
        wvv.refresh(views_v6, muv1rw_engine, logger=logger)
    elif args.command == "recreate":
        if args.frame_name:
            raise NotImplementedError("Not done!")
        wvv.drop_all(muv1rw_engine, logger=logger)
        wvv.create(views_v6, muv1rw_engine, logger=logger)
    else:
        raise ValueError("Unknown command: {}".format(args.command))


if __name__ == "__main__":
    main()
