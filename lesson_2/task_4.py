"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод __init__, в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
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
    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        discount_price = self.price - self.price * (self.discount / 100)
        return f'Цена со скидкой - {discount_price}'

    def get_parent_data(self):
        return f'{self.name} {self.price}'


if __name__ == '__main__':
    item = ItemDiscount('Велосипед', 3500)
    print(f'Экземпляр родительского класса - {item.name} {item.price}')

    item_report = ItemDiscountReport(item.name, item.price, 25)
    print(f'Экземпляр дочернего класса - {item_report.get_parent_data()}')
    print(item_report)
