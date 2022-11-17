from connection import create_connection

if __name__ == '__main__':
    sql_text = "ALTER TABLE users ADD COLUMN phone varchar(30);"

    with create_connection() as conn:
        if conn is not None:
            c = conn.cursor()
            c.execute(sql_text)
            c.close()
            conn.commit()
