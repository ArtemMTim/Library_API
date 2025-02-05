import requests
from django.core.mail import send_mail

from config import settings


def send_telegram_message(message, chat_id):
    """Функция отправки сообщений через телеграм-бот.
    Принимает текст сообщения и id чата, отправляет его."""
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/sendMessage", params=params
    )


def send_email_message(email, subject, message):
    """Отправка уведомлений по электронной почте.
    Принимает адрес почты, тему и сообщение.
    """
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
