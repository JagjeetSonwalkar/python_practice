from django import forms
from .models import Blogx

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogx
        fields = "__all__"