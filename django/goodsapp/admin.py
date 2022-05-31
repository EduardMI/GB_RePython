from django.contrib import admin

from .models import Goods
from .models.category import Category

admin.site.register(Goods)
admin.site.register(Category)
