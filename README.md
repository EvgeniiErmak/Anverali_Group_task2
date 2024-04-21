# Anverali_Group_task2

Это второй проект в рамках задачи для Anverali Group. Проект представляет собой веб-приложение для регистрации пользователей в двух категориях: заказчиков (Customers) и подрядчиков (Contractors).

## Структура проекта

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

## Инструкции по установке и запуску

1. Убедитесь, что у вас установлен Python версии 3.x и установлен Poetry.

2. Склонируйте репозиторий:

```
git clone https://github.com/DJErmak3000/Anverali_Group_task2.git
```

3. Перейдите в директорию проекта:

```
cd Anverali_Group_task2
```

4. Установите зависимости:

```
poetry install
```

5. Примените миграции:

```
poetry run python manage.py migrate
```

6. Запустите сервер:

```
poetry run python manage.py runserver
```

7. Откройте браузер и перейдите по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/) для доступа к приложению.

## Контакты автора

Автор: Евгений Ермак
Телефон: +7 930-290-99-80
Telegram: [@DJErmak3000](https://t.me/DJErmak3000)
Email: [ew.ermak5000@mail.ru](mailto:ew.ermak5000@mail.ru)
