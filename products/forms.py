from django import forms
from .models import Products
from categories.models import Categories


class ModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class AddProductsForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 5
        }))

    price = forms.IntegerField(max_value=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_id = ModelChoiceField(
        queryset=Categories.objects.all(),
        required=True,
        empty_label='-- Select --',
        to_field_name='id',
    )

    class Meta:
        model = Products
        fields = ['title', 'description', 'price', 'category_id']
