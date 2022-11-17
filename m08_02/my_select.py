from connection import create_connection

if __name__ == '__main__':
    sql_select_where = """
    SELECT id, name, age
    FROM users
    WHERE age > 30
    ORDER BY name, age DESC
    LIMIT 15
    """
    sql_select_one = "SELECT * FROM users WHERE id=%s"

    with create_connection() as conn:
        if conn is not None:
            c = conn.cursor()
            c.execute(sql_select_where)
            r = c.fetchall()
            print(r)
            c.execute(sql_select_one, (226, ))
            r = c.fetchone()
            print(r)
            c.close()
            conn.commit()
