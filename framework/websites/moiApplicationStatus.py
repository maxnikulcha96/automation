"""Czech Republic MOI application status website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By


class MoiApplicationStatus(Website):
    def __init__(self, browser):
        """
        Initializes a new MoiApplicationStatus instance.

        :param browser: The browser instance.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://frs.gov.cz/cs/ioff/application-status"

        self.locators = {
            "application_number_input": (By.ID, 'edit-ioff-application-number'),
            "application_type_selectbox": (By.ID, 'edit-ioff-application-code'),
            "application_year": (By.ID, 'edit-ioff-application-year'),
            "submit_button": (By.ID, 'edit-submit-button'),
            "result_status_span": (By.XPATH, '//span[contains(@class,"alert alert-warning")]//strong')
        }

        Website.__init__(self, browser, self.url)

    def fill_application_details(self, number, type, year):
        self.browser.write_text(
            self.locators["application_number_input"], number)
        print("Filled application number: {}".format(number))

        self.browser.select_value_from_dropdown(
            self.locators["application_type_selectbox"], type)
        print("Choosen application type : {}".format(type))

        self.browser.select_value_from_dropdown(
            self.locators["application_year"], year)
        print("Choosen application year : {}".format(year))

    def click_submit_button(self):
        self.browser.click(self.locators["submit_button"])
        print("Clicked submit button")

    def get_result_status(self):
        return self.browser.get_element_text(self.locators["result_status_span"])

    def login(self):
        super().login()

    def logout(self):
        super().logout()
