from django.shortcuts import render
from telegram import Update
import json
from tg_dispatcher import bot, dispatcher
from django.http import JsonResponse


def message_handler(request):
    update = Update.de_json(json.loads(request.body), bot)
    dispatcher.process_update(update)
    return JsonResponse({"ok": True})