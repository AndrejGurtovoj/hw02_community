# backend_community_homework
Yatube - это социальная сеть с авторизацией, персональными лентами, комментариями и подписками на авторов статей.

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)

## Функционал
- Создано и зарегистрировано приложение Posts;
- Подключена база данных;
- Десять последних записей выводятся на главную страницу;
- В админ-зоне доступно управление объектами модели Post. Можно публиковать новые записи, редактировать и удалять существующие;
- Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndrejGurtovoj/hw02_community.git
```

Cоздать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустить проект:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```
