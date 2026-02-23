from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@login_required(login_url='/login/')
def recipe_page(request):
    # get the data
    if request.method == "POST":
        data = request.POST 

        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")    
        
        # save the data - firt import the model
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
            ) 

        return redirect('/recipe/')

    # view the data on front_end
    query_set = Recipe.objects.all()   

    # search the data
    if request.GET.get('search'):
        query_set = query_set.filter(recipe_name__icontains = request.GET.get('search')) 

    return render(
        request, "recipe/recipe.html", 
        context={"page":"recipe", "recipes" : query_set}
    )

@login_required
def recipe_update(request, id):
    query_set = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        query_set.recipe_name = recipe_name
        query_set.recipe_description = recipe_description
        if recipe_image:
            query_set.recipe_image = recipe_image
        
        query_set.save()
        return redirect("/recipe/")

    return render(request, 
    "recipe/update_recipe.html",
    context = {"page":"recipe update", "recipe":query_set}
    )

@login_required
def recipe_delete(request, id):
    # delete a record
    query_set = Recipe.objects.get(id = id)
    query_set.delete()
    return redirect('/recipe/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "invalid username!")
            return redirect("/login/")

        # authenticate is method which return the bool value by check the username exists or not
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.error(request, "Invalid Password!!")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/recipe/")

    return render(request, "recipe/login.html", context={"page":"login"})

def logout_page(request):
    logout(request)
    return redirect("/login/")

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already exists")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created succesfully.")
        return redirect("/register/")

    return render(request, "recipe/register.html", context={"page":"register"})
