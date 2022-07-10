from django.urls import path

from electronics.views import SmartphoneCreateView, SmartphoneListView, LaptopCreateView, LaptopListView

urlpatterns = [
    path('smartphone/create/', SmartphoneCreateView.as_view()),
    path('smartphone/', SmartphoneListView.as_view()),
    path('laptop/create/', LaptopCreateView.as_view()),
    path('laptop/', LaptopListView.as_view()),
]