from django import forms
from .models import GalleryModel

class CreateForm(forms.ModelForm):
    file = forms.FileField(label='File to Upload')

    class Meta:
        model = GalleryModel
        fields = ('file',)
