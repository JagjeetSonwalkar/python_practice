from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home_page(request):
    context = {
        "name" : "Mohit_Kumar",
        "age" : 25,
        "skills" : ["python", "Django", "React"],
        "user" : User("Kumar", 30),
        "blog" : {
            "title" : "Django Template",
            "content" : "<b>This blod</b>",
            "created_at" : datetime(2025, 8, 18, 10, 30)
        },
        "empty_value" : None,
    }

    return render(request, "bloggin/home.html", context)

def blog_details(request):
    post = {
        "title":"My second Templates Post",
        "describtion": "Djano is a high level pyton web framework",
        "author": None,
        "created_at": datetime(2025,8,19,10,30),
        "comments_count": 5,
        "tags": ["djagno", "web develpment", "python"],
        "number": 7,
        "price": 100,
    }

    return render(request, "bloggin/blog.html", {"post":post})

def blog_list(request):
    blogs = [
        {"title":"Django Basic", "is_featured":True, "author":"jaggi"},
        {"title":"Django Advance", "is_featured":False, "author":""},
        {"title":"Django REST API", "is_featured":False, "author":"jonny"},
    ]

    context = {
        "blogs":blogs,
        "today": datetime.now(),
        "html_code": "<h1>Welcome to Django</h1>",
    }

    return render(request, "bloggin/blog_list.html", context)