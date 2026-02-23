from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")

def blog(request):
    students_list = [
        {"name":"Mohit", "class":"10th"},
        {"name":"Rohit", "class":"09th"},
        {"name":"Sohit", "class":"08th"},
    ]
    return render(request, "blog/blog.html", context={"students_list":students_list})