from django.urls import path
from student.views import student_create, students_list, student_details, student_update, student_delete

urlpatterns = [
    path('add/', student_create, name="student_create"),
    path("", students_list, name="student_list"),
    path("details/<int:id>/", student_details, name="student_details"),
    path("edit/<int:id>/", student_update, name = "student_edit"),
    path("delete/<int:id>/", student_delete, name="student_delete")
]
