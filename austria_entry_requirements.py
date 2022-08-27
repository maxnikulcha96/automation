#!/usr/bin/python

from framework.web.browsers import FirefoxBrowser
from framework.websites.austriaEntryRequirements import AustriaEntryRequirements


def setUp():
    global browser, website

    browser = FirefoxBrowser()
    website = AustriaEntryRequirements(browser)


def get_entry_requirements():
    website.load()

    website.accept_cookies()

    website.get_entry_requirements()


def tearDown():
    website.logout()

    browser.close()

    print("------------------------------------------------")


def main():
    setUp()
    get_entry_requirements()
    tearDown()


if __name__ == "__main__":
    main()
