from django.shortcuts import render, get_object_or_404

from .models import Post, Group

NUMBER_OF_POSTS: int = 10


def index(request):
    posts = Post.objects.all()[:NUMBER_OF_POSTS]
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте',
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:NUMBER_OF_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
