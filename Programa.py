import requests, json
from Queries import Queries
from Url import Url

city = input('Indique a cidade: ')

# Build Url
base_url = "http://api.openweathermap.org/data/2.5/weather"
url = Url(Queries(city).getQueries(), base_url)
url = url.getUrl()

# HTTP Request
response = requests.get(url)

# Checking the status request
if response.status_code == 200:
    data = response.json()
    main = data['main']

    temperature = main['temp']
    humidity    = main['humidity']
    pressure    = main['pressure']
    temp_min    = main['temp_min']
    temp_max    = main['temp_max']

    report = data['weather']

    print(f'City: {city}')
    print(f'Temperature: {temperature} ºC')
    print(f'Humidity: {humidity} %')
    print(f'Pressure: {pressure} kPa')
    print(f'Temp Min: {temp_min} ºC')
    print(f'Temp Máx: {temp_max} ºC')
else:
    print('Error in HTTP request!')
