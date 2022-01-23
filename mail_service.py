import datetime
import os

import requests


def send_mail(locals: [dict]):
    now = datetime.datetime.now()
    # datetime event_title link
    subject = f"{len(locals)} Python-Conferences in {now.strftime('%m/%Y')}"
    content = "\n\n".join(
        [f"({idx + 1}) {local['datetime'].strftime('%d.%m.%Y')} \"{local['event_title']}\" - {local['link']}" for
         idx, local
         in enumerate(locals)])
    return requests.post(
        f"{os.getenv('MAIL_GUN_API_BASE_URL')}/messages",
        auth=("api", os.getenv('MAIL_GUN_API_KEY')),
        data={"from": os.getenv("MAIL_SENDER"),
              "to": [os.getenv("MAIL_RECIPIENT")],
              "subject": subject,
              "text": content})
