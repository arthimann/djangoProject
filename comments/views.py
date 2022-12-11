from django.shortcuts import render, redirect
from .forms import AddProductComment
from products.models import Product


def add_view(request, *args, **kwargs):
    form = AddProductComment(request.POST or None)
    form.instance.product_id = Product.objects.get(id=kwargs['product_id'])
    form.instance.author = request.user.id

    if form.is_valid():
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))
