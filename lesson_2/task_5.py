"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе
будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
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


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        return self.name


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return self.price


if __name__ == '__main__':
    item = ItemDiscount('Велосипед', 3500)
    print(f'Экземпляр родительского класса - {item.name} {item.price}')

    item_report_name = ItemDiscountReportName(item.name, item.price)
    item_report_price = ItemDiscountReportPrice(item.name, item.price)

    print(item_report_name.get_info())
    print(item_report_price.get_info())
