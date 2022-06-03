"""
Задача 4.
Написать программу «Банковский депозит».
Клиент банка делает депозит на определенный срок.

В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).

Проценты начисляются на депозит в конце каждого месяца.

Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада (в месяцах),
а на выходе возвращать сумму вклада на конец срока.

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


def calc_total_deposit(deposit, term):
    total_deposit = 0

    for bank_rate in bank_rates:
        if bank_rate['min_sum'] <= deposit < bank_rate['max_sum']:
            total_deposit = deposit
            percent = bank_rate[term] / 100

            total_deposit += deposit * percent * (term / 12)
    return total_deposit


if __name__ == '__main__':
    sum_deposit = float(input('Введите сумму вклада от 1000 до 1 000 000: '))
    number_months = int(input('Введите кол-во месяцев вклада 6, 12 или 24: '))

    print(calc_total_deposit(sum_deposit, number_months))
