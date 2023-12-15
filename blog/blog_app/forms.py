from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
    """
    Класс формы предназначен для отправки поста от одного пользователя к другому по электронной почте.
    """
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea, required=False)


class CommentForm(forms.ModelForm):
    """
    Класс формы предназначен для комментирования постов.
    """
    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных формы.
        """
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    """
    Форма помогает пользователю выполнять поиск постов.
    """
    query = forms.CharField()
