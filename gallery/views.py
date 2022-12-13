from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateForm
from .models import GalleryModel


def index_view(request):
    gallery_entities = GalleryModel.objects.all()
    return render(request, 'gallery/index.html', {
        'auth': request.user.is_authenticated,
        'gallery_entities': gallery_entities,
    })


@login_required(login_url='/members/')
def create_view(request):
    form = CreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))


    return render(request, 'gallery/store.html', {
        'form': form
    })


def store_view(request, *args, **kwargs):
    pass


def show_view(request, *args, **kwargs):
    pass


def destroy_view(request, *args, **kwargs):
    pass
