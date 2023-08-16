from django.http import JsonResponse
from django.views import View
import json

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

class AllWeatherListView(View):
    def get(self, request):
        return JsonResponse(weather_data)

class WeatherDetailView(View):
    def get(self, request, city):
        weather_info = weather_data.get(city)
        if weather_info:
            return JsonResponse(weather_info)
        else:
            return JsonResponse({'error': 'City not found'}, status=404)

class WeatherListView(View):
    def post(self, request):
        try:
            new_weather_data = json.loads(request.body)
            city = new_weather_data.get('city')
            if city:
                weather_data[city] = new_weather_data
                return JsonResponse({}, status=201)
            else:
                return JsonResponse({'error': 'City not provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)


class WeatherUpdateView(View):
    def put(self, request, city):
        updated_weather_data = json.loads(request.body)
        existing_data = weather_data.get(city)
        if existing_data:
            existing_data.update(updated_weather_data)
            return JsonResponse(existing_data)
        else:
            return JsonResponse({'error': 'City not found'}, status=404)


class WeatherDeleteView(View):
    def delete(self, request, city):
        if city in weather_data:
            del weather_data[city]
            return JsonResponse({}, status=204)
        else:
            return JsonResponse({'error': 'City not found'}, status=404)
        



