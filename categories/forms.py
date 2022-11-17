from django import forms
from .models import Categories


class CategoriesForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 10
        }))

    class Meta:
        model = Categories
        fields = ['title', 'description']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if 'asd' not in title:
            raise forms.ValidationError('wtf dude!?')

        return title
