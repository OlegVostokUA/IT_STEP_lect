import time
import requests


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

    weather_json = requests.get(url=url, params=params).json()
    print(f'{city}: {weather_json["weather"][0]["main"]}')


def main(cities_):
    for city in cities_:
        get_weather(city)


cities = ['Delhi', 'Istanbul', 'Tokyo', 'London', 'New York', 'Hamburg', 'Berlin',
          'Kyiv', 'Rome', 'San Francisco', 'Los angeles', 'Chicago']


start = time.time()
main(cities)
end = time.time()
print('TOTAL ', end - start)
