from django import forms
from .models import Comment


class AddProductComment(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 5
        }))
    product_id = forms.CharField(widget=forms.HiddenInput(), initial='1')

    class Meta:
        model = Comment
        fields = [
            'comment',
            'product_id',
        ]


