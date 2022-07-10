from django.urls import path

from accounts.views import CustomUserRegisterView, CustomUserLoginView, CustomUserLogoutView, PasswordChangeView

urlpatterns = [
    path('register/', CustomUserRegisterView.as_view()),
    path('login/', CustomUserLoginView.as_view()),
    path('logout/', CustomUserLogoutView.as_view()),
    path('password_change/', PasswordChangeView.as_view()),
]