from faker import Faker

from database.db import session
from database.models import Student, Teacher, TeacherStudent

fake = Faker()


def add_student(teacher_ids: list):
    teachers = session.query(Teacher).filter(Teacher.id.in_(teacher_ids)).all()
    student = Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        cell_phone=fake.phone_number(),
        address=fake.address(),
        teachers=teachers
    )
    session.add(student)
    session.commit()
    return student


def update_student(student_id: int, teacher_ids: list):
    teachers = session.query(Teacher).filter(Teacher.id.in_(teacher_ids)).all()
    student = session.query(Student).filter_by(id=student_id).first()
    student.teachers = teachers
    session.commit()
    return student


def remove_student(student_id: int):
    session.query(Student).filter(Student.id == student_id).delete()
    session.commit()


if __name__ == '__main__':
    r = add_student([1, 3, 4])
    print(vars(r))
    #
    # r = update_student(r.id, [3, 4])
    # remove_student(12)
