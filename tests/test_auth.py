import time

# import pytest
import allure
from pages.auth_page import AuthPage

@allure.feature('Авторизация')
@allure.story('Авторизация с корректными логином и паролем')
def test_authorisation(web_browser,user_login="standard_user",
                       user_password="secret_sauce"):
    """Тестирование авторизации с использованием
    корректного логина и пароля"""
    page = AuthPage(web_browser)
    # time.sleep(1)

    # вводим данные для логина и пароля
    allure.step(f"ввод логина {user_login} и пароля {user_password}")
    page.username.send_keys(user_login)
    page.password.send_keys(user_password)

    # нажимаем кнопку "Войти"
    page.login_btn.click()
    time.sleep(1)

    # проверяем, что текущая страница - это страница профиля "Вход и безпасность"
    assert page.get_current_url() == 'https://www.saucedemo.com/inventory.html'
    assert page.app_logo.is_visible()
    assert page.btn_menu.is_visible()
    assert page.btn_shopping_cart.is_visible()
    assert page.btn_product_sort.is_visible()
    assert page.inventory_list.is_visible()

    # item_cards = page.inventory_items[0]
    # assert item_cards.is_visible()

    assert page.inventory_items.count() > 0
    assert page.items_img.count() > 0
    assert page.items_description.count() > 0
    assert page.items_description.count() == page.items_img.count() == page.inventory_items.count()

    page.close()

@allure.feature('Авторизация')
@allure.story('Авторизация с корректными логином и неверным паролем')
def test_negative_authorisation_wrong_pass(web_browser,user_login="standard_user",
                                           user_password="wrong_password"):
    """Тестирование авторизации с использованием
    корректного логина и неверного пароля"""
    page = AuthPage(web_browser)
    # time.sleep(1)

    allure.step(f"ввод логина {user_login} и пароля {user_password}")
    # вводим данные для логина и пароля
    page.username.send_keys(user_login)
    page.password.send_keys(user_password)

    # нажимаем кнопку "Войти"
    page.login_btn.click()
    time.sleep(1)

    # проверяем, что текущая страница - это не страница "All item"
    assert page.get_current_url() != 'https://www.saucedemo.com/inventory.html'
    assert page.form_error.is_visible()
    page.close()

@allure.feature('Авторизация')
@allure.story('Авторизация заблокированного логина')
def test_negative_authorisation_locked_user(web_browser,user_login="locked_out_user",
                                            user_password="secret_sauce"):
    """Тестирование авторизации с использованием
    заблокированного логина и верного пароля"""
    page = AuthPage(web_browser)
    # time.sleep(1)

    # вводим данные для логина и пароля
    page.username.send_keys(user_login)
    page.password.send_keys(user_password)

    # нажимаем кнопку "Войти"
    page.login_btn.click()
    time.sleep(1)

    # проверяем, что текущая страница - это не страница "All item"
    assert page.get_current_url() != 'https://www.saucedemo.com/inventory.html'
    assert page.form_error.is_visible()
    page.close()

@allure.feature('Авторизация')
@allure.story('Авторизация с пустыми полями логин и пароль')
def test_negative_authorisation_empty_data(web_browser,user_login="",
                                           user_password=""):
    """Тестирование авторизации с использованием
    пустых полей логин и пароля"""
    page = AuthPage(web_browser)
    # time.sleep(1)

    # вводим данные для логина и пароля
    page.username.send_keys(user_login)
    page.password.send_keys(user_password)

    # нажимаем кнопку "Войти"
    page.login_btn.click()
    time.sleep(1)

    # проверяем, что текущая страница - это не страница "All item"
    assert page.get_current_url() != 'https://www.saucedemo.com/inventory.html'
    assert page.form_error.is_visible()
    page.close()

@allure.feature('Авторизация')
@allure.story('Авторизация с корректным логином и паролем, с задержкой загрузки')
def test_authorisation_glitch_user(web_browser,user_login="performance_glitch_user",
                                   user_password="secret_sauce"):
    """Тестирование авторизации с использованием
    корректного логина и пароля, с задержкой загрузки"""
    page = AuthPage(web_browser)
    # time.sleep(1)

    # вводим данные для логина и пароля
    page.username.send_keys(user_login)
    page.password.send_keys(user_password)

    # нажимаем кнопку "Войти"
    page.login_btn.click()
    time.sleep(10)

    # проверяем, что текущая страница - это страница "All item"
    assert page.get_current_url() == 'https://www.saucedemo.com/inventory.html'
    assert page.app_logo.is_visible()
    assert page.btn_menu.is_visible()
    assert page.btn_shopping_cart.is_visible()
    assert page.btn_product_sort.is_visible()
    assert page.inventory_list.is_visible()

    assert page.inventory_items.count() > 0
    assert page.items_img.count() > 0
    assert page.items_description.count() > 0
    assert page.items_description.count() == page.items_img.count() == page.inventory_items.count()

    page.close()