'''Tables, views and matviews in VisionML DB.'''

# these frames form a directed-acyclic graph that needs a proper management
import networkx as _nx
import mt.sql.psql as _dp


class Frame(object):
    '''An ML frame.

    Parameters
    ----------
    name : str
        name of the frame, including schema if any
    '''

    def __init__(self, name, schema='ml'):
        self.name = name
        self.schema = schema
        self.frame_sql_str = _dp.frame_sql(self.name, schema=self.schema)

    def __repr__(self):
        return self.frame_sql_str


G = _nx.DiGraph()  # the global ML graph of frames


class Table(Frame):
    '''An ML table.

    Parameters
    ----------
    name : str
        name of the frame, including schema if any
    schema : str, optional
        schema name. Default to 'public'.
    '''

    def __init__(self, name, schema='ml'):
        super(Table, self).__init__(name, schema=schema)
        G.add_node(self)


class View(Frame):
    '''Wrapper of a create SQL query to create/remove/refresh a PG view or matview.

    Parameters
    ----------
    name : str
        name of the [mat]view, including schema if any
    is_matview : bool
        whether it is a materialized view or not
    schema : str, optional
        schema name. Default to 'public'.
    create_sql : str
        query string defining the view (e.g. 'SELECT ...')
    drop_cascade : bool
        whether to drop 'cascade' or not
    parent_frames : list
        list of instances of Frame representing the parent frames
    '''

    def __init__(self, name, is_matview, schema='ml', create_sql=None, drop_cascade=True, parent_frames=[]):
        super(View, self).__init__(name, schema=schema)
        G.add_node(self)
        self.is_matview = is_matview

        drop_suffix = 'CASCADE' if drop_cascade else 'RESTRICT'

        if create_sql is None:
            self.refresh_sql = None
            self.create_sql = None
        elif is_matview:
            self.refresh_sql = "REFRESH MATERIALIZED VIEW {};".format(
                self.frame_sql_str)
            self.create_sql = "CREATE MATERIALIZED VIEW {} AS {}".format(
                self.frame_sql_str, create_sql)
        else:
            self.refresh_sql = None
            self.create_sql = "CREATE VIEW {} AS {}".format(
                self.frame_sql_str, create_sql)

        for parent_frame in parent_frames:
            G.add_edge(parent_frame, self)


# ----- useful functions -----


def find(view_name, schema='ml'):
    '''Finds the view/matview instance from its name.

    Parameters
    ----------
    view_name : str
        name of the view/matview to be searched for
    schema : str, optional
        schema name. Default to 'public'.

    Returns
    -------
    View or None
        the corresponding View instance or None if not found
    '''
    for v in G.nodes:
        if isinstance(v, View) and _dp.frame_sql(view_name, schema=schema) == v.frame_sql_str:
            return v

    return None  # to assert not found


def drop_view(view, conn, nb_trials=3, logger=None):
    '''Drops a view/matview and all of its descendants.

    Parameters
    ----------
    view : View
        the view to be dropped
    conn : sqlalchemy.engine.base.Engine
        connection engine
    nb_trials: int
        number of query trials
    logger: logging.Logger or None
        logger for debugging
    '''
    return _dp.drop_frame(view.name, conn, schema=view.schema, restrict=False, nb_trials=nb_trials, logger=logger)


def drop(view_name, conn, schema='ml', nb_trials=3, logger=None):
    '''Drops a view/matview and all of its descendants.

    Parameters
    ----------
    view_name : str
        name of the view/matview to be dropped
    conn : sqlalchemy.engine.base.Engine
        connection engine
    schema : str, optional
        schema name. Default to 'public'.
    nb_trials: int
        number of query trials
    logger: logging.Logger or None
        logger for debugging
    '''

    view_sql_str = _dp.frame_sql(view_name, schema=schema)

    v = find(view_name, schema=schema)
    if v is None:
        logger.warning("View '{}' not found. Skipped.".format(view_sql_str))
        return

    drop_view(v, conn, nb_trials=nb_trials, logger=logger)


def drop_all(conn, nb_trials=3, logger=None):
    '''Drops all views/matviews and all of their descendants.

    Parameters
    ----------
    conn : sqlalchemy.engine.base.Engine
        connection engine
    nb_trials: int
        number of query trials
    logger: logging.Logger or None
        logger for debugging
    '''
    for v in G.nodes:
        if isinstance(v, View):
            drop_view(v, conn, nb_trials=nb_trials, logger=logger)


def refresh(views, conn, logger=None):
    '''Refreshes a list of views.

    Parameters
    ----------
    views : list
        list of views to be removed
    conn : sqlalchemy.engine.base.Engine
        connection engine
    logger : logging.Logger or equivalent
        logger for debugging
    '''
    for view in views:
        if view.refresh_sql is None:
            continue
        if logger:
            logger.info(view.frame_sql_str)
        _dp.exec_sql(view.refresh_sql, conn, logger=logger)


def create(views, conn, logger=None):
    '''Creates a list of views.

    Parameters
    ----------
    views : list
        list of views to be removed
    conn : sqlalchemy.engine.base.Engine
        connection engine
    logger : logging.Logger or equivalent
        logger for debugging
    '''
    for view in views:
        if view.create_sql is None:
            continue
        if _dp.frame_exists(view.name, conn, schema=view.schema):
            if logger:
                logger.info("View '{}' exists. Skipped.".format(
                    view.frame_sql_str))
        else:
            if logger:
                logger.info(view.frame_sql_str)
            _dp.exec_sql(view.create_sql, conn, logger=logger)
