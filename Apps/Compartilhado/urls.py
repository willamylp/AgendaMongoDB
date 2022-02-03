from django.urls import path

from .views import ListShare, create_share

urlpatterns = [
    path('newshared/<int:id>/', create_share, name="create_share"),
    path('listshare/', ListShare.as_view(), name="list_share"),
]
