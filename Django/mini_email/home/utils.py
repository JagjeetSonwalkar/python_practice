from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_client():
    subject = "This email is from Django server"
    message = "This is a test messages from django sever email"
    from_email = settings.EMAIL_HOST_USER 
    recipient_list = ["sonwalkarshravani@gmail.com"]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)