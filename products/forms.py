from django import forms
from .models import ProductModel
from categories.models import CategoryModel


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

    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_id = ModelChoiceField(
        queryset=CategoryModel.objects.all(),
        required=True,
        empty_label='-- Select --',
        to_field_name='id',
    )

    class Meta:
        model = ProductModel
        fields = ['title', 'description', 'price', 'category_id']


