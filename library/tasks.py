from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import requests



@shared_task
def email_notification(email, subject, message):
    """Отправка уведомлений о выдачи/сдачи книги по электронной почте.
    Принимает адрес почты, тему и сообщение.
    """
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
@shared_task()
def telegram_notification(message, chat_id):
    """Отправка уведомлений о выдачи/сдачи книги через телеграм-бот.
    Принимает текст сообщения и id чата, отправляет его."""
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/sendMessage", params=params
    )