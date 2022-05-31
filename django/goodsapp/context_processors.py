from .models import Category


def menu(request):
    return {'category_list': Category.objects.all()}
