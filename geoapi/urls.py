from django.urls import path
from geoapi import views

app_name = 'geoapi'

urlpatterns = [
    path('', views.GeoLocation.as_view(), name='geodata'),
]
