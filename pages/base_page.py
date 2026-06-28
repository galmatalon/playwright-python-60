import time

from playwright.sync_api import Page


class BasePage:

    def __init__(self, page:Page):
        self.__page = page

    @property
    def page(self):
        return self.__page

    def fill_text(self, locator, text):
        #self.__page.locator(locator).highlight()
        self._highlight_element(locator)
       #time.sleep(0.5)
        self.__page.locator(locator).fill(text)

    def click(self, locator):
        self._highlight_element(locator)
        #self.__page.locator(locator).highlight()
        self.__page.locator(locator).click()

    def select_option(self, locator, text):
        #self.__page.locator(locator).highlight()
        self.__page.locator(locator).select_option(text)

    def get_text(self, locator):
        self._highlight_element(locator, "orange")
        #self.__page.locator(locator).highlight()
        text = self.__page.locator(locator).inner_text()
        return text

    def _highlight_element(self, locator: str, color: str = "yellow"):
        element = self.__page.locator(locator)
        element.evaluate(f"""
            (el) => {{
                const origShadow = el.style.boxShadow;
                const origBackground = el.style.backgroundColor;

                el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
                el.style.backgroundColor = '{color}';

                setTimeout(() => {{
                    el.style.boxShadow = origShadow;
                    el.style.backgroundColor = origBackground;
                }}, 300);
            }}
        """)


