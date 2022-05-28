"""
Задача 2.
Реализовать функцию print_directory_contents(path).
Функция принимает имя директории и выводит ее содержимое, включая содержимое
всех поддиректорий (рекурсивно вызывая саму себя).
Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile
"""
import os
import pprint

task_list = []


def print_directory_contents(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        # full_path = os.path.abspath(full_path)
        if os.path.isfile(full_path):
            task_list.append(full_path.replace("\\", "/"))
        else:
            print_directory_contents(full_path)
    return task_list


if __name__ == '__main__':
    task_dir = input('Введите адрес директории для проверки: ')
    pprint.pprint((print_directory_contents(task_dir)))
