from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone
# Create your views here.


class HomeView(ListView):
    model = Item
    paginate_by = 10
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


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # We are not getting objects that has been purchased
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        is_ordered=False)
    # Get the order that has not been completed for an user
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    print(order_qs)
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    # getting the item
    item = get_object_or_404(Item, slug=slug)
    # checking if the user has an order
    order_qs = Order.objects.filter(
        user=request.user,
        is_ordered=False
    )
    # if they have an order
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                is_ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            # order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)
