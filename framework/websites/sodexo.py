"""Sodexo website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By


class Sodexo(Website):
    def __init__(self, browser):
        """
        Initializes a new Sodexo website instance.

        :param browser: The browser instance.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://sodexo-ucet.cz"

        self.locators = {
            "accept_all_cookies_button": (By.ID, "onetrust-accept-btn-handler"),
            "login_email_input": (By.ID, "Username"),
            "login_password_input": (By.ID, "Password"),
            "login_button": (By.XPATH, "//button[@type='submit']"),
            "balance_a": (By.CLASS_NAME, "benefits__balance")
        }

        Website.__init__(self, browser, self.url)

    def __accept_cookies(self):
        self.browser.click(self.locators["accept_all_cookies_button"])
        print("Clicked 'accept all cookies' button")

    def login(self, email, password):
        """
        Login the website.

        :param email: The login email.
        :param password: The login password.
        """

        self.__accept_cookies()

        self.browser.write_text(self.locators["login_email_input"], email)
        self.browser.write_text(
            self.locators["login_password_input"], password)

        self.browser.click(self.locators["login_button"])
        print("Clicked 'login' button")

    def get_balance(self):
        return self.browser.get_element_text(self.locators["balance_a"])
