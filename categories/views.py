from django.shortcuts import render
from django.http import HttpResponse
from categories.forms import CategoriesForm
from django.utils.decorators import decorator_from_middleware
from .Http.Middleware.add import AddCategoryMiddleware


# Create your views here.
def index_view(request, *args, **kwargs):
    return render(request, 'categories/list.html', {})


@decorator_from_middleware(AddCategoryMiddleware)
def add_view(request, *args, **kwargs):
    form = CategoriesForm()

    if request.method == 'POST':
        print("wtf", request.POST['title'], request.POST['description'])

    return render(request, 'categories/add.html', {
        'form': form,
    })

