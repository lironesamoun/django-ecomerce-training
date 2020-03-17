from django.shortcuts import render
from .models import *
# Create your views here.


def item_list(request):

    context = {
        'items': Item.objects.all(),
    }
    return render(request, "core/home-page.html", context)
