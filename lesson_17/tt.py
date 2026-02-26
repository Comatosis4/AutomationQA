import randominfo
import csv

with open("randominfo/data.csv", 'r', newline='', encoding='utf8') as data:
    reader = csv.reader(data)
    rows = list(reader)

rows[0].append('country')

for row in rows[1:]:
    row.append('India')

with open("data_fix.csv", 'w', newline='', encoding='utf8') as data:
    writer = csv.writer(data)
    writer.writerows(rows)

person = randominfo.Person()
print(person.full_name, person.gender, person.country, person.address)