from django.shortcuts import render

# Create your views here.
def home_page(request):
    name = "Jaggi"
    context = {"page":"home", "name":name}
    
    return render(request, 'home/index.html', context)