import csv
with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    data = list(reader)[1:]