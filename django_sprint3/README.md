# Блогикум — часть 2

Учебный Django-проект с публикациями, категориями и местоположениями.

## Структура

- `blogicum/` — рабочая папка Django-проекта;
- `tests/` — тесты Практикума;
- `db.json` — фикстуры базы данных;
- `pytest.ini` — настройки pytest;
- `requirements.txt` — зависимости;
- `.flake8` — настройки проверки стиля;
- `.gitignore` — исключения Git.

## Запуск

```text
cd blogicum
python manage.py migrate
python manage.py loaddata ../db.json
python manage.py runserver
```

Тесты запускаются из корня проекта:

```text
pytest
```
