from django.shortcuts import render
from .third_party import PostApi


def index_view(request, *args, **kwargs):
    posts = PostApi.get_posts()
    return render(request, 'posts/index.html', {
        'posts': posts
    })
