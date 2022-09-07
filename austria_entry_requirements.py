#!/usr/bin/python

from framework.web.browsers import FirefoxBrowser
from framework.websites.austriaEntryRequirements import AustriaEntryRequirements


def setUp():
    global browser, website

    browser = FirefoxBrowser()
    website = AustriaEntryRequirements(browser)


def get_entry_requirements():
    website.get_entry_requirements()


def main():
    setUp()
    website.load()
    get_entry_requirements()
    browser.close()


if __name__ == "__main__":
    main()
