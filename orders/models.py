from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    PAY_CHOICES = (
        ('Card', ("Card")),
        ('Cash', ("Cash")),
    )
    payment_method = models.CharField(max_length=128, choices=PAY_CHOICES)
    order_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')
    qty = models.IntegerField()
    total_price = models.DecimalField(max_digits=9, decimal_places=2)


