from django.contrib import admin

from .models import Item, Order, OrderItem, BillingAddress, ItemReview, Category, Variation

admin.site.register(Item)

admin.site.register(Order)

admin.site.register(BillingAddress)

admin.site.register(OrderItem)

admin.site.register(ItemReview)

admin.site.register(Category)

admin.site.register(Variation)

