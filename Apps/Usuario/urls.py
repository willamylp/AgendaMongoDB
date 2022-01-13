from django.urls import path, include
from .views import homeUserLogin,createUser

urlpatterns = [
    path('',homeUserLogin,name="loginUser_home"),
    path('new/',createUser,name="create_user"),
]