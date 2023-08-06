#!python

import argparse

from wml.core import s3
from wml.visionml import segm, logger


async def main(args, context_vars: dict = {}, logger=logger):
    segm.sync_locally(logger=logger)
    _, _, inserted_list, updated_list = await segm.update_from_muv1db(event_id_list=None, context_vars=context_vars, logger=logger)

    if args.render:
        event_id_list = inserted_list + updated_list
        df = segm.render_images(event_id_list, logger=logger)

        if not args.no_upload:
            segm.upload_to_s3(df['event_id'].tolist(), logger=logger)
    logger.info("Finished.")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Read-sync the segmented data from muv1 db, optionally rendering and uploading the rendered segmented images to S3.")
    parser.add_argument('-r', '--render', action='store_true',
                        help="Render newly inserted or updated events.")
    parser.add_argument('-n', '--no_upload', action='store_true',
                        help="If set and '-r' is specified, will not upload rendered images to S3. Default is to upload after rendering.")
    args = parser.parse_args()

    s3.run_main(main, args, logger=logger)
