from django.contrib import admin

from carts.models import Cart, CartItem, Coupon

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Coupon)
