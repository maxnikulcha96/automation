#!/usr/bin/python

from datetime import datetime
from framework.web.browsers import FirefoxBrowser
from framework.websites.georgeExchangeRate import GeorgeExchangeRate
from tests.baseTest import BaseTest


def setUp():
    global browser, website, baseTest

    browser = FirefoxBrowser()
    website = GeorgeExchangeRate(browser)

    baseTest = BaseTest(browser, website)


def get_exchange_rate():
    exchange_rate = website.get_today_exchange_rate()

    today = datetime.today().strftime('%Y-%m-%d')
    print("The EUR/CZK exchange rate on {0} is :{1}"
          .format(today, exchange_rate))


def main():
    setUp()
    baseTest.load()
    get_exchange_rate()
    baseTest.tearDown()


if __name__ == "__main__":
    main()
