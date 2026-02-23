from django.shortcuts import render,redirect
from .utils import send_mail_to_client

# Create your views here.
def home_page(request):
    return render(request, "home/index.html")

def send_email(request):
    send_mail_to_client()
    return redirect('/')