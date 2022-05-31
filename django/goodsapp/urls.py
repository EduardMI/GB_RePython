from django.urls import path
from .views import GoodsListView, GoodsCategoryListView

app_name = 'goodsapp'

urlpatterns = [
    path('', GoodsListView.as_view(), name='main'),
    path('category/<int:pk>', GoodsCategoryListView.as_view(), name='category'),
]