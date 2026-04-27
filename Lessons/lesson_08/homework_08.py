class Student:
    def __init__(self, name, surname, age, average):
        self.name = name
        self.surname = surname
        self.age = age
        self.average = average

    def change_average(self, new_average):
        self.average = new_average
        print(f'New average: {self.average}')

new_student = Student('Oleh', 'Cherniai', 29, 4.9)
print(new_student.name)
print(new_student.surname)
print(new_student.age)
print(new_student.average)
new_student.change_average(5.0)