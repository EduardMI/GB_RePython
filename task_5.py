"""
Расширить программу из п. 4:
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений (выбирается случайно) заменить на значения типа 345example
(в обратном порядке, число и строка).
(То есть вы переделываете функцию записи в файл так, чтобы она иногда меняла запись на 345example)

Реализовать функцию поиска определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.

Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
(это ДВЕ ОТДЕЛЬНЫЕ функции которые ВЫВОДЯТ значения, не записывают и не модифицируют файлы)

"""
import os
import re
import string
import random


def create_new_file(length=100):
    file_name = input('Введите имя файла: ')
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            texts_list = [(''.join(random.choice(string.ascii_lowercase) for _ in range(8))) for _ in range(length)]
            number_list = [random.randint(0, 10000) for _ in range(length)]
            out_list = zip(texts_list, number_list)
            for item in out_list:
                file.write(f'{item[0]}{item[1]}\n') if random.randint(1, 100) < 90 \
                    else file.write(f'{item[1]}{item[0]}\n')
        read_file(os.path.abspath(file_name))
    except FileExistsError:
        print('Файл с таким именем уже существует.')


def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line)


def search_substring(path, substring):
    pattern = fr'\d*\w*{substring}\w*\d*'

    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    match = re.search(pattern, text)
    match_all = re.findall(pattern, text)
    print(f'Первое вхождение - {match[0]}') if match else print('Ничего не найдено')
    print(f'Все вхождения - {match_all}') if match_all else None


def replacing_substring(path, substring):
    pattern = fr'\d*\w*{substring}\w*\d*'
    value = 'replaced_string'

    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    print(re.sub(pattern, value, text))


if __name__ == '__main__':
    # create_new_file()
    search_substring('task_5.txt', 'kb')
    replacing_substring('task_5.txt', 'kb')
