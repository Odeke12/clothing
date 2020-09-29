from django import template
from shop.models import Item

register = template.Library()

@register.filter
def gender_male_count(user):
    qs = Item.objects.filter(gender='M')
    return qs.count()

@register.filter
def gender_female_count(user):
    qs = Item.objects.filter(gender='F')
    return qs.count()

@register.filter
def shoe_count(user):
    qs = Item.objects.filter(category='S')
    return qs.count() 
    


