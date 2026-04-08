from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request, "accounts_regular_form/contact.html", {"form": form})