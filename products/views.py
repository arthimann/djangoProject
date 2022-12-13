from django.shortcuts import render
from .forms import AddProductsForm
from .models import ProductModel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from comments.forms import StoreCommentForm


def index_view(request, *args, **kwargs):
    product_entities = ProductModel.objects.all()

    return render(request, 'products/index.html', {
        'product_entities': product_entities,
    })


def show_view(request, *args, **kwargs):
    product_entities = ProductModel.objects.get(id=kwargs['product_id'])
    comment_form = StoreCommentForm(None)

    return render(request, 'products/show.html', {
        'product_entities': product_entities,
        'form': comment_form,
        'back_url': f"{request.scheme}://{request.get_host()}/products",
        'store_url': f"{request.scheme}://{request.get_host()}/comments/{kwargs['product_id']}/store/",
    })


@login_required(login_url='/members/')
def store_view(request, *args, **kwargs):
    form = AddProductsForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = AddProductsForm()

    return render(request, 'products/store.html', {
        'form': form
    })


@login_required(login_url='/members/')
def edit_view(request, *args, **kwargs):
    form_entity = ProductModel.objects.get(id=kwargs['product_id'])
    form = AddProductsForm(request.POST or None, instance=form_entity)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(f"/products/{kwargs['product_id']}/")

    return render(request, 'products/edit.html', {
        'form': form,
        'edit': True,
    })
