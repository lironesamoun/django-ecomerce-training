from django import template
from core.models import Order, OrderItem


register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, is_ordered=False)
        try:
            order_item = OrderItem.objects.get(user=user, is_ordered=False)
            return order_item.quantity
        except OrderItem.DoesNotExist:
            return 0

    return 0
