from connection import create_connection
from faker import Faker
from random import randint

fake = Faker()

if __name__ == '__main__':
    sql_text = """
    INSERT INTO users (name, email, password, age) VALUES(%s, %s, %s, %s)
    """
    with create_connection() as conn:
        if conn is not None:
            c = conn.cursor()
            for _ in range(400):
                c.execute(sql_text, (fake.name(), fake.email(), fake.password(), randint(2, 100)))
            c.close()
            conn.commit()
