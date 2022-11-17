from django import forms
from .models import Categories


class CategoriesForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.TextInput(attrs={'class': 'form-control'})

    class Meta:
        model = Categories
        fields = ['title', 'description']
