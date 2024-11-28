from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail

from config import settings
from config.settings import EMAIL_HOST_USER
from users.models import User
from records.models import Entry


def send_message():
    """Раз в день отправляет сообщения о дедлайне"""

    current_date = datetime.now().date()

    for user in User.objects.all():
        for entry in Entry.objects.filter(user=user):

            if entry.end_time and entry.status is not 'PAST':
                deadline = entry.end_time.date() - current_date
                if entry.end_time.date() == current_date:
                    subject = 'Сегодня дедлайн!'
                    message = f'Cегодня дедлайн по цели "{entry.title}"!'
                    send_mail(
                        subject=subject,
                        message=message,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[entry.user.email],
                    )
                    print(f'На почту{entry.user} отправлено письмо')
                elif deadline == timedelta(days=3):
                    subject = 'Скоро дедлайн!'
                    message = f'Через 3 дня дедлайн по цели "{entry.title}"!'
                    send_mail(
                        subject=subject,
                        message=message,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[entry.user.email],
                    )
                    print(f'На почту{entry.user} отправлено письмо')


def start_sheduler():
    scheduler = BackgroundScheduler()
    if not scheduler.get_jobs():
        scheduler.add_job(send_message, 'interval', seconds=10)
    if not scheduler.running:
        scheduler.start()
