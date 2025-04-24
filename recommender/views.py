from django.shortcuts import render, get_object_or_404
from .models import Drink
import requests

API_KEY = 'd12112bfc7792cd2628fdc6229ad0250'  # حتماً کلید واقعی خودتو بذار

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location_by_ip(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        data = response.json()
        return data.get('city'), data.get('country_code')
    except Exception as e:
        print("Location error:", e)
        return None, None

def get_temperature(city, country_code, api_key):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=metric&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        return data['main']['temp']
    except Exception as e:
        print("Weather error:", e)
        return None

def recommend_drink(request):
    ip = get_client_ip(request)
    city, country_code = get_location_by_ip(ip)

    # اگر location نگرفت، دستی مقدار بده (مثلاً تهران، ایران)
    if not city or not country_code:
        city = 'Gonbad-e Qabus'
        country_code = 'IR'

    temp = get_temperature(city, country_code, API_KEY)

    drinks = []
    if temp is not None:
        if temp > 25:
            drinks = Drink.objects.filter(temperature_type='cold')
        elif 15 <= temp <= 25:
            drinks = Drink.objects.filter(temperature_type='warm')
        else:
            drinks = Drink.objects.filter(temperature_type='hot')

    return render(request, 'recommend/recommend.html', {
        'drinks': drinks,
        'temp': temp,
        'city': city
    })
def drink_detail(request, slug):
    drink = get_object_or_404(Drink, slug=slug)
    return render(request, 'recommend/drink_detail.html', {
        'drink': drink
    })
def home(request):
    return render(request, 'home.html')  # اینجا می‌توانید صفحه اصلی خود را نمایش دهید
