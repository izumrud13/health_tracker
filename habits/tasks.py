import os
from datetime import datetime, date, timedelta

import requests
from celery import shared_task
from django.conf import settings

from habits.models import Habit


@shared_task
def send_message():
    """Отправка в телеграм напоминание о привычке"""

    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    time_now = datetime.now().time().replace(second=0)
    date_now = date.today()
    habits_send = Habit.objects.filter(is_pleasant_habit=False)

    for habit in habits_send:
        if habit.time > time_now:
            chat_id = habit.owner.telegram_id
            text = f'Вам нужно {habit.action} в {habit.time} в {habit.place}'
            requests.post(
                url=f"{URL}{TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": text
                }
            )
        habit.date = date_now + timedelta(days=habit.frequency)
        habit.save()
