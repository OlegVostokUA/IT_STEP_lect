# import requests
# from bs4 import BeautifulSoup as bs
#
#
# def parse_courses():
#     headers = {
#         "Accept": "application/json, text/plain, */*",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0"
#     }
#
#     url = 'https://privatbank.ua/rates-archive'
#     page = requests.get(url, headers=headers)
#     #print(page.text)
#     result = bs(page.text, 'html.parser')
#     currency_block = result.find('div', class_='courses-currencies')
#
#     curr_pair = currency_block.findAll('div', class_='currency-pairs')
#
#     data = []
#     for i in curr_pair:
#         var = i.find('div', class_='purchase')
#         var = var.text
#         var2 = i.find('div', class_='sale')
#         var2 = var2.text
#
#         data.append(var)
#         data.append(var2)
#
#     print(data)
#
#
#
#
# parse_courses()

import asyncio

# import pyppeteer
from pyppeteer import launch

async def main():
    browser = await launch()

    page = await browser.newPage()

    await page.goto('https://privatbank.ua/rates-archive')

    await page.screenshot({'path': 'screen.png'})

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())