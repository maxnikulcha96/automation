#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.migdalPensionPlan import MigdalPensionPlan
from framework.checkers.checkers import BaseWebsiteChecker


def main():
    browser = FirefoxBrowser()
    website = MigdalPensionPlan(browser)
    checker = BaseWebsiteChecker(website)

    website.load()

    checker.check_title("כניסה למגדל שלי")

    israel_id = str(sys.argv[1])
    website.fill_israel_id(israel_id)
    website.click_submit_button()

    code = input("Enter code:")
    website.fill_code(code)
    website.click_submit_button()

    amount = website.get_pension_amount()
    print("The pension amount is :{0}".format(amount))

    website.logout()

    print("------------------------------------------------")

    browser.close()


main()
