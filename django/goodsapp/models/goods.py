from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models
from django.utils.timezone import now

from goodsapp.models.category import Category


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
    category = models.ManyToManyField(Category)
    site = models.ManyToManyField(Site)

    objects = models.Manager()
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['-create_date']
