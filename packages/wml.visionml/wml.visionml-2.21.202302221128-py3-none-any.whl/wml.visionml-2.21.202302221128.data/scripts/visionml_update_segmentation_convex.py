#!python

'''Updates the v6_segmentation_convex table in muv1 db's ML schema.'''

import pandas as _pd

import mt.sql.psql as _dp
import wml.visionml as _wv
import wml.visionml.muv1 as _vm
from wml.core import logger, home_dirpath
import mt.base.path as _p


def identify_modified_events(valid_df, convex_df):
    s = valid_df.index.isin(convex_df.index)
    event_list = valid_df[~s].index.tolist()
    valid_df = valid_df[s][['last_updated']]
    valid_df.columns = ['valid_last_updated']
    df = valid_df.join(convex_df, how='inner')
    event_list += df[df['last_updated'] != df['valid_last_updated']].index.tolist()
    return event_list


def main():
    valid_df = _vm.read_v6_segmentation_valid(logger=logger)
    convex_df = _vm.read_v6_segmentation_convex(cache_only=True, logger=logger)

    event_list = identify_modified_events(valid_df, convex_df)

    df1 = convex_df[~convex_df.index.isin(event_list)] # reusable convex rows
    logger.info("Reusing {} events.".format(len(df1)))

    df2 = valid_df[valid_df.index.isin(event_list)][['last_updated', 'mask_contours']]
    if len(df2) == 0:
        logger.info("No need to sync.")
    else:
        logger.info("Generating {} convex hulls.".format(len(df2)))
        df2['mask_convex_xy'] = df2['mask_contours'].apply(_vm.convert_mask_contours_to_mask_convex_xy)
        df2 = df2.drop('mask_contours', axis=1)

        df = _pd.concat([df1, df2], sort=True)
        filepath = _p.join(home_dirpath, 'muv1db', 'ml', 'v6_segmentation_convex.parquet')
        logger.info("Writing the {}-row table to '{}'".format(len(df), filepath))
        _dp.writesync_table(_wv.muv1rw_engine, filepath, 'v6_segmentation_convex', 'event_id', hash_name='last_updated', schema='ml', engine_ro=_wv.muv1ro_engine, logger=logger)

    logger.info("Finished.")


if __name__ == '__main__':
    main()
