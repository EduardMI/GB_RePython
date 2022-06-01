from django.contrib.sites.shortcuts import get_current_site

from .models import Category


def menu(request):
    # return {'category_list': Category.objects.all()}
    return {'category_list': Category.on_site.all(),
            'site': get_current_site(request.site)}
