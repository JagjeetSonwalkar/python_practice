from django.urls import path
from .views import send_test_email, send_test_emailx, test_send_mass_mail

urlpatterns = [
    path('', send_test_email, name="send_test_email"),
    path("email-html/", send_test_emailx, name = "send_test_emailx"),
    path("bulk-email/", test_send_mass_mail, name = "bulk_email" )
]