from django.shortcuts import render, redirect
from .forms import AddProductComment
from .models import Comment


def add_view(request, *args, **kwargs):
    request.POST.author = request.user.id
    form = AddProductComment(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(request.path_info)

