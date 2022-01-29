from django.urls import path

from .views import CreateShare, ListShare

urlpatterns = [
    path('newshared/<int:id>/', CreateShare, name="create_share"),
    path('listshare/', ListShare.as_view(), name="list_share"),
]
