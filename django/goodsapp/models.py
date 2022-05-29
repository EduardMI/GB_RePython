from django.db import models
from django.utils.timezone import now


class Goods(models.Model):
    PIECE = 'PI'
    PACKAGE = 'PA'
    UNITS = (
        (PIECE, 'шт.'),
        (PACKAGE, 'уп.')
    )

    name = models.CharField(verbose_name='Название', max_length=64)
    create_date = models.DateTimeField(auto_now_add=now)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    unit = models.CharField(verbose_name='Ед. измерения', choices=UNITS, max_length=2)
    supplier = models.CharField(verbose_name='Поставщик', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
