"""The base checkers implementation."""

from abc import ABC


class BaseWebsiteChecker(ABC):
    def __init__(self, website):
        """
        Initializes a new BaseWebsiteChecker instance.

        :param website: The website to check.
        """

        self.website = website

    def check_title(self, expected_value):
        """
        Validates that the title of the websites is equals to the expected value.

        :param expected_value: The expected title of the website.
        """

        assert self.website.get_title() == expected_value
