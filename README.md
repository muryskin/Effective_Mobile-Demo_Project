# Демонстрационный проект для Effective Mobile

### Задача: <br> Автоматизировать тестирование логина на сайте https://www.saucedemo.com/ с использованием Python.

#### Написать 5 тестов, проверяющих разные сценарии авторизации:
1. Успешный логин (standard_user / secret_sauce)
2. Логин с неверным паролем
3. Логин заблокированного пользователя (locked_out_user)
4. Логин с пустыми полями
5. Логин пользователем performance_glitch_user (проверить корректный переход и что страница открывается несмотря на возможные задержки)

#### Требования:
1. Использовать Selenium или Playwright
2. Использовать Page Object
3. Подключить Allure
4. Проверять корректность URL и отображение элементов
5. Добавить Dockerfile для запуска тестов в контейнере
6. Python 3.10
7. Все зависимости — в requirements.txt
8. Короткая инструкция по запуску — в README.md

---

### Структура проекта:

**conftest.py** - 

**tests/test_auth.py** - авто-тесты для тестирования логина: <br>
- test_authorisation - Авторизация с корректными логином и паролем
- test_negative_authorisation_wrong_pass - Авторизация с корректными логином и неверным паролем
- test_negative_authorisation_locked_user - Авторизация заблокированного логина
- test_negative_authorisation_empty_data - Авторизация с пустыми полями логин и пароль
- test_authorisation_glitch_user - Авторизация с корректным логином и паролем, с задержкой загрузки

**pages/base.py** - 

**pages/elements.py** - 

**pages/auth_page.py** - 

**requirements.txt** - 

**Dockerfile** - 

**allure-results** - 

**allure-report** - 
