#!/usr/bin/python

from datetime import datetime
from framework.web.browsers import FirefoxBrowser
from framework.websites.georgeExchangeRate import GeorgeExchangeRate


def main():
    browser = FirefoxBrowser()
    website = GeorgeExchangeRate(browser)

    website.load()

    website.accept_only_essential_cookies()

    exchange_rate = website.get_today_exchange_rate()

    today = datetime.today().strftime('%Y-%m-%d')
    print("The EUR/CZK exchange rate on {0} is :{1}"
          .format(today, exchange_rate))

    print("------------------------------------------------")

    browser.close()


if __name__=="__main__":
    main()
