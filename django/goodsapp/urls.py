from django.urls import path
from .views import GoodsListView

app_name = 'goodsapp'

urlpatterns = [
    path('', GoodsListView.as_view(), name='main'),
]