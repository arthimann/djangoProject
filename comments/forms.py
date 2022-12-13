from django import forms
from .models import CommentModel


class StoreCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 5
        }))

    class Meta:
        model = CommentModel
        fields = ('comment',)
