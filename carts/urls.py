from django.urls import path

from carts.views import CartItemCreate, CartItemDelete

urlpatterns = [
    path('add_to_cart/', CartItemCreate.as_view()),
    path('remove_from_cart/', CartItemDelete.as_view()),
]
