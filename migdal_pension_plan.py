#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.migdalPensionPlan import MigdalPensionPlan
from framework.checkers.checkers import BaseWebsiteChecker


def main():
    browser = FirefoxBrowser(headless=True, slowRun=True)
    page = MigdalPensionPlan(browser)
    checker = BaseWebsiteChecker(page)

    page.load()

    checker.check_title("כניסה למגדל שלי")

    israel_id = str(sys.argv[1])
    page.fill_israel_id(israel_id)
    page.click_submit_button()

    code = input("Enter code:")
    page.fill_code(code)
    page.click_submit_button()

    amount = page.get_pension_amount()
    print("The pension amount is :{0}".format(amount))

    # Execute logout script

    print("------------------------------------------------")

    browser.close()


main()
