#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.migdalPensionPlan import MigdalPensionPlan
from framework.checkers.checkers import BaseWebsiteChecker


def setUp():
    global browser, website, checker

    browser = FirefoxBrowser()
    website = MigdalPensionPlan(browser)
    checker = BaseWebsiteChecker(website)

    global israel_id
    israel_id = str(sys.argv[1])


def get_pension_amount():
    website.load()

    checker.check_title("כניסה למגדל שלי")

    website.fill_israel_id(israel_id)
    website.click_submit_button()

    code = input("Enter code:")
    website.fill_code(code)
    website.click_submit_button()

    amount = website.get_pension_amount()
    print("The pension amount is :{0}".format(amount))


def tearDown():
    website.logout()

    browser.close()

    print("------------------------------------------------")


def main():
    setUp()
    get_pension_amount()
    tearDown()


if __name__ == "__main__":
    main()
