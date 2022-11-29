from datetime import datetime

from sqlalchemy.orm import joinedload
from sqlalchemy import and_

from database.db import session
from database.models import Student, Teacher, TeacherStudent


def get_students():
    students = session.query(Student).options(joinedload('teachers'), joinedload('contacts')).all()
    for s in students:
        print(vars(s))
        print(s.fullname)
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")
        print(f"{[f'id: {c.id} first_name: {c.first_name}' for c in s.contacts]}")


def get_students_join():
    students = session.query(Student).join('teachers').all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")
        print(f"{[f'id: {c.id} first_name: {c.first_name}' for c in s.contacts]}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_students()
    # get_students_join()
