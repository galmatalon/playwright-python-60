from playwright.sync_api import Page

from pages.base_page import BasePage


class FooterComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __LINKEDIN_BTN= "[data-test='social-linkedin']"
    __FB_BTN = "[data-test='social-facebook']"

    def open_linkedin(self):
        self.click(self.__LINKEDIN_BTN)

    def open_facebook(self):
        self.click(self.__FB_BTN)
