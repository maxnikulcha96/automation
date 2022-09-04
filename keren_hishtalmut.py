#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.kerenHishtalmut import KerenHishtalmut
from framework.checkers.checkers import BaseWebsiteChecker
from tests.baseTest import BaseTest


def setUp():
    global browser, website, checker, baseTest

    browser = FirefoxBrowser()
    website = KerenHishtalmut(browser)
    checker = BaseWebsiteChecker(website)

    baseTest = BaseTest(browser, website)

    global israel_id, phone_number
    israel_id = str(sys.argv[1])
    phone_number = str(sys.argv[2])


def get_keren_amount():
    checker.check_title("אלטשולר שחם - כניסה לאזור האישי")

    website.fill_israel_id(israel_id)

    website.fill_phone_number(phone_number)

    website.click_submit_button()

    code = input("Enter code:")
    website.fill_code(code)
    website.click_submit_button()

    website.click_disapproval_button()

    amount = website.get_keren_amount()
    print("The Keren Hishtalmut amount is :{0}".format(amount))


def main():
    setUp()
    baseTest.load()
    get_keren_amount()
    baseTest.tearDown()


if __name__ == "__main__":
    main()
