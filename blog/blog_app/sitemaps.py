from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """
    Класс отвечает за формирование карты сайта.
    """
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        """
        Метод возвращает QuerySet объектов, которые включены в поиск.

        :return: QuerySet опубликованных постов.
        """
        return Post.published.all()

    def lastmod(self, obj):
        """
        Метод получает каждый объект, возвращаемый методом items(self) и возвращает время последнего изменения объекта.

        :param obj: Объект, возвращаемый методом items(self).
        :return: Время последнего изменения объекта.
        """
        return obj.updated
