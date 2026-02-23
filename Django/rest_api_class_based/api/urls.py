# from django.urls import path
# from .views import StudentAPI
# from .views import StudentListCreateAPI, StudentRetriveUpdateDeleteAPI

# urlpatterns = [
#     path('students/', StudentListCreateAPI.as_view()), # for get(all), post
#     path('students/<int:pk>/', StudentRetriveUpdateDeleteAPI.as_view()) # for get(single), put, delete
# ]

# urlpatterns = [
#     path('students/', StudentAPI.as_view()), # for get(all), post
#     path('students/<int:student_id>/', StudentAPI.as_view()) # for get(single), put, delete
# ]

from .views import StudentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentViewSet, basename = 'student')

urlpatterns = [
    path('', include(router.urls))
]