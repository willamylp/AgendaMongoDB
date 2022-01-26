from django.urls import path

from .views import CreateShare

urlpatterns = [
    path('compartilhado/', CreateShare, name="create_share"),
]
