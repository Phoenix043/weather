from django.urls import path
from .views import WeatherDetailView,WeatherListView,WeatherUpdateView,WeatherDeleteView,AllWeatherListView

urlpatterns = [
    path('weather/<str:city>/', WeatherDetailView.as_view(), name='weather_detail'),
    path('weather/', WeatherListView.as_view(), name='weather_list'),
    path('weather/<str:city>/update/', WeatherUpdateView.as_view(), name='weather_update'),
    path('weather/<str:city>/delete/', WeatherDeleteView.as_view(), name='weather_delete'),
    path('weathers/all/', AllWeatherListView.as_view(), name='all_weather_list')
]

