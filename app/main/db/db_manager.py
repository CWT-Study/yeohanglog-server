from app.main.db.db_config import db_session
from pymongo.database import Database

USER_TABLE = "user"
TRIP_TABLE = "trip"
TRIP_LOG_TABLE = "triplog"


@db_session
def push_db_coll(table, dict, conn: Database = None):
    conn[table].insert(dict)


@db_session
def update_db_coll(table, dict, conn: Database = None):
    None


@db_session
def find_and_modify_db_coll(table, query_dict, set_dict, isNewColl = True, conn: Database = None):
    return conn[table].find_and_modify(query_dict, set_dict, isNewColl)


@db_session
def pop_db_coll(table, query_dict, conn: Database = None):
    return conn[table].find(query_dict)


@db_session
def pop_db_coll_to_list(table, query_dict, conn: Database = None):
    return list(conn[table].find(query_dict))


@db_session
def pop_db_all_coll(table, conn: Database = None):
    return conn[table].find()


@db_session
def pop_db_all_coll_to_list(table, conn: Database = None):
    return list(conn[table].find())
