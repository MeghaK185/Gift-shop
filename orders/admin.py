from django.contrib import admin

# Register your models here.
from .models import Order,OrderItem,Cart,CartItem

admin.site.register(Order)

admin.site.register(OrderItem)

admin.site.register(Cart)

admin.site.register(CartItem)
