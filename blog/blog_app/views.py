from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.
def post_list(request):
    """
    Функция представления отвечает за отображение всех постов.

    :param request: Запрос клиента.
    :return: HTML-страница со всеми опубликованными постами.
    """
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)  # По умолчанию берём первую страницу.
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'blog_app/post/list.html', context={'posts': posts})


def post_detail(request, year, month, day, post):
    """
    Функция представления отвечает за отображение конкретного поста.

    :param request: Запрос клиента.
    :param id: ID записи.
    :return: HTML-страница опубликованного поста.
    :raises Http404: Ошибка 404, если нет опубликованного поста с переданным id.
    """
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(request, 'blog_app/post/detail.html', context={'post': post})
