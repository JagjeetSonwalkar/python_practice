from django.shortcuts import render, get_object_or_404, redirect
from student.forms import StudentForm
from student.models import Student

# Create your views here.
def student_create(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "student/student_success.html")
    return render(request, "student/student_create.html", {"form":form})

def students_list(request):
    students = Student.objects.all()
    return render(request, "student/students_list.html", {'students':students})

def student_details(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "student/student_detail.html", {"student":student})

def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "student/student_create.html", {'form':form})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    
    return render(request, "student/student_confirm_delete.html", {"student":student})
