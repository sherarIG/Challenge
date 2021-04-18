import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, table_name):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param table_name: the name of the table that the function will create
    :return:
    """
    sql_create_table = """ CREATE TABLE IF NOT EXISTS %s (
                               id INTEGER,
                               url TEXT
                               ); """ % table_name
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def add_record(conn, table, record):
    """ adds a record to the table provided as a parameter
        :param conn: Connection object
        :param table: Name of the table in which the record is inserted
        :param record: list with two elements key : id, value : url
        :return: if the insert was successful, id of the last row inserted, else 0
        """
    sql = ''' INSERT INTO %s (id, url) VALUES(?,?) ''' % table
    try:
        cur = conn.cursor()
        cur.execute(sql, record)
        return cur.lastrowid
    except Exception as err:
        print('Insert Failed: %s\nError: %s' % (sql, str(err)))
        return 0
