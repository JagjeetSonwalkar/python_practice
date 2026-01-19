from django.shortcuts import render, redirect
from .models import *

# Create your views here.
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

    return render(
        request, "recipe/recipe.html", 
        context={"page":"recipe", "recipes" : query_set}
    )

def recipe_delete(request, id):
    query_set = Recipe.objects.get(id = id)
    query_set.delete()
    return redirect('/recipe/')