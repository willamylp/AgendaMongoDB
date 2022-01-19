from django.urls import path

from .views import createUser, homeUserLogin

urlpatterns = [
    path('', homeUserLogin, name="loginUser_home"),
    path('new/', createUser, name="create_user"),
]
