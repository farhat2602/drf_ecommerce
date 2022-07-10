from django.urls import path

from products.views import ProductDetailView

urlpatterns = [
    path('detail/<pk>/', ProductDetailView.as_view()),
]