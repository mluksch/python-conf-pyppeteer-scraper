import datetime

from pyppeteer import launch

BASE_URL = 'https://www.python.org'


async def scrape_python_confs():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(BASE_URL)
    results = []
    li_list = await page.querySelectorAll(".shrubbery .menu li")
    for el in li_list:
        try:
            time = await el.querySelector("time")
            dt = await page.evaluate('el => el.getAttribute("datetime")', time)
            event = await el.querySelector('a')
            event_title = await page.evaluate('el => el.textContent', event)
            event_link = await page.evaluate('el => el.getAttribute("href")', event)
            results.append({
                "datetime": datetime.datetime.fromisoformat(dt.strip()),
                "event_title": event_title,
                "link": f"{BASE_URL}{event_link}"
            })
        except Exception as e:
            pass
    await browser.close()
    return results
