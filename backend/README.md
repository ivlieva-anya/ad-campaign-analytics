# Ad Campaign Analytics Backend

Бэкенд для системы аналитики рекламных кампаний, написанный на Python с использованием FastAPI.

## Требования

- Python 3.8+
- PostgreSQL
- pip

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` в корневой директории бэкенда:
```
DATABASE_URL=postgresql://user:password@localhost/ad_campaign_db
SECRET_KEY=your-secret-key
```

4. Создайте базу данных PostgreSQL:
```sql
CREATE DATABASE ad_campaign_db;
```

## Запуск

1. Запустите сервер разработки:
```bash
uvicorn main:app --reload
```

2. API будет доступно по адресу: http://localhost:8000
3. Документация API (Swagger UI): http://localhost:8000/docs

## Структура проекта

- `main.py` - основной файл приложения
- `database.py` - настройки базы данных
- `models.py` - модели данных
- `auth.py` - утилиты аутентификации
- `requirements.txt` - зависимости проекта

## API Endpoints

- `POST /api/auth/register` - регистрация нового пользователя
- `POST /api/auth/login` - аутентификация пользователя
- `GET /api/user/profile` - получение профиля пользователя
- `GET /api/campaigns` - получение списка кампаний
- `POST /api/campaigns` - создание новой кампании
- `GET /api/reports` - получение отчетов
- `POST /api/reports` - создание нового отчета 