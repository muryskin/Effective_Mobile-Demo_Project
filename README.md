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

**tests/test_auth.py** - авто-тесты для тестирования логина: <br>
- test_authorisation - Авторизация с корректными логином и паролем
- test_negative_authorisation_wrong_pass - Авторизация с корректными логином и неверным паролем
- test_negative_authorisation_locked_user - Авторизация заблокированного логина
- test_negative_authorisation_empty_data - Авторизация с пустыми полями логин и пароль
- test_authorisation_glitch_user - Авторизация с корректным логином и паролем, с задержкой загрузки

**pages/base.py** - базовые методы Page Object

**pages/elements.py** - методы для взаимодействия с элементами Page Object

**pages/auth_page.py** - элементы страницы авторизации

**conftest.py** - файл конфигурации
- для запуска тестов в IDE раскомментировать строку:
> browser = webdriver.Chrome() <br>
> или <br>
> browser = webdriver.Firefox() <br>

- для запуска тестов с использованием Докера раскомментировать строки:
> chrome_options = Options() <br>
> chrome_options.add_argument("--no-sandbox") <br>
> chrome_options.add_argument("--disable-dev-shm-usage") <br>
> chrome_options.add_argument("--disable-gpu") <br>
> chrome_options.add_argument("--disable-webrtc") <br>
> chrome_options.add_argument("--hide-scrollbars") <br>
> chrome_options.add_argument("--disable-notifications") <br>
> chrome_options.add_argument("--start-maximized") <br>
>
> адрес сервера для запуска тестов в IDE с запущенным в Докере selenium/standalone-chrome сервером <br>
> SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub") <br>
> или <br>
> адрес сервера для запуска тестов в Докере <br>
> SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://host.docker.internal:4444/wd/hub") <br>
>
> browser = webdriver.Remote(command_executor=SELENIUM_REMOTE_URL,options=chrome_options) <br>

**requirements.txt** - зависимости

**Dockerfile, docker-compose.yml** - файлы для запуска тестов в контейнере с использованием selenium/standalone-chrome сервера
- запуск всех служб из docker-compose.yml (проложение для автотестов и selenium/standalone-chrome сервер):
> docker compose up -d

**allure-results** - allure-результаты проведенных авто-тестов

**allure-report** - allute-отчеты по проведенным авто-тестам
