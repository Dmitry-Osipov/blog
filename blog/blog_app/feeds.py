import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import  truncatewords_html
from django.urls import reverse_lazy

from .models import Post


class LatestPostsFeed(Feed):
    """
    Класс отвечает за формирование новостной ленты.
    """
    title = 'My blog'
    link = reverse_lazy('blog_app:post_list')
    description = 'New posts of my blog'

    def items(self):
        """
        Метод возвращает первые 5 опубликованных записей в коллекции QuerySet.

        :return: QuerySet со срезом в первые 5 элементов.
        """
        return Post.published.all()[:5]

    def item_title(self, item):
        """
        Метод возвращает заголовок каждого поста.

        :param item: Пост.
        :return: Заголовок поста.
        """
        return item.title

    def item_description(self, item):
        """
        Метод возвращает отформатированный обрезанный пост.

        :param item: Пост.
        :return: Описание поста в виде тела поста обрезанное в 30 слов.
        """
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        """
        Метод возвращает время последнего обновления поста.

        :param item: Пост.
        :return: Время обновления поста.
        """
        return item.publish
