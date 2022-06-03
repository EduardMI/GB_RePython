"""
Задача 3.
Разработать целочисленный генератор случайных чисел.
В функцию передавать начальную и конечную границу диапазона генерации (выдавать значения из диапазона включая концы).
Заполнить этими данными словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”,
а значение сгенеренное случайное число.  Вывести содержимое словаря.
(Усложненный вариант по желанию*): Не использовать стандартный модуль python random.
"""
import random


def get_rand_nums(start, end):
    nums_list = []
    nums_dict = {}
    quantity = end - start + 1
    flag = True
    while flag:
        rand_num = random.randint(start, end)
        if rand_num not in nums_list:
            nums_list.append(rand_num)
            quantity -= 1
        if quantity == 0:
            flag = False

    for index, value in enumerate(nums_list):
        nums_dict.update({f'elem_{index +1 }': value})

    return nums_dict


if __name__ == '__main__':
    start_nums = int(input('Введите первое целое число: '))
    end_nums = int(input('Введите второе целое число: '))
    print(get_rand_nums(start_nums, end_nums))
