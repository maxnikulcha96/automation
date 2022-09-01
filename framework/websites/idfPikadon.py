"""IDF Pikadon website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By


class IDFPikadon(Website):
    def __init__(self, browser):
        """
        Initializes a new IDFPikadon instance.

        :param browser: The browser instance.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://www.hachvana.mod.gov.il/mga/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:simple_login"

        self.locators = {
            "israel_id_input": (By.ID, "idnum"),
            "phone_number_input": (By.ID, "phone"),
            "submit_button": (By.ID, "login_btn"),
            "code_input": (By.ID, "otppswd"),
            "submit_code_button": (By.ID, "submitSms"),
            "pikadon_amount_div": (By.CLASS_NAME, "DepositBalanceText"),
        }

        Website.__init__(self, browser, self.url)

    def fill_israel_id(self, id):
        self.browser.write_text(self.locators["israel_id_input"], id)
        print("Filled Israel ID: {0}".format(id))

    def fill_phone_number(self, number):
        self.browser.write_text(self.locators["phone_number_input"], number)
        print("Filled phone number: {0}".format(number))

    def click_submit_button(self):
        self.browser.click(self.locators["submit_button"])
        print("Clicked submit button")

    def fill_code(self, code):
        self.browser.write_text(self.locators["code_input"], code)
        print("Filled code: {0}".format(code))

    def click_submit_code_button(self):
        self.browser.click(self.locators["submit_code_button"])
        print("Clicked submit code button")

    def open_pikadon_ampunt_page(self):
        self.browser.load_url(
            "https://www.hachvana.mod.gov.il/OnlineService/Pages/DepositsPayments.aspx")

    def get_pikadon_amount(self):
        return self.browser.get_element_text(self.locators["pikadon_amount_div"])

    def login(self):
        super().login()

    def logout(self):
        super().logout()
