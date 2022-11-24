import random

from faker import Faker

from database.db import session
from database.models import Student, ContactPerson

fake = Faker()


def create_persons():
    students = session.query(Student).all()

    for _ in range(len(students) + 5):
        student = random.choice(students)
        pr = ContactPerson(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
            student=student  # student_id=student.id
        )
        session.add(pr)
    session.commit()


if __name__ == '__main__':
    create_persons()
