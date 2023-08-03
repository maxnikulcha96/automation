#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.israelPostDeliveryTracking import IsraelPostDeliveryTracking


def setUp():
    global browser, website

    browser = FirefoxBrowser(headless=False)
    website = IsraelPostDeliveryTracking(browser)

    global item_number
    item_number = str(sys.argv[1])


def trace_item():
    website.trace_item(item_number)


def main():
    setUp()
    website.load()
    trace_item()
    website.logout()
    browser.close()


if __name__ == "__main__":
    main()