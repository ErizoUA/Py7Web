from faker import Faker

from database.db import session
from database.models import Teacher

fake = Faker()
count_teachers = 6


def create_teachers():
    for _ in range(count_teachers):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date="-10y")
        )
        session.add(teacher)
    session.commit()


if __name__ == '__main__':
    create_teachers()
