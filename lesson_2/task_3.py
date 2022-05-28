"""
Реализовать возможность переустановки значения цены товара в родительском классе.
Проверить, распечатать информацию о товаре.

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

    @name.setter
    def name(self, value):
        self.__name = value

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.name} {self.price}'


if __name__ == '__main__':
    item = ItemDiscount('Велосипед', 3500)
    print(f'Экземпляр родительского класса - {item.name} {item.price}')
    item.name = 'Костыль'
    item.price = 4600

    item_report = ItemDiscountReport(item.name, item.price)
    print(f'Экземпляр дочернего класса - {item_report.get_parent_data()}')
