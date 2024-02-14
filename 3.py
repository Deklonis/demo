import csv
with open('students.csv', encoding='utf8') as file:

    reader = csv.reader(file, delimiter=',')
    data = list(reader)[1:]

pr_id = input()
while pr_id != 'СТОП':
    fl = True
    for id, Name, titleProject_id, clas, score in data:
        name = Name.split()[1][0] + '. ' + Name.split()[0]
        if titleProject_id == pr_id:
            print(f'Проект № <{titleProject_id}> делал: <{name}>он(а) получил(а) оценку - <{score}>.')
            fl = False
    if fl:
        print('Ничего не найдено')
    pr_id = input()