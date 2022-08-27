#!/usr/bin/python

from datetime import datetime
from webbrowser import get
from framework.web.browsers import FirefoxBrowser
from framework.websites.georgeExchangeRate import GeorgeExchangeRate


def setUp():
    global browser, website

    browser = FirefoxBrowser()
    website = GeorgeExchangeRate(browser)


def get_exchange_rate():
    website.load()

    website.accept_only_essential_cookies()

    exchange_rate = website.get_today_exchange_rate()

    today = datetime.today().strftime('%Y-%m-%d')
    print("The EUR/CZK exchange rate on {0} is :{1}"
          .format(today, exchange_rate))


def tearDown():
    browser.close()

    print("------------------------------------------------")


def main():
    setUp()
    get_exchange_rate()
    tearDown()


if __name__ == "__main__":
    main()
