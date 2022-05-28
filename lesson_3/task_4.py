"""
Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение (например example345).
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого.
"""
import os
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
                file.write(f'{item[0]}{item[1]}\n')
        read_file(os.path.abspath(file_name))
    except FileExistsError:
        print('Файл с таким именем уже существует.')


def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line)


if __name__ == '__main__':
    create_new_file()
