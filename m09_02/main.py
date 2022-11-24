from datetime import datetime

from sqlalchemy.orm import joinedload
from sqlalchemy import and_

from database.db import session
from database.models import Student, Teacher


def get_students():
    students = session.query(Student).options(joinedload('teachers')).all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")


def get_students_join():
    students = session.query(Student).join('teachers').all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")


def get_teachers():
    teachers = session.query(Teacher).options(joinedload('students')).all()
    for t in teachers:
        print(vars(t))
        print(f"{[f'id: {s.id} first_name: {s.first_name}' for s in t.students]}")


def get_teachers_filter():
    teachers = session.query(Teacher).options(joinedload('students')).filter(
        and_(Teacher.start_work > datetime(year=2016, month=1, day=1),
             Teacher.start_work < datetime(year=2019, month=1, day=1))
    ).all()
    for t in teachers:
        print(vars(t))
        print(f"{[f'id: {s.id} first_name: {s.first_name}' for s in t.students]}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # get_students()
    # get_students_join()
    # get_teachers()
    get_teachers_filter()
