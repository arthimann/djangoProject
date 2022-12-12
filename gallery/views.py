from django.shortcuts import render, redirect
from .forms import CreateForm
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, 'gallery/index.html', {
        'auth': request.user.is_authenticated,
    })


@login_required(login_url='/members/')
def create_view(request):
    form = CreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))


    return render(request, 'gallery/create.html', {
        'form': form
    })


def store_view(request, *args, **kwargs):
    pass


def show_view(request, *args, **kwargs):
    pass


def destroy_view(request, *args, **kwargs):
    pass
