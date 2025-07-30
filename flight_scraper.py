import asyncio
from playwright.async_api import async_playwright

async def fetch_flight_price(origin, destination, date):
    url = f"https://www.skyscanner.net/transport/flights/{origin}/{destination}/{date}/"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, timeout=90000)
        await page.wait_for_selector('.day-list-item', timeout=60000)
        
        # Try to extract the lowest price
        price_elements = await page.query_selector_all('.Price_mainPrice__1-qxw')
        prices = []
        for el in price_elements:
            txt = await el.inner_text()
            price = ''.join(filter(str.isdigit, txt))
            if price:
                prices.append(int(price))
        await browser.close()
        return min(prices) if prices else None