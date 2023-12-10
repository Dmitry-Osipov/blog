# Приложение ведения блога с использованием Python 3.11 и Django 4.1.13.
## Описание и технологии проекта
- Сайт реализовывает личный блог.
- Реализована система отправки интересующих постов по E-mail.
- Реализована система комментариев под постом.
- Сайт имеет приятный интерфейс и интуитивное взаимодействие.
## Структура папок
blog - sources root:
- blog - пакет конфигурации:
    - __init__.py - файл указывает питону, что данная директория является пакетом;
    - asgi.py - это точка входа для веб-серверов, которые поддерживают ASGI (Asynchronous Server Gateway Interface);
    - settings.py - файл настроек сайта;
    - urls.py - файл для хранения всех перенаправлений клиента;
    - wsgi.py -  это точка входа для веб-серверов, которые поддерживают WSGI (Web Server Gateway Interface).
- blog_app - пакет основного приложения:
    - migrations - пакет служит для хранения миграций БД;
    - static - папка со статикой для приложения blog_app:
        - css - папка для стилей оформления.
    - templates - директория с шаблонами текущего приложения:
        - blog_app - директория служит для избежания коллизий с другими приложениями: 
            - post - директория хранения шаблонов, принадлежащих приложению blog_app: 
                - includes - папка для устранения дублирования кода в HTML-файлах:
                    - comment_form.html - шаблон добавления комментария; 
                    - pagination.html - шаблон реализации пагинации.
                - comment.html - шаблон отображения комментариев;
                - detail.html - шаблон отображения конкретного поста;
                - list.html - шаблон отображения всех постов;
                - share.html - шаблон отображения поста на отправку по E-mail. 
            - base.html - базовый шаблон.
    - __init__.py - файл указывает питону, что данная директория является пакетом;
    - admin.py – файл для настройки админ-панели сайта (админ-панель поставляется совместно с Django и каждый сайт может сразу ее использовать);
    - apps.py – файл для настройки (конфигурирования) текущего приложения;
    - forms.py - файл для классов формы;
    - models.py – файл для хранения ORM-моделей для представления данных из базы данных;
    - tests.py – модуль с тестирующими процедурами;
    - urls.py - файл для хранения всех перенаправлений клиента;
    - views.py – файл для хранения представлений (контроллеров) текущего приложения. 
- db.sqlite3 - база данных сайта;
- manage.py - файл, который передаёт команды django-admin и выполняет их "от лица" сайта.

.gitignore - файл запретов для системы контроля версий;
