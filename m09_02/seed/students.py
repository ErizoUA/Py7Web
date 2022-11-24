from faker import Faker

from database.db import session
from database.models import Student

fake = Faker()
count_teachers = 10


def create_students():
    for _ in range(count_teachers):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
        )
        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()
