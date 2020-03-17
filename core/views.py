from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, "core/home-page.html")


def checkout(request):
    return render(request, "core/checkout-page.html")


def product(request):
    return render(request, "core/product-page.html")


def item_list(request):

    context = {
        'items': Item.objects.all(),
    }
    return render(request, "core/home-page.html", context)
