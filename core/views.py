from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.


class HomeView(ListView):
    model = Item
    template_name = 'core/home-page.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/product-page.html'

    def get_object(self):
        # Nous récupérons l'objet, via la super-classe
        article = super(ItemDetailView, self).get_object()

        return article  # Et nous retournons l'objet à afficher


def checkout(request):
    return render(request, "core/checkout-page.html")


def item_list(request):

    context = {
        'items': Item.objects.all(),
    }
    return render(request, "core/home-page.html", context)
