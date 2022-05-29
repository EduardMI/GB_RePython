from django.views.generic import ListView

from .models import Goods


class GoodsListView(ListView):
    model = Goods
    template_name = 'goods_list.html'
    ordering = ['-create_date']
