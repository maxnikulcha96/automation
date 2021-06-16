from abc import ABC


class Website(ABC):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def load(self):
        self.browser.load_url(self.url)

    def get_title(self):
        return self.browser.get_title()
