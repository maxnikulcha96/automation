#!/usr/bin/python

from framework.web.browsers import FirefoxBrowser
from framework.websites.austriaEntryRequirements import AustriaEntryRequirements
from tests.baseTest import BaseTest


def setUp():
    global browser, website, baseTest

    browser = FirefoxBrowser()
    website = AustriaEntryRequirements(browser)

    baseTest = BaseTest(browser, website)


def get_entry_requirements():
    website.accept_cookies()
    website.get_entry_requirements()


def main():
    setUp()
    baseTest.load()
    get_entry_requirements()
    baseTest.tearDown()


if __name__ == "__main__":
    main()
