import textwrap
from datetime import datetime, timedelta

import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from library.models import Book
from library.services import send_email_message, send_telegram_message


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


@shared_task()
def send_reminder():
    """Отправляет уведомление о необходимости сдачи книги в срок.
    Напоминает за 5 дней досрока и в день окончания срока."""
    today = datetime.now().date()
    books = Book.objects.filter(issue=True)
    for book in books:
        # напоминание об окончании срока чтения книги в текущий день
        if book.return_date == today:
            email = book.reader.email
            title = book.title
            authors = ", ".join([str(author) for author in book.author.all()])
            message = textwrap.dedent(
                f"""\
            Здравствуйте!
            Напоминаем Вам, что сегодня истекает срок выдачи книги "{title}" автора {authors}.
            С Уважением, администрация библиотеки!
            """
            )
            subject = "Необходимость сдачи книги"
            send_email_message(email=email, subject=subject, message=message)
            if book.reader.tg_id:
                send_telegram_message(message=message, chat_id=book.reader.tg_id)
        # напоминание об окончании срока чтения книги через 5 дней
        if today + timedelta(days=5) == book.return_date:
            email = book.reader.email
            title = book.title
            authors = ", ".join([str(author) for author in book.author.all()])
            message = textwrap.dedent(
                f"""\
            Здравствуйте!
            Напоминаем Вам, через 5 дней истекает срок выдачи книги "{title}" автора {authors}.
            С Уважением, администрация библиотеки!
            """
            )
            subject = "Необходимость сдачи книги"
            send_email_message(email=email, subject=subject, message=message)
            if book.reader.tg_id:
                send_telegram_message(message=message, chat_id=book.reader.tg_id)
