from abc import ABC


class BaseWebsiteChecker(ABC):
    def __init__(self, website):
        self.website = website

    def check_title(self, expected_value):
        assert self.website.get_title() == expected_value
