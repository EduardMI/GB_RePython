from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField('Название', max_length=64)
    create_date = models.DateTimeField(auto_now_add=now)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-create_date']
