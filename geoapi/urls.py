from django.urls import path
from geoapi import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'geoapi'

urlpatterns = [
    path('', views.GeoLocation.as_view(), name='geodata'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
