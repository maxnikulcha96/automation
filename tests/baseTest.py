"""Base test."""


class BaseTest():
    def __init__(self, browser, website):
        """
        Initializes a new BaseTest instance.

        :param browser: The browser instance.
        :param website: The website instance.
        """

        self.browser = browser
        self.website = website

    def load(self):
        self.website.load()
        self.website.login()

    def tearDown(self):
        self.website.logout()
        self.browser.close()

        print("------------------------------------------------")
