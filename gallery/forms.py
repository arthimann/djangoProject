from django import forms
from .models import CreateModel

class CreateForm(forms.ModelForm):
    file = forms.FileField(label='File to Upload')

    class Meta:
        model = CreateModel
        fields = ('file',)
