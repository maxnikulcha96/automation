"""Migdal Pension plan website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By


class MigdalPensionPlan(Website):
    def __init__(self, browser):
        """
        Initializes a new MigdalPensionPlan instance.

        :param browser: The browser conncetion.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://www.migdal.co.il/mymigdal/process/login"

        self.locators = {
            "israel_id_input": (By.XPATH, "//input[@name='id']"),
            "submit_button": (By.XPATH, "//button[@type='submit']"),
            "code_input": (By.ID, "code"),
            "pension_amount_div": (By.CLASS_NAME, "lobbyPage_itemPrice"),
        }

        Website.__init__(self, browser, self.url)

    def fill_israel_id(self, id):
        self.browser.write_text(self.locators["israel_id_input"], id)
        print("Filled Israel ID: {0}".format(id))

    def click_submit_button(self):
        self.browser.click(self.locators["submit_button"])
        print("Clicked submit button")

    def fill_code(self, code):
        self.browser.write_text(self.locators["code_input"], code)
        print("Filled code: {0}".format(code))

    def get_pension_amount(self):
        return self.browser.get_element_text(self.locators["pension_amount_div"])

    def logout(self):
        super().logout()
        
        self.browser.execute_script("authenticatedUser.logout()")
