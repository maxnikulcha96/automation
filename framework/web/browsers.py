"""The browsers implementation."""

from abc import ABC
from selenium import webdriver


class BaseBrowser(ABC):
    def __init__(self, driver, maximized=False):
        """
        Initializes a new BaseBrowser instance.

        :param driver: The selenium webdriver connection.
        :param maximized: If to maximize the browser window (default False).
        """

        self.driver = driver
        self.maximized = maximized

    def setup_driver(self):
        """
        Setups and configures the webdriver.
        """

        self.driver.implicitly_wait(30)

        if self.maximized:
            self.driver.maximize_window()

    def load_url(self, url):
        """
        Loads a web page.

        :param url: The web page URL.
        """

        self.driver.get(url)

    def find_element(self, locator):
        """
        Finds and returns a web element by the given locator.

        :param locator: The locator of the web element.
        """

        return self.driver.find_element(*locator)

    def get_title(self):
        """
        Returns the title of the current page.
        """

        return self.driver.title

    def clear_text(self, locator):
        """
        Clears the text from the web element.

        :param locator: The locator of the web element.
        """

        element = self.find_element(locator)
        element.clear()

    def write_text(self, locator, text):
        """
        Writes the text into the web element.

        :param locator: The locator of the web element.
        :param text: The text to write.
        """

        element = self.find_element(locator)
        element.send_keys(text)

    def get_element_text(self, locator):
        """
        Returns the text of the web element.

        :param locator: The locator of the web element.
        """

        element = self.find_element(locator)

        if element.tag_name == "INPUT":
            return element.get_attribute("value")
        else:
            return element.text

    def click(self, locator):
        """
        Clicks the web element.

        :param locator: The locator of the web element.
        """

        element = self.find_element(locator)
        element.click()

    def select_value_from_dropdown(self, locator, value):
        """
        Selects a specific value from the dropdown.

        :param locator: The locator of the web element.
        :param value: The value to select.
        """

        from selenium.webdriver.support.select import Select

        sel = Select(self.driver.find_element(*locator))
        sel.select_by_visible_text(value)

    def close(self):
        """
        Closes the web browser.
        """

        self.driver.close()


class SafariBrowser(BaseBrowser):
    def __init__(self, maximized=False):
        """
        Initializes a new SafariBrowser instance.

        :param maximized: If to maximize the browser window (default False).
        """

        self.driver = webdriver.Safari()

        BaseBrowser.__init__(self, self.driver, maximized)

        self.setup_driver()
