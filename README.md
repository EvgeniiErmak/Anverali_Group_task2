## Anverali_Group_task2

Это пример структуры проекта Django для веб-приложения, представляющего собой платформу для регистрации как подрядчиков, так и клиентов.

### Описание

Проект содержит два основных приложения: `contractor` и `customer`, каждое из которых отвечает за регистрацию и профили соответствующих пользователей.

### Структура проекта

```
Anverali_Group_task2/
├── Anverali_Group_task2/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── contractor/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── customer/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── poetry.lock
├── project_structure.txt
├── pyproject.toml
└── templates/
    ├── base.html
    ├── contractor/
    │   ├── profile.html
    │   └── register.html
    ├── customer/
    │   ├── profile.html
    │   └── register.html
    └── home.html
```

### Использование

1. Убедитесь, что у вас установлен Python и Poetry.
2. Клонируйте репозиторий на свой локальный компьютер.
3. Перейдите в каталог проекта и установите зависимости с помощью Poetry:

```bash
poetry install
```

4. Создайте миграции и примените их:

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

5. Запустите сервер разработки:

```bash
poetry run python manage.py runserver
```

6. Откройте браузер и перейдите на [http://localhost:8000](http://localhost:8000), чтобы увидеть приложение в действии.

### Автор

Евгений Ермак  
Телефон: +7 930-290-99-80  
Telegram: [https://t.me/DJErmak3000](https://t.me/DJErmak3000)  
E-mail: [ew.ermak5000@mail.ru](mailto:ew.ermak5000@mail.ru)