from django import forms
from .models import Category


class CategoriesForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 10
        }))

    class Meta:
        model = Category
        fields = ['title', 'description']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        return title
