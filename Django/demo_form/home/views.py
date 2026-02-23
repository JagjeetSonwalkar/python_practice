from django.shortcuts import render, redirect
from .forms import StudentForm

# Create your views here.
def student_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
    else:
        form = StudentForm()

    return render(request, "home/student_form.html", context={"page":"student_form","form":form})

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()                     # save to database
            return redirect("success")
    else:
        form = StudentForm()
    
    return render(request, "home/student_form.html", context={"page":"student_form", "form":form})

def success_page(request):
    return render(request, "home/success.html", context={"page":"success"})