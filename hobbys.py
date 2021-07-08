import csv
def replace(file): #Функция удаления ненужных знаков
    for el in range(len(file)):
        file[el] = str(file[el]).replace(',', ' ').replace('[', '').replace(']', '').replace("'","")

with open('users.csv', encoding='utf8', newline='') as f:
    reader = csv.reader(f)
    names = list(reader)
with open('hobby.csv', encoding='utf8', newline='') as f:
    reader = csv.reader(f)
    hobby = list(reader)

replace(hobby)
replace(names)

zip_iterator = zip(names, hobby)
for el in zip_iterator:
    print(el[0],':',el[1])

dictionary = dict(zip(names,hobby)) #Создаём словарь для переноса в файл


with open('data.csv', 'w',encoding='utf8',newline='') as f:
    w = csv.writer(f)
    w.writerows(dictionary.items())
