from django import forms
from student.models import Student

# Django Model-Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "email"]
    
    # validation
    def clean_age(self):
        age = self.cleaned_data.get("age")

        if age < 18:
            raise forms.ValidationError("Age must me atleast 18!")

        return age

