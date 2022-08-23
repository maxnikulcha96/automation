"""The base website implementation."""

from abc import ABC
import abc


class Website(ABC):
    def __init__(self, browser, url):
        """
        Initializes a new Website instance.

        :param browser: The browser conncetion.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = url

    def load(self):
        """
        Loads the website.
        """

        self.browser.load_url(self.url)

    def get_title(self):
        """
        Returns the title of the website.
        """

        return self.browser.get_title()

    # @abc.abstractmethod
    # def login(self):
    #     """
    #     Login the website.
    #     """

    #     print("Login website")

    @abc.abstractmethod
    def logout(self):
        """
        Logout the website.
        """

        print("Logout website")
