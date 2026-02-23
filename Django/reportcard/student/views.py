from django.shortcuts import render
from .models import *

from django.core.paginator import Paginator
from django.db.models import Q, Sum

# Create your views here.
def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get("search"):
        search = request.GET.get("search")
        # queryset = queryset.filter(student_name__icontains = search)
        queryset = queryset.filter(
            Q(student_name__icontains = search) | 
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search)
            )

    paginator = Paginator(queryset, 20)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {"Page":"students", 
    # "queryset":queryset,
    "queryset":page_obj,
    }

    return render(request, "student/student_reportcard.html", context)

def see_marks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id).select_related("subject")
    total = queryset.aggregate(totalmarks = Sum("marks"))

    context = {"Page":"student", "queryset":queryset, "student_id":student_id, "total":total}
    return render(request, "student/see_marks.html", context)