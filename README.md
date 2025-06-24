# Тесты проекта

## Установка и запуск тестов

### 1. Создание виртуального окружения и установка зависимостей

python -m venv venv
source venv/bin/activate      # Для Windows используйте: venv\Scripts\activate
pip install -r requirements.txt

### №2. Установка браузеров для Playwright

playwright install

### 3. Запуск тестов

## Запустить все тесты:

pytest

## Запустить конкретный файл с тестами:

pytest tests/test_company_access.py

## Запустить конкретный тест:

pytest tests/test_company_access.py::test_director_matches_current_user