from django.views import View
from django.shortcuts import render
import requests
from geoapi import config

access_key = config.api_key
weather_key = config.weather_api_key


class GeoLocation(View):

    def get(self, request):
        if request.method == 'GET':

            geo_url = 'http://api.ipstack.com/check?access_key=' + access_key + '&fields='
            r = requests.get(geo_url).json()

            geodata = {
                'ip': r['ip'],
                'latitude': r['latitude'],
                'longitude': r['longitude'],
                'region_name': r['region_name'],
                'city': r['city'],
                'zip': r['zip'],
            }

            weather_url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid=' + weather_key
            geolat = '{:.2f}'.format(r['latitude'])
            geolon = '{:.2f}'.format(r['longitude'])
            w = requests.get(weather_url.format(str(geolat), str(geolon))).json()
            weatherdata = {
                    'temperature': w['main']['temp'],
                    'description': w['weather'][0]['description'],
                    'icon': w['weather'][0]['icon'],

                }
            context = {
                'geodata': geodata,
                'weatherdata': weatherdata
            }
            return render(request, 'geoapi/index.html', context)