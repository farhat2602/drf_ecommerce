from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from carts.models import Cart, CartItem
from orders.models import Order

User = get_user_model()


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


@receiver(post_save, sender=Order)
def recreate_cart(sender, instance, created, **kwargs):
    if created:
        instance.cart = Cart.objects.filter(user=instance.buyer)
        instance.cart.update(is_active=False)
        if instance.cart:
            Cart.objects.create(user=instance.buyer)


@receiver(post_save, sender=CartItem)
def get_total_price(sender, instance, created, **kwargs):
    cart = Cart.objects.get(user=instance.cart.user, is_active=True)
    total = 0
    for cart_item in cart.cart_item.all():
        total += cart_item.total_price
        cart.total_price = total
        cart.save()


@receiver(pre_delete, sender=CartItem)
def get_total_price(sender, instance, created, **kwargs):
    cart = Cart.objects.get(user=instance.cart.user, is_active=True)
    total = cart.total_price - instance.total_price
    cart.total_price = total
    cart.save()
