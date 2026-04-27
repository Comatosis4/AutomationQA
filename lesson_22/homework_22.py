from lesson_22.body_22 import *

print('Додавання нового студента')
new_student = create_student(session, "Oleg")
print(f'Студент {new_student.name} доданий.')

print('Додавання студента до курсу')
add_student_to_course(session, 3, 2)


print('Отримуємо студентів записаних на курс')
students = get_students_by_course(session, "Math")
for student in students:
    print(student.name)


print('Отримуємо курси на які записаний студент')
courses = get_courses_by_student(session, 20)
for course in courses:
    print(course.title)


print('Оновлюємо ім\'я студента')
upd_name = update_student_name(session, 5, "Oleg Updated")
print(f'Нове ім\'я {upd_name.name}')


print('Видаляємо студента')
delete_student(session, 5)
