from django.shortcuts import render

# Create your views here.
def index_page(request):
    context={"page":"home"}
    return render(request, "home/index.html")