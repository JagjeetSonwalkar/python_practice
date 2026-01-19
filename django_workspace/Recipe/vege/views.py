from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def recipe_page(request):
    if request.method == "POST":
        data = request.POST 
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_img = request.FILES.get('recipe_img')

        print(recipe_name)
        print(recipe_description)
        print(recipe_img)
    
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_img = recipe_img,
            )
        
        return redirect('/recipe/')
    
    query_set = Recipe.objects.all()  

    if request.GET.get('search'):
        query_set = query_set.filter(recipe_name__icontains = request.GET.get('search'))
    

    context = {"recipes": query_set}

    return render(request, "recipe_temp/recipe.html", context = {"page":"recipes"})

def recipe_delete(request, id):
    query_set = Recipe.objects.get(id = id)
    query_set.delete()
    return redirect('/recipe/')

def recipe_update(request, id):
    query_set = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        query_set.recipe_name = recipe_name
        query_set.recipe_description = recipe_description

        if recipe_image:
            query_set.recipe_img = recipe_image

        query_set.save()

        return redirect('/recipe')

    context = {'recipe':query_set}

    return render(request, "recipe_temp/recipe_update.html", context = {'page':"recipe_update"})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipe')

    return render(request, "recipe_temp/login.html", context={'page':"login"})

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken!')
            return redirect("/register/")

        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
                        )

        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully")

        return redirect('/login/')

    return render(request, "recipe_temp/register.html", context = {"page":"register"})