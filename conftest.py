import pytest
from selenium import webdriver
import os
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def web_browser():
    # -----------------
    # вебдрайвер для запуска тестов в IDE
    # browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    # -----------------

    # -----------------
    # вебдрайвер для выполнения в Докере
    # chrome_options = Options()
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--disable-webrtc")
    # chrome_options.add_argument("--hide-scrollbars")
    # chrome_options.add_argument("--disable-notifications")
    # chrome_options.add_argument("--start-maximized")

    # адрес сервера для запуска тестов в IDE
    # с запущенным в Докере selenium/standalone-chrome сервером
    # SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")

    # адрес сервера для запуска тестов в Докере
    # SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://host.docker.internal:4444/wd/hub")
    # browser = webdriver.Remote(
    #     command_executor=SELENIUM_REMOTE_URL,
    #     options=chrome_options
    # )
    # -----------------

    browser.implicitly_wait(10)

    yield browser
    browser.close()