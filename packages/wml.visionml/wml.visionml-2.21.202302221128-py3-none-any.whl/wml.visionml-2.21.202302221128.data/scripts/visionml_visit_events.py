#!python

import argparse as _ap

from mt import pd
from wml.core import logger, s3
from wml.visionml import event


async def main(args, context_vars: dict = {}):
    try:
        df = pd.dfload(args.filepath)
    except:
        logger.warn_last_exception()
        logger.error("Unable to load the dataframe '{}'.".format(args.filepath))
        return

    if args.event_id not in df.columns:
        logger.error("Field '{}' does not exist in the dataframe.".format(args.event_id))
        return

    event_id_list = df[args.event_id].drop_duplicates().tolist()
    logger.info("Loaded {} event ids.".format(len(event_id_list)))

    logger.info("The next step may take a long time. Be patient.")
    event.visit_events(event_id_list, context_vars=context_vars, logger=logger, verbosity=0)


if __name__ == '__main__':
    parser = _ap.ArgumentParser(
        description='Utility script to visit all events from a dataframe.')
    parser.add_argument('-e', '--event_id', type='str', default='event_id',
                        help="Name of the field that contains all the event ids.")
    parser.add_argument('filepath', type=str,
                        help="The path to the dataframe file to be loaded from.")
    args = parser.parse_args()

    s3.run_main(main, args)
