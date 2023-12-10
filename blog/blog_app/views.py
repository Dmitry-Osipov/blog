from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def post_list(request):
    """
    Функция представления отвечает за отображение всех постов.

    :param request: Запрос клиента.
    :return: HTML-страница со всеми опубликованными постами.
    """
    posts = Post.published.all()
    return render(request, 'blog_app/post/list.html', context={'posts': posts})


def post_detail(request, id):
    """
    Функция представления отвечает за отображение конкретного поста.

    :param request: Запрос клиента.
    :param id: ID записи.
    :return: HTML-страница опубликованного поста.
    :raises Http404: Ошибка 404, если нет опубликованного поста с переданным id.
    """
    post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)

    return render(request, 'blog_app/post/detail.html', context={'post': post})
