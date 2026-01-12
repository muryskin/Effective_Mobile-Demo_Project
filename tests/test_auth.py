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
    with allure.step("Открытие страницы для логина"):
        page = AuthPage(web_browser)

    with allure.step("Ввод данных для логина и пароля"):
    # вводим данные для логина и пароля
        page.username.send_keys(user_login)
        page.password.send_keys(user_password)

    with allure.step("Нажатие кнопки 'Войти'"):
    # нажимаем кнопку "Войти"
        page.login_btn.click()
        time.sleep(1)

    with (allure.step("Проверка: текущая страница - 'All item'")):
    # проверяем, что текущая страница - это страница "All item"
        assert page.get_current_url() == 'https://www.saucedemo.com/inventory.html', f"Не удалось залогиниться с использованием {user_login} и {user_password}"

    with allure.step("Проверка: логотип приложения видимый"):
        assert page.app_logo.is_visible()

    with allure.step("Проверка: кнопка 'Меню' видимая"):
        assert page.btn_menu.is_visible()

    with allure.step("Проверка: кнопка 'Корзина' видимая"):
        assert page.btn_shopping_cart.is_visible()

    with allure.step("Проверка: кнопка 'Сортировка' видимая"):
        assert page.btn_product_sort.is_visible()

    with allure.step("Проверка: список товаров видимый"):
        assert page.inventory_list.is_visible()

    with allure.step("Проверка: в списке есть как минимум один товар"):
        assert page.inventory_items.count() > 0

    with allure.step("Проверка: в списке есть фото как минимум у одного товара"):
        assert page.items_img.count() > 0

    with allure.step("Проверка: в списке есть описание как минимум у одного товара"):
        assert page.items_description.count() > 0

    with allure.step("Проверка: Количество товаров в списке совпадает с количеством фотографий и количеством описаний товаров"):
        assert page.items_description.count() == page.items_img.count() == page.inventory_items.count()


@allure.feature('Авторизация')
@allure.story('Авторизация с корректными логином и неверным паролем')
def test_negative_authorisation_wrong_pass(web_browser,user_login="standard_user",
                                           user_password="wrong_password"):
    """Тестирование авторизации с использованием
    корректного логина и неверного пароля"""
    with allure.step("Открытие страницы для логина"):
        page = AuthPage(web_browser)

    with allure.step("Ввод данных для логина и пароля"):
    # вводим данные для логина и пароля
        page.username.send_keys(user_login)
        page.password.send_keys(user_password)

    with allure.step("Нажатие кнопки 'Войти'"):
    # нажимаем кнопку "Войти"
        page.login_btn.click()
    time.sleep(1)

    with allure.step("Проверка: текущая страница - не 'All item'"):
    # проверяем, что текущая страница - это не страница "All item"
        assert page.get_current_url() != 'https://www.saucedemo.com/inventory.html'

    with allure.step("Проверка: форма ошибки видима"):
        assert page.form_error.is_visible()

@allure.feature('Авторизация')
@allure.story('Авторизация заблокированного логина')
def test_negative_authorisation_locked_user(web_browser,user_login="locked_out_user",
                                            user_password="secret_sauce"):
    """Тестирование авторизации с использованием
    заблокированного логина и верного пароля"""
    with allure.step("Открытие страницы для логина"):
        page = AuthPage(web_browser)

    with allure.step("Ввод данных для логина и пароля"):
    # вводим данные для логина и пароля
        page.username.send_keys(user_login)
        page.password.send_keys(user_password)

    with allure.step("Нажатие кнопки 'Войти'"):
    # нажимаем кнопку "Войти"
        page.login_btn.click()
    time.sleep(1)

    with allure.step("Проверка: текущая страница - не 'All item'"):
    # проверяем, что текущая страница - это не страница "All item"
        assert page.get_current_url() != 'https://www.saucedemo.com/inventory.html'

    with allure.step("Проверка: форма ошибки видима"):
        assert page.form_error.is_visible()

@allure.feature('Авторизация')
@allure.story('Авторизация с пустыми полями логин и пароль')
def test_negative_authorisation_empty_data(web_browser,user_login="",
                                           user_password=""):
    """Тестирование авторизации с использованием
    пустых полей логин и пароля"""
    with allure.step("Открытие страницы для логина"):
        page = AuthPage(web_browser)

    with allure.step("Ввод данных для логина и пароля"):
    # вводим данные для логина и пароля
        page.username.send_keys(user_login)
        page.password.send_keys(user_password)

    with allure.step("Нажатие кнопки 'Войти'"):
    # нажимаем кнопку "Войти"
        page.login_btn.click()
    time.sleep(1)

    with allure.step("Проверка: текущая страница - не 'All item'"):
    # проверяем, что текущая страница - это не страница "All item"
        assert page.get_current_url() != 'https://www.saucedemo.com/inventory.html'

    with allure.step("Проверка: форма ошибки видима"):
        assert page.form_error.is_visible()

@allure.feature('Авторизация')
@allure.story('Авторизация с корректным логином и паролем, с задержкой загрузки')
def test_authorisation_glitch_user(web_browser,user_login="performance_glitch_user",
                                   user_password="secret_sauce"):
    """Тестирование авторизации с использованием
    корректного логина и пароля, с задержкой загрузки"""
    with allure.step("Открытие страницы для логина"):
        page = AuthPage(web_browser)

    with allure.step("Ввод данных для логина и пароля"):
    # вводим данные для логина и пароля
        page.username.send_keys(user_login)
        page.password.send_keys(user_password)

    with allure.step("Нажатие кнопки 'Войти'"):
    # нажимаем кнопку "Войти"
        page.login_btn.click()
    time.sleep(10)

    with (allure.step("Проверка: текущая страница - 'All item'")):
    # проверяем, что текущая страница - это страница "All item"
        assert page.get_current_url() == 'https://www.saucedemo.com/inventory.html', f"Не удалось залогиниться с использованием {user_login} и {user_password}"

    with allure.step("Проверка: логотип приложения видимый"):
        assert page.app_logo.is_visible()

    with allure.step("Проверка: кнопка 'Меню' видимая"):
        assert page.btn_menu.is_visible()

    with allure.step("Проверка: кнопка 'Корзина' видимая"):
        assert page.btn_shopping_cart.is_visible()

    with allure.step("Проверка: кнопка 'Сортировка' видимая"):
        assert page.btn_product_sort.is_visible()

    with allure.step("Проверка: список товаров видимый"):
        assert page.inventory_list.is_visible()

    with allure.step("Проверка: в списке есть как минимум один товар"):
        assert page.inventory_items.count() > 0

    with allure.step("Проверка: в списке есть фото как минимум у одного товара"):
        assert page.items_img.count() > 0

    with allure.step("Проверка: в списке есть описание как минимум у одного товара"):
        assert page.items_description.count() > 0

    with allure.step("Проверка: Количество товаров в списке совпадает с количеством фотографий и количеством описаний товаров"):
        assert page.items_description.count() == page.items_img.count() == page.inventory_items.count()
