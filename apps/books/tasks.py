from celery import shared_task
import requests


@shared_task
def send_telegram_message(message):
    requests.get(f"https://api.telegram.org/bot7469961928:AAFplfnwrUuojjnjOaw0Cop1eCz1cUtTmkM/sendMessage?text={message}&chat_id=1921103181")
