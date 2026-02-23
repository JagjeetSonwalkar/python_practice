from django.urls import path
from contact.views import contact_form, submit_contact

urlpatterns = [
    path('', contact_form, name = "contact" ),
    path("submit_contact/", submit_contact, name = "submit_contact")
]