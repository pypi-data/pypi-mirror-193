#!python

import argparse

from mt import pd, cv
from wml.core import logger, s3
from wml.visionml import event


# textplay() and xplay()


async def main(args, context_vars: dict = {}):
    event_id = int(args.event_id)

    df = await event.get_data(event_id, 4, context_vars=context_vars, logger=logger, verbosity=1)
    df['thumbnail'] = event.rectify_thumbnails(df['thumbnail'])
    for _, row in df.iterrows():
        img = row['thumbnail']
        if img.shape[0] != 300 or img.shape[1] != 400:
            logger.info("nah")
            img = cv.resize(img, (400, 300))
        logger.debug("{}: {}".format(row['image_id'], img.shape))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Utility script to play an event's thumnails as a short video clip.")
    parser.add_argument('-f', '--fps', type=float, default=10.0,
                        help="Frame rate, in fps.")
    parser.add_argument('event_id', type=int,
                        help="The event id to be played.")
    args = parser.parse_args()

    s3.run_main(main, args)
