from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def create_connection():
    conn = None
    try:
        conn = connect(host='localhost', user='postgres', database='postgres', password='567234')
        yield conn
    except Error as err:
        print(err)
    finally:
        conn.close()

