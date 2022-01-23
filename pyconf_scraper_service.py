import datetime

from pyppeteer import launch

BASE_URL = 'https://www.python.org'


async def scrape_python_confs():
    try:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(BASE_URL)
        shrubbery_list = await page.querySelectorAll(".shrubbery")
        conf_root = shrubbery_list[1]
        conf_list = await page.evaluate(
            """
            el => Object.values(el.querySelectorAll("li")).map(item => {
                return {
                    "event_title": item.querySelector("a").text,
                    "link": item.querySelector("a").getAttribute("href"),
                    "datetime": item.querySelector("time").getAttribute("datetime"),
                }    
            })
            """, conf_root)
        await browser.close()
        return [{
            "datetime": datetime.datetime.fromisoformat(item["datetime"].strip()),
            "event_title": item["event_title"],
            "link": f"{BASE_URL if item['link'].startswith('/') else ''}{item['link']}"
        } for item in conf_list]
    except Exception as e:
        print(f"error: {e}")
        return []
