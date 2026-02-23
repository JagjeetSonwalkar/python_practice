from django.shortcuts import render, redirect
from .forms import StudentForm

# Create your views here.
def student_form(request):
    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = StudentForm()
        
    return render(request, "home/student_form.html", context={"page":"student_form", "form":form})

def success_page(request):
    return render(request, "home/success.html", context={"page":"success"})