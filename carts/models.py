from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')
    qty = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.qty)


class Coupon(models.Model):
    coupon = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True)
    validity_from = models.DateTimeField()
    validity_to = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    discount = models.IntegerField()
    users = models.ManyToManyField(User, null=True, blank=True)
