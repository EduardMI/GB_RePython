from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField('Название', max_length=64)
    create_date = models.DateTimeField(auto_now_add=now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-create_date']
