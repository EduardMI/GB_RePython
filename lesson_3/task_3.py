"""
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None. Если есть значения,
которым не хватило ключей, их необходимо отбросить.
"""
import random
import string


def get_dict(key, val):
    len_key = len(key)
    len_val = len(val)

    if len_key > len_val:
        for _ in range(len_key - len_val):
            val.append(None)

    new_dict = {k: v for k, v in zip(key, val)}
    return new_dict


if __name__ == '__main__':
    list_key = [random.randint(1, 10000) for _ in range(int(input('Введите кол-во элементов списка ключей: ')))]
    list_value = [string.ascii_letters[random.randint(1, 10000)] for _ in range(
        int(input('Введите кол-во элементов списка значений: ')))]
    print(get_dict(list_key, list_value))
