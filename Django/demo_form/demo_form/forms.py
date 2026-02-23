from django import forms

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    