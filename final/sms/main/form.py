from django import forms
from .models import Student,Mark

class MarkForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    subject = forms.CharField(max_length=50)
    mark = forms.IntegerField()

    def save(self):
        mark = Mark(
            student=self.cleaned_data['student'],
            subject=self.cleaned_data['subject'],
            mark=self.cleaned_data['mark']
        )
        mark.save()
