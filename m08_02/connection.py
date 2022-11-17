from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    conn = None
    try:
        conn = connect(host='mouse.db.elephantsql.com', user='nzckefmu', database='nzckefmu',
                       password='GZF4hN7W8Pk91BmTdClVKshhbP9vOWrU')
        yield conn
    except Error as err:
        print(err)
    finally:
        conn.close()
