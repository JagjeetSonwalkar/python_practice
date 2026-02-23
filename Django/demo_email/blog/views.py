from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, EmailMessage, send_mass_mail, EmailAlternative
from django.template.loader import render_to_string

# send simple text email
def send_test_email(request):
    subject = "Welcome to my Blog"
    message = "Thankyou for following my blog"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["jagjeetsonwalkar0@gmail.com"]
    
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return HttpResponse("Test email sent successfully.")

# using html template
def send_test_emailx(request):
    subject = "Welcome to my Blog"
    message = render_to_string('email/welcome_email.html', {'username':"Jaggi", 'fav_game':"BGMI"})
    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        ["jagjeetsonwalkar0@gmail.com"],
    )
    email.content_subtype = "html" 
    email.send()
    return HttpResponse("test mail send successfully")

# send mass email
def test_send_mass_mail(request):
    message1 = (
        "Welcome to My Blog",                     # Subject
        "Thank you for following my blog.",      # Message
        settings.EMAIL_HOST_USER,                # From email
        ["shavanisonwalkar@gmail.com"],          # Recipient list
    )

    message2 = (
        "New Course Available",
        "Check out our new Django course.",
        settings.EMAIL_HOST_USER,
        ["jagjeetsonwalkar0@gmail.com"],
    )

    send_mass_mail((message1, message2), fail_silently=False)

    return HttpResponse("Mass emails sent successfully.")

def send_bulk_email_html(request):
    subject = "welcome to platform"
    from_email = "jagjeetsonwalkar0@gamil.com"
    recipient_list = ["shavanisonwalkar@gmail.com","jagjeetsonwalkar0@gmail.com"]

    html_content = render_to_string("welcome_email.html", {"username":"jack"})

    msg = EmailAlternative(subject, "Welcome to mu platform", from_email, recipient_list)
    # msg.attach_file('path/to/your/attachement.pdf')
    msg.attach_alternative(html_content, "text/html")

    msg.send()
    return HttpResponse("bulk emails sent successfully")