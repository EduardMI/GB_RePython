"""
Задача 1.

Вывести таблицу умножения в виде:
1 x 1 = 1
1 x 2 = 2
...
1 x 10 = 10
—
2 x 1 = 2
2 x 2 = 4
...
N x 10 = 10N

Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию).
Между разделами вывести разделитель в виде 5 дефисов

"""


def multiplication_table():
    num = input('Введите целое число: ')

    try:
        num = int(num)
    except TypeError:
        print('Не является целым числом!!')

    for i in range(1, num + 1):
        if i != 1:
            print('-----')
        for j in range(1, 11):
            print(f'{i} x {j} = {i * j}')


if __name__ == '__main__':
    multiplication_table()
