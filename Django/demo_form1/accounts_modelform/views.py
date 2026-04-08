from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogForm

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)   # ONLY request.POST
        if form.is_valid():
            form.save()
            return HttpResponse("Posted")
    else:
        form = BlogForm()   # EMPTY form

    return render(request, "accounts_modelform/blog.html", {"form": form})