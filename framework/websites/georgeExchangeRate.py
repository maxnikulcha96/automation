"""George EUR/CZK exchange rate website."""

from datetime import datetime
from framework.web.website import Website
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class GeorgeExchangeRate(Website):
    def __init__(self, browser):
        """
        Initializes a new GeorgeExchangeRate instance.

        :param browser: The browser conncetion.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://www.csas.cz/cs/kurzovni-listek#/type/NONCASH/currency/EUR"

        self.today = datetime.today().strftime('%Y-%m-%d')

        self.locators = {
            "only_essential_cookies_button": (By.ID, 'popin_tc_privacy_button_2'),
            "today_exchange_rate_td": (By.XPATH, "//td[@data-testid='{0}-buy']".format(self.today))
        }

        Website.__init__(self, browser, self.url)

    def accept_only_essential_cookies(self):
        try:
            self.browser.click(self.locators["only_essential_cookies_button"])
            print("Clicked accept essential cookies only")
        except NoSuchElementException:
            print("Unable to locate element: #popin_tc_privacy_button_2")

    def get_today_exchange_rate(self):
        return self.browser.get_element_text(self.locators["today_exchange_rate_td"])

    def logout(self):
        super().logout()
