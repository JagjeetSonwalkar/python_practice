from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_page(request):
    playing_11 = [
        {"name":"Rohit", "jersey_no":45},
        {"name":"Shumbham", "jersey_no":15},
        {"name":"Virat", "jersey_no":18},
        {"name":"Tilak", "jersey_no":49},
        {"name":"Surya", "jersey_no":35},
        {"name":"Hardik", "jersey_no":33},
        {"name":"Axar", "jersey_no":5},
        {"name":"Bumhra", "jersey_no":1},
        {"name":"Shami", "jersey_no":6},
        {"name":"Kulpeed", "jersey_no":3},
    ]

    squard = [
        {"name":"Rohit", "jersey_no":45},
        {"name":"Iyher", "jersey_no":49},
        {"name":"Shumbham", "jersey_no":15},
        {"name":"Virat", "jersey_no":18},
        {"name":"Tilak", "jersey_no":49},
        {"name":"Abhi", "jersey_no":None},
        {"name":"Surya", "jersey_no":35},
        {"name":"Hardik", "jersey_no":33},
        {"name":"Axar", "jersey_no":5},
        {"name":"Bumhra", "jersey_no":1},
        {"name":"Shami", "jersey_no":6},
        {"name":"kumar", "jersey_no":None},
        {"name":"Kulpeed", "jersey_no":3},
    ]

    return render(request, template_name="home/index.html", context = {"playing_11" : playing_11})

def squard_page(request):
    squard = [
        {"name":"Rohit", "jersey_no":45},
        {"name":"Iyher", "jersey_no":49},
        {"name":"Shumbham", "jersey_no":15},
        {"name":"Virat", "jersey_no":18},
        {"name":"Tilak", "jersey_no":49},
        {"name":"Abhi", "jersey_no":0},
        {"name":"Surya", "jersey_no":35},
        {"name":"Hardik", "jersey_no":33},
        {"name":"Axar", "jersey_no":5},
        {"name":"Bumhra", "jersey_no":1},
        {"name":"Shami", "jersey_no":6},
        {"name":"kumar", "jersey_no":0},
        {"name":"Kulpeed", "jersey_no":3},
    ]

    return render(request, template_name="home/squard.html", context={"squard" : squard})
