import pytest
from selenium import webdriver

@pytest.fixture()
def web_browser():
    # browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    return browser