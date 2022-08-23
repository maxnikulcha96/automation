#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.kerenHishtalmut import KerenHishtalmut
from framework.checkers.checkers import BaseWebsiteChecker


def main():
    browser = FirefoxBrowser()
    website = KerenHishtalmut(browser)
    checker = BaseWebsiteChecker(website)

    website.load()

    checker.check_title("אלטשולר שחם - כניסה לאזור האישי")

    israel_id = str(sys.argv[1])
    website.fill_israel_id(israel_id)

    phone_number = str(sys.argv[2])
    website.fill_phone_number(phone_number)

    website.click_submit_button()

    code = input("Enter code:")
    website.fill_code(code)
    website.click_submit_button()

    website.click_disapproval_button()

    amount = website.get_keren_amount()
    print("The Keren Hishtalmut amount is :{0}".format(amount))

    website.logout()

    print("------------------------------------------------")

    browser.close()


main()
