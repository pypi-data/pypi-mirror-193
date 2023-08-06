# pylint: disable=import-outside-toplevel

"""Just for backward compatibility.
"""


import sqlalchemy as sa


def engine_execute(engine, query_str):
    with engine.begin() as conn:
        query = sa.text(query_str)
        return conn.execute(query)
