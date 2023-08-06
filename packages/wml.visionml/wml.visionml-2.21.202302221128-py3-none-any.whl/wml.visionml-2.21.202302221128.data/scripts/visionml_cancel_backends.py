#!python

'''Cancels all backend transactions related to the ML schema in muv1 db.'''


import mt.sql.psql as _dp
import wml.visionml as _wv
from wml.core import logger


def main():
    _dp.pg_cancel_all_backends(_wv.muv1rw_engine, schema='ml', logger=logger)


if __name__ == '__main__':
    main()
