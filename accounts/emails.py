from django.core.mail import send_mail
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import  urlsafe_base64_encode

def send_activation_email(user):
    subject = 'Activate your UrbanBoard account'
    uidb64 = urlsafe_base64_encode(force_bytes(user.id))
    activation_link = f"http://127.0.0.1:8000/activate/{uidb64}/"

    message = f"""
    Hello {user.username},

    Thank you for signing up on UrbanBoard.

    Please click the link below to activate your account:
    {activation_link}

    If you did not register, ignore this message.

    Regards,
    UrbanBoard Team
    """

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
