from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, ConversationHandler, Filters
from django.contrib.auth import get_user_model
import random
from datetime import datetime, timedelta
from apps.users.models import OneTimeCode
from rest_framework.exceptions import ValidationError


User = get_user_model()

import os
from dotenv import load_dotenv


def start(update, context):
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    telegram_id = update.message.from_user.id

    User.objects.update_or_create(
        username=telegram_id,
        defaults={
            "first_name":first_name,
            "last_name":last_name
        }
    )

    one_time_code = random.randint(100000, 999999)
    expire_time = datetime.now() - timedelta(seconds=60)
    otps = OneTimeCode.objects.filter(phone_number=telegram_id, created_at__gte=expire_time)

    if otps.exists():
        update.message.reply_text(f"OTP: {otps.first().code}")

    else:
        update.message.reply_text(f"OTP: {one_time_code}")
        OneTimeCode.objects.create(code=one_time_code, phone_number=telegram_id)


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

dispatcher = Dispatcher(bot, None, workers=0)

dispatcher.add_handler(CommandHandler("start", start))

