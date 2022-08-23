#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.kerenHishtalmut import KerenHishtalmut
from framework.checkers.checkers import BaseWebsiteChecker


def main():
    browser = FirefoxBrowser()
    page = KerenHishtalmut(browser)
    checker = BaseWebsiteChecker(page)

    page.load()

    checker.check_title("אלטשולר שחם - כניסה לאזור האישי")

    israel_id = str(sys.argv[1])
    page.fill_israel_id(israel_id)

    phone_number = str(sys.argv[2])
    page.fill_phone_number(phone_number)

    page.click_submit_button()

    code = input("Enter code:")
    page.fill_code(code)
    page.click_submit_button()

    page.click_disapproval_button()

    amount = page.get_keren_amount()
    print("The Keren Hishtalmut amount is :{0}".format(amount))

    page.logout()

    print("------------------------------------------------")

    browser.close()


main()
