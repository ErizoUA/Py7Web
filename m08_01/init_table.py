from connection import create_connection
from psycopg2 import DatabaseError


def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        c.close()
        conn.commit()
    except DatabaseError as e:
        print(e)


if __name__ == '__main__':
    sql_text = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(130),
        email VARCHAR(130),
        password VARCHAR(130),
        age NUMERIC CHECK (age > 1 AND age < 120)
    );
    """
    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_text)
