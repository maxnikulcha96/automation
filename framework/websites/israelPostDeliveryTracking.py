"""Israel Post delivery tracking website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By


class IsraelPostDeliveryTracking(Website):
    def __init__(self, browser):
        """
        Initializes a new IsraelPostDeliveryTracking instance.

        :param browser: The browser instance.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://israelpost.co.il/en/itemtrace"

        self.locators = {
            "item_code_input": (By.ID, "ItemCode"),
            "submit_button": (By.ID, "btn-ItemCode")
        }

        Website.__init__(self, browser, self.url)


    def __fill_item_number(self, item_number):
        self.browser.write_text(self.locators["item_code_input"], item_number)
        print("Filled item number: {0}".format(item_number))


    def __click_submit__button(self):
        self.browser.click(self.locators["submit_button"])
        print("Clicked submit button")


    def trace_item(self, item_number):
        self.__fill_item_number(item_number)
        self.__click_submit__button()
