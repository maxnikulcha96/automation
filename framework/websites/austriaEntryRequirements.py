"""Austria entry requirements website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AustriaEntryRequirements(Website):
    def __init__(self, browser):
        """
        Initializes a new AustriaEntryRequirements instance.

        :param browser: The browser conncetion.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://goverdrive.portal.at/index.php/s/qnepQJZoEEZgX22"

        self.locators = {
            "disclaimer_label": (By.XPATH, "//label[@for='id_disclaimer']"),
            "accept_cookies_button": (By.ID, 'id_btn_ack'),
            "download_file_a": (By.ID, 'downloadFile')
        }

        Website.__init__(self, browser, self.url)

    def accept_cookies(self):
        try:
            self.browser.click(self.locators["disclaimer_label"])
            self.browser.click(self.locators["accept_cookies_button"])
            print("Clicked accept essential cookies only")
        except NoSuchElementException:
            print("Unable to accept cookies")

    def get_entry_requirements(self):
        self.browser.click(self.locators["download_file_a"])
        print("Downloaded entry requirements file")

    def login(self):
        super().login()

    def logout(self):
        super().logout()
