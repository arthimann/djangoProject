from django.shortcuts import render
from .forms import AddProductsForm


def add_view(request, *args, **kwargs):
    form = AddProductsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = AddProductsForm()

    return render(request, 'products/add.html', {
        'form': form
    })
