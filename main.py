import csv
with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    lf = list(reader)[1:]
    for id, name, title, clas, score in lf:
        print(id)