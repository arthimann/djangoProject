from django.shortcuts import render
from categories.forms import CategoriesForm
from django.utils.decorators import decorator_from_middleware
from categories.middleware.add import AddCategoryMiddleware
from django.http import HttpResponse, HttpResponseRedirect
from categories.models import Categories


# Create your views here.
def index_view(request, *args, **kwargs):
    category_entities = Categories.objects.all()
    return render(request, 'categories/list.html', {
        'category_entities': category_entities
    })


# @decorator_from_middleware(AddCategoryMiddleware)
def add_view(request, *args, **kwargs):
    form = CategoriesForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = CategoriesForm()

    return render(request, 'categories/add.html', {
        'form': form,
    })
