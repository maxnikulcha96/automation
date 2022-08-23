#!/usr/bin/python

from datetime import datetime
from framework.web.browsers import FirefoxBrowser
from framework.websites.georgeExchangeRate import GeorgeExchangeRate


def main():
    browser = FirefoxBrowser()
    page = GeorgeExchangeRate(browser)

    page.load()

    page.accept_only_essential_cookies()

    exchange_rate = page.get_today_exchange_rate()

    today = datetime.today().strftime('%Y-%m-%d')
    print("The EUR/CZK exchange rate on {0} is :{1}"
          .format(today, exchange_rate))

    print("------------------------------------------------")

    browser.close()


main()
