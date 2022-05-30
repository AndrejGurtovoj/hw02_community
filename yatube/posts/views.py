from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User


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


def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = Post.objects.filter(author=user).count()
    context = {
        'page_obj': page_obj,
        'author': user,
        'count': count,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    text = post.text
    text_title = text[:30]
    pub_date = post.pub_date
    author = post.author
    name = author.get_full_name()
    count_posts = author.posts.all().count()
    group = post.group
    context = {
        'text': text,
        'pub_date': pub_date,
        'name': name,
        'count_posts': count_posts,
        'author': author,
        'group': group,
        'text_title': text_title,
    }
    return render(request, 'posts/post_detail.html', context)
