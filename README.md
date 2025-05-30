# JSONPlaceholder API Autotests

Автоматические тесты для проверки публичного REST API [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## 📌 Что проверяется:

- Успешное создание поста (`POST /posts`)
- Успешное изменение поста (`PUT /posts/1`)
- Успешное удаление поста (`DELETE /posts/1`)

## 📦 Требования

- Python 3.7+
- requests
- pytest

## 🚀 Установка и запуск

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Запустите тесты:

```bash
pytest test_jsonplaceholder_api.py
```

## 🧾 Файлы (находятся в ветке master)

- `test_jsonplaceholder_api.py` — автотест
- `requirements.txt` — зависимости
