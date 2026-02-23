from django.urls import path
from todo_app.views import task_list, task_create, task_update, task_delete, task_toggle_complete 

name = "todo_app"

urlpatterns = [
    path('', task_list, name="task_list"),
    path("add/", task_create, name="task_create"),
    path("edit/<int:pk>/", task_update, name="task_update"),
    path("delete/<int:pk>/",task_delete, name="task_delete"),
    path("toggle/<int:pk>/", task_toggle_complete, name="task_toggle"),
]