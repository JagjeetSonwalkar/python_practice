from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

class UsernameOrEmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            # Check if input is email
            if "@" in username:
                try:
                    user_obj = User.objects.get(email=username)
                    username = user_obj.username
                except User.DoesNotExist:
                    raise forms.ValidationError("Invalid email or username.")

            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )

            if self.user_cache is None:
                raise forms.ValidationError("Invalid credentials.")
        return self.cleaned_data