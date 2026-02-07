# Заданий список кортежів (ім'я, прізвище, вік, професія, місце проживання):
# Додайте свій новий запис на початок даного списку.
# У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
# Перевірте, чи всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30. Виведіть результат перевірки

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
people_records.insert(0, ('Oleh', 'Cherniai', 29, 'QA', 'Kyiv'))
print(people_records)
people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records)
ind = [6, 10, 13]
for num in ind:
    if people_records[num][2] >= 30:
        print(f'{people_records[num][0]} старше 30ти')
    else:
        print(f'{people_records[num][0]} молодше 30ти')