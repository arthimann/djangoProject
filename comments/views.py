from django.shortcuts import render, redirect
from .forms import StoreCommentForm
from products.models import ProductModel


def store_view(request, *args, **kwargs):
    form = StoreCommentForm(request.POST or None)
    form.instance.product_id = ProductModel.objects.get(id=kwargs['product_id'])
    form.instance.author = request.user.id

    if form.is_valid():
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))
