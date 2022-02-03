from django.urls import path

from .views import create_user, home_user_login

urlpatterns = [
    path('', home_user_login, name="loginUser_home"),
    path('new/', create_user, name="create_user"),
]
