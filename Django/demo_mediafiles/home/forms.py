from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_resume(self):
        file = self.cleaned_data.get("resume")

        if file.size > 2*1024*1024 or not file.name.endswith(".pdf"):
            raise forms.ValidationError("file too large (MAX 2MB) or Only pdf allowed")

        return file