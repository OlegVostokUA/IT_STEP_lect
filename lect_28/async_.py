import time
import requests
import asyncio
from aiohttp import ClientSession


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:

            weather_json = await response.json()
            print(f'{city}: {weather_json["weather"][0]["main"]}')


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))

    for task in tasks:
        await task


cities = ['Delhi', 'Istanbul', 'Tokyo', 'London', 'New York', 'Hamburg', 'Berlin',
          'Kyiv', 'Rome', 'San Francisco', 'Los angeles', 'Chicago']


start = time.time()
asyncio.run(main(cities))
end = time.time()
print('TOTAL ', end - start)
