"""
Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False
"""


def check_float_or_int():
    flag = True
    while flag:
        number = input('Введите число: ')
        try:
            number = float(number)
            flag = False
        except ValueError:
            print('Введите целое или дробное число')
            continue
        list_num = list(map(int, str(number).split('.')))
        if not list_num[1]:
            return 'Число целое'
        else:
            return f'Число дробное\n {list_num[0] == list_num[1]}'


if __name__ == '__main__':
    print(check_float_or_int())
