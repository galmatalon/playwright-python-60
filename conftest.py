import time

import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import ConfigReader


# Ise this code in the conftest.py
# In case you want to open browser before each class
@pytest.fixture(scope="class")
def setup_page_class(request, browser):
    request.cls.page = browser.new_page()
    url = ConfigReader.read_config("general", "url")
    request.cls.page.goto(url)
    request.cls.login_page = LoginPage(request.cls.page)
    request.cls.products_page = ProductsPage(request.cls.page)
    request.cls.cart_page = CartPage(request.cls.page)

    yield
    # request.cls.page.close()
    # browser.close()
    time.sleep(10)


# Ise this code in the conftest.py
# In case you want to open browser before each method (test)
@pytest.fixture(scope="function")
def setup_page_function(request, page: Page):
    url = ConfigReader.read_config("general","url")
    page.goto(url)
    request.cls.login_page = LoginPage(page)
    request.cls.products_page = ProductsPage(page)
    request.cls.cart_page = CartPage(page)