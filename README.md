# 📸 PhotoShare API

## 🚀 Запуск проєкту

```bash
poetry install
poetry run uvicorn app.main:app --reload
```

## 📍 Swagger

http://127.0.0.1:8000/docs

## 📦 Структура проєкту

* `models/` — моделі бази даних
* `schemas/` — API схеми (Pydantic)
* `services/` — бізнес-логіка
* `routes/` — API ендпоінти
* `auth/` — авторизація та безпека
* `database/` — підключення до БД
* `config/` — налаштування

## 🧪 Статус проєкту

🟡 Day 0 — базова структура та запуск сервера
