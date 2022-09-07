"""Keren Hishtalmut website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class KerenHishtalmut(Website):
    def __init__(self, browser):
        """
        Initializes a new KerenHishtalmut instance.

        :param browser: The browser instance.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://online.as-invest.co.il/login"

        self.locators = {
            "israel_id_input": (By.XPATH, "//input[@formcontrolname='id']"),
            "phone_number": (By.XPATH, "//input[@formcontrolname='phoneNumber']"),
            "submit_button": (By.XPATH, "//button[@type='submit']"),
            "code_first_digit_unput": (By.XPATH, "//input[@title='שדה 1 מתוך 6']"),
            "code_second_digit_unput": (By.XPATH, "//input[@title='שדה 2 מתוך 6']"),
            "code_third_digit_unput": (By.XPATH, "//input[@title='שדה 3 מתוך 6']"),
            "code_fourth_digit_unput": (By.XPATH, "//input[@title='שדה 4 מתוך 6']"),
            "code_fifth_digit_unput": (By.XPATH, "//input[@title='שדה 5 מתוך 6']"),
            "code_sixth_digit_unput": (By.XPATH, "//input[@title='שדה 6 מתוך 6']"),
            "disapproval_button": (By.CLASS_NAME, "disapproval-button"),
            "total_amount_div": (By.CLASS_NAME, "total-amount"),
            "logout_span": (By.XPATH, "//button[@class='action']//span[text()='יציאה']"),
        }

        Website.__init__(self, browser, self.url)

    def __fill_israel_id(self, id):
        self.browser.write_text(self.locators["israel_id_input"], id)
        print("Filled Israel ID: {0}".format(id))

    def __fill_phone_number(self, number):
        self.browser.write_text(self.locators["phone_number"], number)
        print("Filled phone number: {0}".format(number))

    def __click_submit_button(self):
        self.browser.click(self.locators["submit_button"])
        print("Clicked submit button")

    def __fill_code(self):
        code = input("Enter code:")
        self.browser.write_text(
            self.locators["code_first_digit_unput"], code[0:1])
        self.browser.write_text(
            self.locators["code_second_digit_unput"], code[1:2])
        self.browser.write_text(
            self.locators["code_third_digit_unput"], code[2:3])
        self.browser.write_text(
            self.locators["code_fourth_digit_unput"], code[3:4])
        self.browser.write_text(
            self.locators["code_fifth_digit_unput"], code[4:5])
        self.browser.write_text(
            self.locators["code_sixth_digit_unput"], code[5:6])

        print("Filled code: {0}".format(code))

    def __click_disapproval_button(self):
        try:
            self.browser.click(self.locators["disapproval_button"])
            print("Clicked disapproval button")
        except NoSuchElementException:
            print("Unable to locate element: .disapproval-button")

    def login(self, id, phone):
        """
        Login the website.

        :param id: The login id.
        :param phone: The login phone number.
        """

        self.__fill_israel_id(id)
        self.__fill_phone_number(phone)
        self.__click_submit_button()
        self.__fill_code()
        self.__click_submit_button()
        self.__click_disapproval_button()

    def get_keren_amount(self):
        return self.browser.get_element_text(self.locators["total_amount_div"])

    def logout(self):
        self.browser.click(self.locators["logout_span"])
