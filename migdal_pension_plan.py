#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.migdalPensionPlan import MigdalPensionPlan
from framework.checkers.checkers import BaseWebsiteChecker
from tests.baseTest import BaseTest


def setUp():
    global browser, website, checker, baseTest

    browser = FirefoxBrowser()
    website = MigdalPensionPlan(browser)
    checker = BaseWebsiteChecker(website)

    baseTest = BaseTest(browser, website)

    global israel_id
    israel_id = str(sys.argv[1])


def get_pension_amount():
    checker.check_title("כניסה למגדל שלי")

    website.fill_israel_id(israel_id)
    website.click_submit_button()

    code = input("Enter code:")
    website.fill_code(code)
    website.click_submit_button()

    amount = website.get_pension_amount()
    print("The pension amount is :{0}".format(amount))


def main():
    setUp()
    baseTest.load()
    get_pension_amount()
    baseTest.tearDown()


if __name__ == "__main__":
    main()
