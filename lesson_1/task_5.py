"""
Задача 4.
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого
и последнего. Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.


"""
bank_rate_1 = {'min_sum': 1000,
               'max_sum': 10000,
               6: 5,
               12: 6,
               24: 5}
bank_rate_2 = {'min_sum': 10000,
               'max_sum': 100000,
               6: 6,
               12: 7,
               24: 6.5}
bank_rate_3 = {'min_sum': 100000,
               'max_sum': 1000000,
               6: 6,
               12: 7,
               24: 6.5}
bank_rates = [bank_rate_1, bank_rate_2, bank_rate_3]


def calc_total_deposit(deposit, term, add_deposit):
    total_deposit = 0

    for bank_rate in bank_rates:
        if bank_rate['min_sum'] <= deposit < bank_rate['max_sum']:
            total_deposit = deposit
            percent = bank_rate[term] / 100
            total_deposit += deposit * percent * (term / 12)
            total_deposit += deposit_replenishment(add_deposit, term, percent)
    return total_deposit


def deposit_replenishment(deposit, term, percent):
    deposit += (deposit * percent * ((term - 2) / 12))
    return deposit * (term - 2)


if __name__ == '__main__':
    sum_deposit = float(input('Введите сумму вклада от 1000 до 1 000 000: '))
    number_months = int(input('Введите кол-во месяцев вклада 6, 12 или 24: '))
    add_sum_dep = float(input('Введите фиксированную ежемесячную сумму пополнения вклада: '))

    print(calc_total_deposit(sum_deposit, number_months, add_sum_dep))
