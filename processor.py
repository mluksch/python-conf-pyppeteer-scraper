import mail_service
import pyconf_scraper_service


async def process():
    locals = await pyconf_scraper_service.scrape_python_confs()
    mail_service.send_mail(locals)
