"""Money Lover website."""

from nis import cat
from framework.web.website import Website
from selenium.webdriver.common.by import By


class MoneyLover(Website):
    def __init__(self, browser):
        """
        Initializes a new MoneyLover instance.

        :param browser: The browser instance.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://web.moneylover.me/"

        active_div = '//div[contains(@class,"active")]'

        self.locators = {
            "login_email_input": (By.ID, "input-26"),
            "login_password_input": (By.ID, "input-28"),
            "login_button": (By.XPATH, '//button[contains(@class,"btn-submit")]'),
            "add_transaction_button": (By.XPATH, '//button[contains(@class,"add-tran")]'),
            "open_category_div": (By.XPATH, '{0}//div[contains(@class,"v-card__text transaction-content")]//span[contains(text(),"Vybrat kategorii")]'.format(active_div)),
            "category_search_input": (By.ID, "input-search-focus"),
            "amount_input": (By.XPATH, '{0}//div[contains(@class,"flex xs4 amount")]//input'.format(active_div)),
            "note_input": (By.XPATH, '{0}//input[@id="note"]'.format(active_div)),
            "save_transaction_button": (By.XPATH, '{0}//button[contains(@class,"action-btn done")]//span[contains(text(),"Uložit")]'.format(active_div)),
            "menu_button": (By.ID, "Icons/account/ic_account"),
            "menu_my_accout_item": (By.XPATH, '//div[contains(@class,"menu-item")]//span[contains(text(),"Můj účet")]'),
            "signout_span": (By.XPATH, '//span[contains(@class,"singout")]'),
            "web_browser_logout_span": (By.XPATH, '//div[contains(@class,"remove-device")]/preceding-sibling::div/span[contains(text(),"Web Browser")]'),
            "logout_success_span": (By.XPATH, '//span[contains(text(),"Logout Success")]')
        }

        Website.__init__(self, browser, self.url)

    def login_website(self, email, password):
        self.browser.write_text(self.locators["login_email_input"], email)
        self.browser.write_text(
            self.locators["login_password_input"], password)

        self.browser.click(self.locators["login_button"])
        print("Clicked login button")

    def __click_add_transaction(self):
        self.browser.wait(15)

        self.browser.click(self.locators["add_transaction_button"])
        print("Clicked 'add transaction' button")

    def __get_category_div_selector_by_text(self, category):
        return (By.XPATH, '//div[contains(@id,"tab-2")]//div[contains(@class,"category-name") and contains(text(),"{0}")]'.format(category))

    def __fill_category(self, category):
        self.browser.click(self.locators["open_category_div"])
        print("Clicked 'select categoty'")

        self.browser.write_text(
            self.locators["category_search_input"], category)

        self.browser.click(self.__get_category_div_selector_by_text(category))
        print("Selected category: '{0}'".format(category))

    def __fill_amount(self, amount):
        self.browser.write_text(
            self.locators["amount_input"], amount)

    def __fill_note(self, note):
        self.browser.write_text(
            self.locators["note_input"], note)

    def __click_save_transaction(self):
        self.browser.click(self.locators["save_transaction_button"])
        print("Clicked 'save transaction' button")

    def add_transaction(self, category, amount, note):
        self.__click_add_transaction()

        self.__fill_category(category)
        self.__fill_amount(amount)
        self.__fill_note(note)
        self.__click_save_transaction()

    def login(self):
        super().login()

    def logout(self):
        self.browser.click(self.locators["menu_button"])
        self.browser.click(self.locators["menu_my_accout_item"])

        # elements = self.browser.find_elements(
        #     self.locators["web_browser_logout_span"])
        # for elem in elements:
        #     self.browser.click(elem)

        self.browser.click(self.locators["signout_span"])

        print("Logout Money Lover")
