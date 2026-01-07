from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.saucedemo.com/'
        super().__init__(web_driver, url)

    # Элементы страницы авторизации
    # логотип страницы
    login_logo = WebElement(xpath='//div[@class="login-logo"]')
    # строка ввода логина
    username = WebElement(xpath='//input[@id="user-name"]')
    # строка ввода пароля
    password = WebElement(xpath='//input[@id="password"]')
    # кнопка "Войти"
    login_btn = WebElement(xpath='//input[@id="login-button"]')

    # Элементы страницы приложения
    # лого приложения
    app_logo = WebElement(xpath='//div[@class="app_logo"]')

    # кнопка Меню
    btn_menu = WebElement(xpath='//button[@id="react-burger-menu-btn"]')
    # переход на страницу "все товары"
    btn_all_item = WebElement(xpath='//a[@id="inventory_sidebar_link"]')
    # переход на страницу "о нас"
    btn_about = WebElement(xpath='//a[@id="about_sidebar_link"]')
    # кнопка "разлогиниться"
    btn_logout = WebElement(xpath='//a[@id="logout_sidebar_link"]')
    # кнопка "сбросить состояние приложения"
    btn_reset = WebElement(xpath='//a[@id="reset_sidebar_link"]')
    # кнопка "закрыть меню"
    btn_cross = WebElement(xpath='//button[@id="react-burger-cross-btn"]')

    # кнопка "Корзина"
    btn_shopping_cart = WebElement(xpath='//div[@id="shopping_cart_container"]')
    # кнопка сортировки
    btn_product_sort = WebElement(xpath='//select[@class="product_sort_container"]')

    # список товаров
    inventory_list = WebElement(xpath='//div[@class="inventory_list"]')
    # карточки товаров
    inventory_items = ManyWebElements(xpath='//div[@class="inventory_item"]')
    # фото товаров
    items_img = ManyWebElements(xpath='//div[@class="inventory_item_img"]')

    # описание товаров
    items_description = ManyWebElements(xpath='//div[@class="inventory_item_description"]')
    items_name = ManyWebElements(xpath='//div[@class="inventory_item_name"]')
    items_desc = ManyWebElements(xpath='//div[@class="inventory_item_desc"]')

    items_pricebar = ManyWebElements(xpath='//div[@class="pricebar"]')
    items_price = ManyWebElements(xpath='//div[@class="inventory_item_price"]')
    btn_add_to_cart = WebElement(xpath='//button[contains(@class,"btn btn_primary btn_small btn_inventory")]')

    # сообщение об ошибке при неудачной авторизации
    # form_error = WebElement(xpath='//div[contains(@class,"error-message-container error"]')
    form_error = WebElement(xpath='//h3[@data-test="error"]')
