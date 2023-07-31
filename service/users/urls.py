from django.urls import path
from .views import (
    UserLoginView,
    UserCreateView,
    UserLogoutView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]
