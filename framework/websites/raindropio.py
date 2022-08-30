"""Raindrop.io website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By


class RaindropIO(Website):
    def __init__(self, browser):
        """
        Initializes a new RaindropIO instance.

        :param browser: The browser conncetion.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://app.raindrop.io/"

        self.locators = {
            "login_email_input": (By.XPATH, '//input[@name="email"]'),
            "login_password_input": (By.XPATH, '//input[@name="password"]'),
            "login_signin_input_button": (By.XPATH, '//input[@type="submit"]'),
            "create_new_backup_div": (By.XPATH, '//div[contains(text(),"Create")]'),
            "menu_button": (By.ID, "button-BT4k"),
            "logout_a": (By.XPATH, '//a[contains(text(),"Logout")]')
        }

        Website.__init__(self, browser, self.url)

    def login_website(self, email, password):
        self.browser.write_text(self.locators["login_email_input"], email)
        self.browser.write_text(
            self.locators["login_password_input"], password)

        self.browser.click(self.locators["login_signin_input_button"])
        print("Clicked sign in button")

    def open_backups_page(self):
        self.browser.load_url("https://app.raindrop.io/settings/backups")

    def click_create_new_backup(self):
        self.browser.click(self.locators["create_new_backup_div"])
        print("Clicked create new backup button")

    def go_back_to_main_page(self):
        self.browser.load_url(self.url)
        
    def login(self):
        super().login()

    def logout(self):
        super().logout()

        self.browser.click(self.locators["menu_button"])
        print("Clicked menu button")

        self.browser.click(self.locators["logout_a"])
        print("Clicked logout button")


