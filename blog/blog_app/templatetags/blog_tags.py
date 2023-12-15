import markdown
from django import template
from django.utils.safestring import mark_safe
from django.db.models import Count

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    """
    Метод подсчитывает общее количество постов.

    :return: Общее количество постов.
    """
    return Post.published.count()


@register.inclusion_tag('blog_app/post/latest_posts.html')
def show_latest_posts(count=5):
    """
    Метод возвращает последние опубликованные посты.

    :param count: Количество постов, которые требуется вернуть. По умолчанию 5.
    :return: Словарь, ключ - 'latest_posts', значение - QuerySet последних опубликованных постов.
    """
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    """
    Метод возвращает самые посты с наибольшим количеством комментариев.

    :param count: Количество постов, которые требуется вернуть. По умолчанию 5.
    :return: Упорядоченный QuerySet постов.
    """
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    """
    Метод позволяет писать посты в формате markdown.

    :param text: Текст.
    :return: Неэкранированные строки текста.
    """
    return mark_safe(markdown.markdown(text))
