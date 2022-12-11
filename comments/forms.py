from django import forms
from .models import Comment


class AddProductComment(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 5
        }))

    class Meta:
        model = Comment
        fields = ('comment',)
