import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_class")
class TestAddProduct(BaseTest):

    def test_01_add_product(self):
        self.login_page.login("standard_user", "secret_sauce")
        self.products_page.add_product("Sauce Labs Fleece Jacket")
        assert self.products_page.get_items_in_cart() == 1

    def test_02_add_product(self):
        self.products_page.add_product("Sauce Labs Bike Light")
        assert self.products_page.get_items_in_cart() == 2

    def test_03_add_product(self):
        self.products_page.footer.open_facebook()






