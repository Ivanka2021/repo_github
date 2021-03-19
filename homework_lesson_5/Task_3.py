"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('file_2.txt', 'r') as my_file:
    file_2 = []
    poor = []
    my_list = my_file.read().split('\n')
for i in my_list:
    try:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        file_2.append(i[1])
    except IndexError:
        print('Ошибку вызывает этот элемент ->', i)
        raise
print(f'Оклад меньше 20`000 {poor}, средний оклад {sum(map(int, file_2)) / len(file_2)}')


