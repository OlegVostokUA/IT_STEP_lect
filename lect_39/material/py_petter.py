import asyncio
# pip install pyppeteer
from pyppeteer import launch


async def main():
    # browser launch
    browser = await launch()
    # make new page
    page = await browser.newPage()
    # go to web-page
    await page.goto('https://www.youtube.com')
    # make screenshot page
    await page.screenshot({'path': 'screen.png'})
    # browser close
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())


### error chromium
# chromium_downloader.py
# -- > 32   REVISION = '1232556'#os.environ.get('PYPPETEER_CHROMIUM_REVISION', __chromium_revision__)
