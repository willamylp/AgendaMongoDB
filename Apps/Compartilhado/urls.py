from django.urls import path

from .views import CreateShare

urlpatterns = [
    path('newshared/<int:id>', CreateShare, name="create_share"),
]
