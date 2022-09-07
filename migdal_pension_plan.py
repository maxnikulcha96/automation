#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.migdalPensionPlan import MigdalPensionPlan


def setUp():
    global browser, website

    browser = FirefoxBrowser()
    website = MigdalPensionPlan(browser)

    global israel_id
    israel_id = str(sys.argv[1])


def get_pension_amount():
    amount = website.get_pension_amount()
    print("The pension amount is :{0}".format(amount))


def main():
    setUp()
    website.load()
    website.login(israel_id)
    get_pension_amount()
    website.logout()
    browser.close()


if __name__ == "__main__":
    main()
