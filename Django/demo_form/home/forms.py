from django import forms
from .models import Student

'''
class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    email = forms.EmailField()

    # Field validation
    def clean_age(self):
        age = self.cleaned_data.get("age")

        if age is not None and age < 18:
            raise forms.ValidationError("Age must be 18 or above")

        return age

    # Form validation
    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        age = cleaned_data.get("age")
        email = cleaned_data.get("email")

        if first_name and last_name and email:
            if first_name + last_name == email:
                raise forms.ValidationError("Name and Email cannot be same")

        

        return cleaned_data
'''

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student # which model?
        fields = "__all__"  # for Specific: Fields ['name', 'email'], for Excluding Fields: exclude = ['address']

        widgets = {
            "first_name" : forms.TextInput(
                attrs={
                    'class': "form-control",
                    "placeholder": "Enter first_name"
                }
            ),

            "last_name" : forms.TextInput(
                attrs={
                    'class': "form-control",
                    "placeholder": "Enter last_name"
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Age'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Email'
                }
            ),

        }