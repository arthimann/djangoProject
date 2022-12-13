from django.shortcuts import render
from categories.forms import StoreCategoryForm
from django.utils.decorators import decorator_from_middleware
from categories.middleware.add import AddCategoryMiddleware
from categories.models import CategoryModel
from django.contrib.auth.decorators import login_required


def index_view(request, *args, **kwargs):
    category_entities = CategoryModel.objects.all()
    return render(request, 'categories/index.html', {
        'category_entities': category_entities
    })


# @decorator_from_middleware(AddCategoryMiddleware)
@login_required(login_url='/members/')
def store_view(request, *args, **kwargs):
    form = StoreCategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = StoreCategoryForm()

    return render(request, 'categories/store.html', {
        'form': form,
    })
