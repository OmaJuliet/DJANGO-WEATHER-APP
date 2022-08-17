from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b0977df3fd0d2b4779d160b3ceb4fef4').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+ ' ' + 'long' + ', ' + str(json_data['coord']['lat'])+ ' ' + 'lat',
            "humidity": str(json_data['main']['humidity'])+'%',
            # "sunrise": str(json_data['sys']['sunrise']),
            "wind_speed": str(json_data['wind']['speed'])+'m/s',
            "wind_degree": str(json_data['wind']['deg'])+'%',
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure'])+'hPa',
        }

    else:
        city = '' 
        data = {}
    return render(request, "weather/index.html", {'city': city, 'data': data})
