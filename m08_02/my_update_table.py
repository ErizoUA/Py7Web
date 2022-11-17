from connection import create_connection
from faker import Faker

fake = Faker()

if __name__ == '__main__':
    sql_text = "UPDATE users SET phone = %s WHERE id = %s;"

    with create_connection() as conn:
        if conn is not None:
            c = conn.cursor()
            for i in range(400):
                c.execute(sql_text, (fake.phone_number(), i))
            c.close()
            conn.commit()
