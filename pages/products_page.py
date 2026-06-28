from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.footer_comp import FooterComponent
from pages.components.header_comp import HeaderComponent


class ProductsPage(HeaderComponent, BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__footer = FooterComponent(page)

    __AREA_LIST = ".inventory_item"
    __PRODUCT_NAME_LABEL = ".inventory_item_name"

    @property
    def footer(self):
        return self.__footer

    def add_product(self,product_name):
        area_list = self.page.locator(self.__AREA_LIST)

        for i in range(area_list.count()):
            title_label = area_list.nth(i).locator(self.__PRODUCT_NAME_LABEL)
            if title_label.inner_text() == product_name:
                add_to_cart_btn = area_list.nth(i).locator("button")
                add_to_cart_btn.click()
                break


