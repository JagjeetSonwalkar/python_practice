from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show_msg(request):
    messages.debug(request, "This is a debug message.")
    return render(request, "msg/show_msg.html")
