# Куда пойти — Москва глазами Артёма

Личный блог, показывающий интересные места на карте.

## Описание

Сайт, показывающий интересные места на карте, с описанием этих мест и фотографиями. Данный сайт вы можете посмотреть по [ссылке](http://moscowplace.pythonanywhere.com). Чтобы посмотреть описание места, необходимо нажать на красную мерцающую точку.

![screenshot](screenshots/screenshot.jpg)

Сайт оптимизирован для просмотра на различных устройствах.

![mobile](screenshots/mob_screenshot.jpg)

Наполнение сайта происзодит через специальную [панель администратора](http://moscowplace.pythonanywhere.com/admin/).

![admin](screenshots/admin_screenshot.jpg)

## Как запустить на локальном компьютере

Скачайте код. Создайте файл с переменными окружения `.env` и положите его рядом с `manage.py`. Доступны 3 переменные окружения: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`.

Скрипт адаптирован под Python ver 3.8.1

Используйте `pip` для установки зависимостей:

```bash
pip install -r requirements.txt
```

Запустите веб-сервер командой:

```bash
python manage.py migrate
python manage.py runserver 8080
```

## Заполнение базы данных

В данном проекте был разразбортан скрипт по заполнению базы данных. Все данные необходимо оформлять в виде ссылки на [json файл](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json). Скрипт автоматически загружает данные и фотографии.

Запуск скрипта осуществляется из командной строки:

```bash
python manage.py load_place ссылка
```

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).