# Куда пойти — Москва глазами Туриста
Сайт о самых интересных местах в Москве

[Ссылка на сайт](https://fergoth.pythonanywhere.com/)

[Ссылка на админку](https://fergoth.pythonanywhere.com/admin)
## Запуск
Для запуска понадобится Python версии 3.10
* Скачайте код
* Установите зависимости из requirements.txt
```sh
pip install -r requirements.txt
```
* Примените миграции
```bash
python manage.py migrate
```
* Создайте суперпользователя для админки
```bash
python manage.py createsuperuser
```
* Запустите локально сайт и откройте ссылку 
```bash
python manage.py runserver
```
* Админка доступна по адресу /admin
## Наполнение данных
! Важен порядок каритнок, первая главная, остальные в карусели
Менять порядок можно перетаскивая картинки
* Добавить данные через Админку
* Или добавить данные через скрипт 
```
python manage.py load_place URL
```
Где по ссылке ожидается json в следующем формате:
```json
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```
## Переменные окружения 
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 4 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `DATABASE_FILEPATH` — полный путь к файлу базы данных SQLite, например: `/home/user/where_to_go.sqlite3`
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Цели
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с [репозитория](https://github.com/devmanorg/where-to-go-places)

