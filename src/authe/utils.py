from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings

def send_verified_link(message, email):
    send_mail(
        'Email verified',
        message,
        settings.EMAIL_FROM,
        [email,]
    )

def send_reset_link(message, email):
    send_mail(
        'Password reset',
        message,
        settings.EMAIL_FROM,
        [email,]
    )