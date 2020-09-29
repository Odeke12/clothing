from django import template
from shop.models import Order

register = template.Library()# to register the template tag

@register.filter
def cart_item_count(user): # function name of the template tag 
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0  