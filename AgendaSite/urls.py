from Apps.Agenda import urls as agenda_urls
from Apps.Compartilhado import urls as compartilhado_urls
from Apps.Usuario import urls as usurio_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(usurio_urls), name="home"),
    path('agenda/', include(agenda_urls), name="agenda"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('compartilhado/', include(compartilhado_urls), name="compartilhado"),
]
