from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from Apps.Agenda import urls as agenda_urls
from Apps.Usuario import urls as usurio_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(usurio_urls),name="home"),
    path('agenda/', include(agenda_urls),name="agenda"),
    path('accounts/', include('django.contrib.auth.urls')),
]