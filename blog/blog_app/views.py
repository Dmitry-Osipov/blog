from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_POST

from .forms import *
from .models import *

# Create your views here.
class PostListView(ListView):
    """
    Класс представления служит для отображения списка постов с реализованной пагинацией.
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_app/post/list.html'


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
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(request, 'blog_app/post/detail.html',
                  context={'post': post, 'comments': comments, 'form': form})


def post_share(request, post_id):
    """
    Функция представления служит для отображения страницы отправки поста.

    :param request: Запрос клиента.
    :param post_id: ID поста.
    :return: HTML-файл отправки поста.
    :raises Http404: Ошибка 404, если пост не был найден по указанному id.
    """
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, 'dimaosipov00@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog_app/post/share.html', context={'post': post, 'form': form, 'sent': sent})


@require_POST  # Декоратор разрешает только обращение по POST, обращение к странице по другому методу выдаст ошибку 405.
def post_comment(request, post_id):
    """
    Функция представления предназначена для отображения страницы добавления комментария.

    :param request: Запрос клиента.
    :param post_id: ID поста.
    :return: HTML-страница добавления комментария.
    :raises Http404: Ошибка 404, если пост не был найден по данному id.
    """
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(request, 'blog_app/post/comment.html',
                  context={'post': post, 'form': form, 'comment': comment})
