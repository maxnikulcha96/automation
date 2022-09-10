"""The browsers implementation."""

from abc import ABC
from sqlite3 import NotSupportedError
from selenium import webdriver


class BaseBrowser(ABC):
    def __init__(self, driver, maximized=False, headless=True, timeout=30):
        """
        Initializes a new BaseBrowser instance.

        :param driver: The selenium webdriver connection.
        :param maximized: If to maximize the browser window (default False).
        :param headless: If to hide the browser window (default True).
        :param timeout: The timeout between each command (default 5 sec).
        """

        self.driver = driver
        self.maximized = maximized
        self.headless = headless
        self.timeout = timeout

        if self.maximized:
            self.driver.maximize_window()

    def load_url(self, url):
        """
        Loads a web page.

        :param url: The web page URL.
        """

        self.driver.get(url)

        print("Loaded url: '{0}'".format(url))

    def find_element(self, locator):
        """
        Finds and returns a web element by the given locator.

        :param locator: The locator of the web element.
        """

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException

        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException:
            print("The element with locator:'{}' was not found".format(locator))

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

    def select_item_from_dropdown_by_text(self, locator, value):
        """
        Selects a specific item from the dropdown by text.

        :param locator: The locator of the web element.
        :param value: The item to select.
        """

        from selenium.webdriver.support.select import Select

        sel = Select(self.driver.find_element(*locator))
        sel.select_by_visible_text(value)

    def select_item_from_dropdown_by_value(self, locator, value):
        """
        Selects a specific item from the dropdown by value.

        :param locator: The locator of the web element.
        :param value: The item to select.
        """

        from selenium.webdriver.support.select import Select

        sel = Select(self.driver.find_element(*locator))
        sel.select_by_value(value)

    def take_screenshot(self, filename):
        """
        Takes a screenshot of the browser content.

        :param filename: The name of the screenshot file.
        """

        self.driver.save_screenshot(filename)

        print("Screenshot saved into: {0}".format(filename))

    def wait(self, seconds):
        """
        Delays the execution of the next action for a given number of seconds.

        :param seconds: The number of seconds to wait.
        """

        from time import sleep
        sleep(seconds)

    def execute_script(self, script):
        """
        Executes a JavaScript code on the browser.

        :param script: The script to execute.
        """

        self.driver.execute_script(script)

        print("Executed script: {0}".format(script))

    def close(self):
        """
        Closes the web browser.
        """

        self.driver.close()
        self.driver.quit()


class SafariBrowser(BaseBrowser):
    def __init__(self, maximized=False, headless=True, timeout=30):
        """
        Initializes a new SafariBrowser instance.

        :param driver: The selenium webdriver connection.
        :param maximized: If to maximize the browser window (default False).
        :param headless: If to hide the browser window (default True).
        :param timeout: The timeout between each command (default 5 sec).
        """

        self.maximized = maximized
        self.headless = headless
        self.timeout = timeout

        if self.headless:
            raise NotSupportedError(
                'Headless mode currently not supported in Safari')
        else:
            self.driver = webdriver.Safari()

        BaseBrowser.__init__(self, self.driver, maximized,
                             headless, timeout)


class FirefoxBrowser(BaseBrowser):
    def __init__(self, maximized=False, headless=True, timeout=30):
        """
        Initializes a new FirefoxBrowser instance.

        :param driver: The selenium webdriver connection.
        :param maximized: If to maximize the browser window (default False).
        :param headless: If to hide the browser window (default True).
        :param timeout: The timeout between each command (default 5 sec).
        """

        self.maximized = maximized
        self.headless = headless
        self.timeout = timeout

        geckodriver_path = '/usr/local/bin/geckodriver'

        if self.headless:
            from selenium.webdriver.firefox.options import Options as FirefoxOptions

            options = FirefoxOptions()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(
                options=options, executable_path=geckodriver_path)
        else:
            self.driver = webdriver.Firefox(
                executable_path=geckodriver_path)

        BaseBrowser.__init__(self, self.driver, maximized,
                             headless, timeout)
