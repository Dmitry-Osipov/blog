from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """
    Модель данных для постов блога. Посты будут иметь автора, заголовок, слаг, тело, статус публикации, а также время
    публикации, создания и обновления.
    """
    class Status(models.TextChoices):
        """
        Вложенный класс перечисления предназначен для обработки статуса постов: черновик и опубликованный пост.
        """
        DRAFT = ('DF', 'Draft')
        PUBLISHED = ('PB', 'Published')

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.
        """
        ordering = ('-publish', )
        indexes = (
            models.Index(fields=['-publish']),
        )

    def __str__(self):
        """
        Метод обеспечивает экземпляру класса корректное наименование.

        :return: Заголовок.
        """
        return self.title
