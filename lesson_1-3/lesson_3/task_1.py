"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением.
В функции необходимо реализовать поиск имени файла (с расширением), а затем «выделение» имени файла (без расширения).
Расширений может быть несколько (например testfile.tar.gz).
"""
import os.path


def get_full_name(file):
    full_path = os.path.abspath(file)
    name = full_path.split('\\')[-1].split('.')[0]
    return name


if __name__ == '__main__':
    print(get_full_name('task_1.py'))
    print(get_full_name('testfile.tar.gz'))
