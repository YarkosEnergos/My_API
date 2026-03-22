# My_API

REST API, реализованный на базе Django и Django REST Framework.
API позволяет создавать посты, получать список групп, добавлять комментарии и управлять контентом с учетом прав доступа.

---

## Описание проекта

 My_API  предоставляет программный интерфейс для взаимодействия с социальной сетью.
С его помощью можно:

* получать список постов
* создавать новые посты
* редактировать и удалять свои посты
* просматривать группы
* добавлять комментарии к постам
* получать комментарии конкретного поста
* работать с API через Token Authentication

Проект реализует разграничение прав доступа: изменять и удалять контент может только его автор.

---

## Технологии

Проект использует следующий стек:

* Python 3.10+
* Django
* Django REST Framework
* SQLite
* Token Authentication (DRF)
* ORM Django

---

## Установка и запуск проекта

### 1. Клонировать репозиторий

```bash
git clone https://github.com/YarkosEnergos/My_API.git
cd api_yatube/yatube_api
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

Активировать:

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

---

### 4. Выполнить миграции

```bash
python manage.py migrate
```

---

### 5. Создать суперпользователя (опционально)

```bash
python manage.py createsuperuser
```

---

### 6. Запустить сервер

```bash
python manage.py runserver
```

Сервер будет доступен по адресу:

```
http://127.0.0.1:8000/
```

---

## Аутентификация

Проект использует Token Authentication.

Получить токен:

POST запрос:

```
http://127.0.0.1:8000/api-token-auth/
```

Body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Ответ:

```json
{
  "token": "your_token"
}
```

Использование токена:

```
Authorization: Token your_token
```

---

## Основные endpoints

### Посты

Получить список постов:

```
GET /posts/
```

Создать пост:

```
POST /posts/
```

Получить пост:

```
GET /posts/{id}/
```

Редактировать пост:

```
PUT /posts/{id}/
PATCH /posts/{id}/
```

Удалить пост:

```
DELETE /posts/{id}/
```

---

### Группы

Получить список групп:

```
GET /groups/
```

Получить группу:

```
GET /groups/{id}/
```

---

### Комментарии

Получить комментарии поста:

```
GET /posts/{post_id}/comments/
```

Создать комментарий:

```
POST /posts/{post_id}/comments/
```

Получить комментарий:

```
GET /posts/{post_id}/comments/{id}/
```

Редактировать комментарий:

```
PUT /posts/{post_id}/comments/{id}/
PATCH /posts/{post_id}/comments/{id}/
```

Удалить комментарий:

```
DELETE /posts/{post_id}/comments/{id}/
```

---

## Права доступа

| Действие  | Доступ                |
| --------- | --------------------- |
| Просмотр  | Все пользователи      |
| Создание  | Только авторизованные |
| Изменение | Только автор          |
| Удаление  | Только автор          |

---
