from abc import ABC
from selenium import webdriver


class BaseBrowser(ABC):
    def __init__(self, driver, maximized=False):

        self.driver = driver
        self.maximized = maximized

    def setup_driver(self):
        self.driver.implicitly_wait(30)

        if self.maximized:
            self.driver.maximize_window()

    def load_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):

        return self.driver.find_element(*locator)

    def get_title(self):

        return self.driver.title

    def clear_text(self, locator):

        element = self.find_element(locator)
        element.clear()

    def write_text(self, locator, text):

        element = self.find_element(locator)
        element.send_keys(text)

    def get_element_text(self, locator):

        element = self.find_element(locator)

        if element.tag_name == "INPUT":
            return element.get_attribute("value")
        else:
            return element.text

    def click(self, locator):

        element = self.find_element(locator)
        element.click()

    def select_value_from_dropdown(self, locator, value):
        from selenium.webdriver.support.select import Select

        sel = Select(self.driver.find_element(*locator))
        sel.select_by_visible_text(value)

    def close(self):

        self.driver.close()


class SafariBrowser(BaseBrowser):
    def __init__(self, maximized=False):

        self.driver = webdriver.Safari()

        BaseBrowser.__init__(self, self.driver, maximized)

        self.setup_driver()
