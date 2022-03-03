import requests, json
from Queries import Queries
from Url import Url

cidade = input('Indique a cidade: ')

# Construção da URL
base_url = "http://api.openweathermap.org/data/2.5/weather"
url = Url(Queries(cidade).getQueries(), base_url)
url = url.getUrl()

# HTTP Request
resposta = requests.get(url)

# Checking the status request
if resposta.status_code == 200:
    data = resposta.json()
    
    main = data['main']
    
    temperatura = main['temp']
    umidade     = main['humidity']
    pressao     = main['pressure']
    temp_min    = main['temp_min']
    temp_max    = main['temp_max']

    report = data['weather']

    print(f'Cidade: {cidade}')
    print(f'Temperatura: {int(temperatura)} °C')
    print(f'Úmidade: {umidade} %')
    print(f'Pressão: {pressao} kPa')
    print(f'Temp Min: {(temp_min)} °C')
    print(f'Temp Máx: {(temp_max)} °C')
else:
    print('Error in HTTP request!')
