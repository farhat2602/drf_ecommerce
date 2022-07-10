from django.urls import path

from shops.views import ShopCreateView, ShopDetailView

urlpatterns = [
    path('create/', ShopCreateView.as_view()),
    path('detail/<pk>/', ShopDetailView.as_view()),
]