from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, min_length=4, required=True)
    last_name = forms.CharField(max_length=15, min_length=4, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
    
    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Used!")
        return email

class CustomAuthencticationForm(AuthenticationForm):
    username = forms.CharField(label="Username or email")

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if username and password:
            if "@" in username:
                try:
                    user_obj = User.objects.get(email=username)
                    username = user_obj
                except User.DoesNotExist:
                    raise forms.ValidationError("Invalid email or Username")
            
            self.user_cache = authenticate(
                self.request,
                username = username,
                password = password
            )

            if self.user_cache is None:
                raise forms.ValidationError("invalid creddentails")
        return self.cleaned_data