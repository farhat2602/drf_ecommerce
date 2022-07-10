from django.urls import path
from categories.views import CategoryCreateView, CategoryView


urlpatterns = [
    path('create/', CategoryCreateView.as_view()),
    path('get/<slug>/', CategoryView.as_view())
]
