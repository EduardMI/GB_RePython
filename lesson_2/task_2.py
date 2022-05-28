"""
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.name} {self.price}'


if __name__ == '__main__':
    item = ItemDiscount('Велосипед', 3500)
    item_report = ItemDiscountReport(item.name, item.price)

    print(f'Экземпляр родительского класса - {item.name} {item.price}')
    print(f'Экземпляр дочернего класса - {item_report.get_parent_data()}')
