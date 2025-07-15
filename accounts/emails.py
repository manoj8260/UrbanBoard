from django.core.mail import send_mail
from django.conf import settings

def send_activation_email(user):
    subject = 'Activate your UrbanBoard account'
    activation_link = f"http://127.0.0.1:8000/accounts/activate/{user.id}/"

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
