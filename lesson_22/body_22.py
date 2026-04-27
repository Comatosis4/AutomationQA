import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from contract.db_orm import Base
from contract.db_orm.student_course import Student_Orm, Course_Orm
from faker import Faker

f = Faker()
load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

courses = [
    Course_Orm(title="Math"),
    Course_Orm(title="Physics"),
    Course_Orm(title="Biology"),
    Course_Orm(title="History"),
    Course_Orm(title="Programming"),
]

students = []
for _ in range(20):
    student = Student_Orm(
        name=f.first_name()
    )
    student.courses = f.random_elements(
        elements=courses,
        length=f.random_int(min=1, max=3),
        unique=True
    )
    students.append(student)

session.add_all(courses)
session.add_all(students)
session.commit()


def create_student(session, name):
    student = Student_Orm(name=name)
    session.add(student)
    session.commit()
    return student

def add_student_to_course(session, student_id, course_id):
    student = session.get(Student_Orm, student_id)
    course = session.get(Course_Orm, course_id)
    s_name = student.name
    c_title = course.title

    if student and course:
        student.courses.append(course)
        session.commit()
        print(f'Студент {s_name} доданий до курсу: {c_title}')

def get_students_by_course(session, course_title):
    course = session.query(Course_Orm).filter_by(title=course_title).first()

    if not course:
        return []

    return course.students

def get_courses_by_student(session, student_id):
    student = session.query(Student_Orm).filter_by(id=student_id).first()

    if not student:
        return []

    return student.courses

def update_student_name(session, student_id, new_name):
    student = session.get(Student_Orm, student_id)
    if student:
        student.name = new_name
        session.commit()
    return student

def delete_student(session, student_id):
    student = session.get(Student_Orm, student_id)
    name = student.name
    if student:
        session.delete(student)
        session.commit()
        print(f'Студент {name} був видалений')