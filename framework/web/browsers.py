"""The browsers implementation."""

from abc import ABC
from sqlite3 import NotSupportedError
from selenium import webdriver


class BaseBrowser(ABC):
    def __init__(self, driver, maximized=False, headless=True, slowRun=True):
        """
        Initializes a new BaseBrowser instance.

        :param driver: The selenium webdriver connection.
        :param maximized: If to maximize the browser window (default False).
        :param headless: If to hide the browser window (default True).
        :param slowRun: If to execute the commands with delay (default True).
        """

        self.driver = driver
        self.maximized = maximized
        self.headless = headless
        self.slowRun = slowRun

    def check_slow_run(self):
        if self.slowRun:
            from time import sleep

            sleep(5)

    def setup_driver(self):
        """
        Setups and configures the webdriver.
        """

        self.driver.implicitly_wait(10)

        if self.maximized:
            self.driver.maximize_window()

    def load_url(self, url):
        """
        Loads a web page.

        :param url: The web page URL.
        """

        self.driver.get(url)
        print("Loaded url: {}".format(url))

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

        self.check_slow_run()

        element = self.find_element(locator)
        element.send_keys(text)

    def get_element_text(self, locator):
        """
        Returns the text of the web element.

        :param locator: The locator of the web element.
        """

        self.check_slow_run()

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

        self.check_slow_run()

        element = self.find_element(locator)
        element.click()

    def select_value_from_dropdown(self, locator, value):
        """
        Selects a specific value from the dropdown.

        :param locator: The locator of the web element.
        :param value: The value to select.
        """

        from selenium.webdriver.support.select import Select

        self.check_slow_run()

        sel = Select(self.driver.find_element(*locator))
        sel.select_by_visible_text(value)

    def take_screenshot(self, filename):
        """
        Takes a screenshot of the browser content.

        :param filename: The name of the screenshot file.
        """

        self.driver.save_screenshot(filename)

        print("Screenshot saved into: {}".format(filename))

    def execute_script(self, script):
        """
        Executes a JavaScript code on the browser.

        :param script: The script to execute.
        """

        self.driver.driver.execute_script(script)
        
        print("Executed script: {}".format(script))

    def close(self):
        """
        Closes the web browser.
        """

        self.driver.close()


class SafariBrowser(BaseBrowser):
    def __init__(self, maximized=False, headless=True, slowRun=True):
        """
        Initializes a new SafariBrowser instance.

        :param driver: The selenium webdriver connection.
        :param maximized: If to maximize the browser window (default False).
        :param headless: If to hide the browser window (default True).
        :param slowRun: If to execute the commands with delay (default True).
        """

        self.maximized = maximized
        self.headless = headless
        self.slowRun = slowRun

        if self.headless:
            raise NotSupportedError(
                'Headless mode currently not supported in Safari')
        else:
            self.driver = webdriver.Safari()

        BaseBrowser.__init__(self, self.driver, maximized, headless, slowRun)

        self.setup_driver()

    def setup_driver(self):
        """
        Setups and configures the webdriver.
        """

        BaseBrowser.setup_driver(self)


class FirefoxBrowser(BaseBrowser):
    def __init__(self, maximized=False, headless=True, slowRun=True):
        """
        Initializes a new FirefoxBrowser instance.

        :param driver: The selenium webdriver connection.
        :param maximized: If to maximize the browser window (default False).
        :param headless: If to hide the browser window (default True).
        :param slowRun: If to execute the commands with delay (default True).
        """

        self.maximized = maximized
        self.headless = headless
        self.slowRun = slowRun

        if self.headless:
            from selenium.webdriver.firefox.options import Options as FirefoxOptions

            options = FirefoxOptions()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(
                options=options, executable_path='/usr/local/bin/geckodriver')
        else:
            self.driver = webdriver.Firefox(
                executable_path='/usr/local/bin/geckodriver')

        BaseBrowser.__init__(self, self.driver, maximized, headless, slowRun)

        self.setup_driver()
