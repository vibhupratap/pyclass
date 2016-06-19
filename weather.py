api_key = '5ed5bbe8f9a62ca0bba60effe916604a'

import requests
import json


cities = ['Oakland','Orlando','Sunnyvale']
prev = 0
mycity = None
for citi in cities:
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+citi+'&appid=5ed5bbe8f9a62ca0bba60effe916604a')
    # print json.loads(r.text)
    # print citi + ":" + str(json.loads(r.text)['main']['temp'])
    if prev == 0:
        prev = json.loads(r.text)['main']['temp']
        mycity = citi
    elif json.loads(r.text)['main']['temp'] > prev:
        prev = json.loads(r.text)['main']['temp']
        mycity = citi

print mycity + ':' + str(prev)
    # print r.text

# {"coord": {"lon": -0.13, "lat": 51.51},
#  "weather": [{"id": 500, "main": "Rain", "description": "light rain", "icon": "10n"}],
#  "base": "cmc stations",
#  "main": {"temp": 288.74, "pressure": 1019, "humidity": 86,
#           "temp_min": 288.35, "temp_max": 289.26},
#  "wind": {"speed": 1.03, "deg": 217, "gust": 3.08},
#  "rain": {"1h": 0.24}, "clouds": {"all": 92}, "dt": 1466372928,
#  "sys": {"type": 3, "id": 10115, "message": 0.003,
#          "country": "GB", "sunrise": 1466307777, "sunset": 1466367684},
#  "id": 2643743, "name": "London", "cod": 200}
