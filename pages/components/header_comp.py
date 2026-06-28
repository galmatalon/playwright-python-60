from playwright.sync_api import Page

from pages.base_page import BasePage


class HeaderComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __CART_BTN = ".shopping_cart_link"
    __CART_ITEMS_LABEL = ".shopping_cart_badge"
    __MENU_BTN = "#react-burger-menu-btn"
    __LOGOUT_BTN = "#logout_sidebar_link"

    def open_cart(self):
        self.click(self.__CART_BTN)

    def logout(self):
        self.click(self.__MENU_BTN)
        self.click(self.__LOGOUT_BTN)

    def get_items_in_cart(self):
        text = self.get_text(self.__CART_ITEMS_LABEL)
        num = int(text)
        return num