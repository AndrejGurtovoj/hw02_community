from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    templates = 'posts/index.html'
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = 'Это главная страница проекта Yatube'
    context = {
        'page_obj': page_obj,
        'title': title
    }
    return render(request, templates, context)


def group_posts(request, slug):
    templates = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    text = 'Записи сообщества'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'text': text
    }
    return render(request, templates, context)
