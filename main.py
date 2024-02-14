import csv

with open('students.csv', encoding='utf8') as file:
    '''
    Открываем файл
    '''
    reader = csv.reader(file, delimiter=',')
    data = list(reader)[1:]
    count_class = {}
    sum_class = {}
    for id, name, title, clas, score in data:
        if 'Хадаров Владимир' in name:
            print(f'Ты получил: <{score}>, за проект - <{title}>')
        if score != 'None':
            sum_class[clas] = sum_class.get(clas, 0) + (int(score) if score != 'None' else 0)
            count_class[clas] = count_class.get(clas, 0)+1
    for el in data:
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]]/count_class[el[-2]], 3)
with open('student_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.writer(file)
    w.writerow(['id', 'name', 'title', 'class', 'score'])
    w.writerows(data)