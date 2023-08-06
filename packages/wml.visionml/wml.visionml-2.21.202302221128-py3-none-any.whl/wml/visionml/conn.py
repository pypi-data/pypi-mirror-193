import sqlalchemy as sa

from mt import net
from mt.base import logger
from mt.base.deprecated import deprecated_func


__all__ = [
    "get_muv1_engine",
    "get_taxonomy_engine",
    "get_winnowdb_engine",
    "muv1ro_engine",
    "muv1rl_engine",
    "muv1rw_engine",
    "winnow_engine",
]


def get_muv1_engine(
    db="muv1",
    user="mlwrangler",
    read_only=False,
    muv1_connection_type: str = None,
    logger=None,
):
    """Get a connection engine to muv1 db. Only connectable when the muv1 tunnel is open.

    Parameters
    ----------
    db : str
        name of database. Valid values are 'muv1', 'visionml'
    user : str
        name of user. Valid values are 'mlwrangler', 'mumaster'
    read_only : bool
        whether or not to use a read-only connection. Only valid if db=='muv1' and
        `muv1_connection_type` is None.
    muv1_connection_type : {'rw', 'rl', 'ro', None}
        New argument to replace `read_only`. 'rw' means read-write. 'ro' means read-only for
        general purposes. 'rl' means read-only for large requests.
    logger : logging.Logger or equivalent
        logger for debugging

    Returns
    -------
    engine : sqlalchemy.engine.Engine
        connection engine to the server

    Notes
    -----
    Your machine must have port 5434 forwarded (potentially via SSH tunnelling) to the muv1 db. Ask MT!
    """
    if user == "mlwrangler":
        details = "mlwrangler:MLwrangler"
    elif user == "mumaster":
        details = "mumaster:wind-fancy-return"
    else:
        raise ValueError("Unknown user '{}'".format(user))

    if muv1_connection_type is None:
        muv1_connection_type = "ro" if read_only else "rw"

    # MT-HACK
    if db != "muv1":
        port_number = 5434
    elif muv1_connection_type == "ro":
        port_number = 5436
    elif muv1_connection_type == "rw":
        port_number = 5434
    elif muv1_connection_type == "rl":
        port_number = 5437
    else:
        raise ValueError(
            "Unknown 'muv1_connection_type' value {}.".format(muv1_connection_type)
        )

    for x in ["localhost", "wml-host", "172.17.0.1"]:
        if net.is_port_open(x, port_number):
            db_string = "postgresql://{}@{}:{}/{}".format(details, x, port_number, db)
            break
    else:
        raise IOError(
            "Unable to find an open port to connect to the '{}' db server.".format(db)
        )

    if logger:
        logger.debug("Connection string: {}".format(db_string))

    return sa.create_engine(db_string)


try:
    muv1ro_engine = get_muv1_engine(muv1_connection_type="ro")
    muv1ro_engine.__doc__ = (
        """The read-only connection engine to muv1 db. For general purposes.

    # Class docstring

    """
        + muv1ro_engine.__doc__
    )
except OSError:
    logger.warn_last_exception()
    logger.warn("Setting muv1ro_engine to None.")
    muv1ro_engine = None

try:
    muv1rl_engine = get_muv1_engine(muv1_connection_type="rl")
    muv1rl_engine.__doc__ = (
        """The read-only connection engine to muv1 db. For large requests.

    # Class docstring

    """
        + muv1ro_engine.__doc__
    )
except OSError:
    logger.warn_last_exception()
    logger.warn("Setting muv1rl_engine to None.")
    muv1rl_engine = None

try:
    muv1rw_engine = get_muv1_engine(muv1_connection_type="rw")
    muv1rw_engine.__doc__ = (
        """The read-write connection engine to muv1 db.

    # Class docstring

    """
        + muv1rw_engine.__doc__
    )
except OSError:
    logger.warn_last_exception()
    logger.warn("Setting muv1rw_engine to None.")
    muv1rw_engine = None


def get_taxonomy_engine():
    """Get connection to taxonomy db. Only connectable when the muv1 tunnel is open.

    Notes
    -----
    Your machine must have port 5434 forwarded (potentially via SSH tunnelling) to the muv1 db. Ask MT!
    """
    db_string = "postgresql://mphan:Minhtri_W1nn0w_User@localhost:5434/taxonomy"
    return sa.create_engine(db_string)


def get_winnowdb_engine(logger=None):
    """Get a connection engine to Winnow db. Only connectable when the pritunl VPN is connected.

    Parameters
    ----------
    logger : logging.Logger or equivalent
        logger for debugging

    Returns
    -------
    engine : sqlalchemy.engine.Engine
        connection engine to the server
    """
    # check if mysql-connector is installed
    try:
        from mysql import connector
    except ImportError:
        msg = "Please pip install mysql-connector to connect to Winnow DB via Python."
        if logger:
            logger.warning(msg)
        raise ImportError(msg)

    port_number = 3306

    for x in [
        "winnow-mysql-prod-reader.winnowsolutions.com",
        "operations-prod.cluster-ro-c4ae6beafj0v.us-east-1.rds.amazonaws.com",
        "localhost",
        "172.17.0.1",
        "gh2-sd",
        "gh2-wn",
    ]:
        if net.is_port_open(x, port_number):
            db_string = (
                "mysql+mysqlconnector://minhtri:WeLoveFood2004@{}:{}/winnow_db".format(
                    x, port_number
                )
            )
            break
    else:
        raise IOError("Unable to find an open port to connect to the winnow db server.")

    if logger:
        logger.debug("Connection string: {}".format(db_string))

    engine = sa.create_engine(db_string)
    return engine


try:
    winnow_engine = get_winnowdb_engine()
    winnow_engine.__doc__ = (
        """The read-only connection engine to winnow db.

    # Class docstring

    """
        + winnow_engine.__doc__
    )
except OSError:
    logger.warn_last_exception()
    logger.warn("Setting winnow_engine to None.")
    winnow_engine = None
