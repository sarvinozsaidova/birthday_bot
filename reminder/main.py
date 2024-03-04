import logging
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from datetime import datetime

from reminder.models import Employee


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


TOKEN = '6552144687:AAFOyaUfeP_JFGqDdg_bAeEv5Q5zPePu1hA'

def send_birthday_reminder(context):
    today = datetime.now().date()
    employees = Employee.objects.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)

    for employee in employees:
        message = f"🎉 Happy Birthday! 🎉\n\n" \
                  f"Name: {employee.name} {employee.surname}\n" \
                  f"Date of Birth: {employee.date_of_birth.strftime('%B %d, %Y')}\n" \
                  f"Picture: {employee.picture.url}"

        bot = context.bot
        bot.send_message(chat_id=employee.telegram_chat_id, text=message)

def start_reminder_bot():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    job_queue = updater.job_queue
    job_queue.run_daily(send_birthday_reminder, time=datetime.time(hour=8))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    start_reminder_bot()