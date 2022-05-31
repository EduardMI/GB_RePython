from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Goods


class GoodsListView(ListView):
    model = Goods
    queryset = Goods.objects.prefetch_related('category').all()
    template_name = 'goods_list.html'


class GoodsCategoryListView(ListView):
    model = Goods
    template_name = 'category_list.html'

    def get_queryset(self):
        queryset = Goods.objects.prefetch_related('category').filter(category=self.kwargs['pk'])
        return queryset
