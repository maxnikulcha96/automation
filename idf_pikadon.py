#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.idfPikadon import IDFPikadon
from framework.checkers.checkers import BaseWebsiteChecker


def main():
    browser = FirefoxBrowser()
    page = IDFPikadon(browser)
    checker = BaseWebsiteChecker(page)

    page.load()

    checker.check_title("הזדהות")

    israel_id = str(sys.argv[1])
    page.fill_israel_id(israel_id)

    phone_number = str(sys.argv[2])
    page.fill_phone_number(phone_number)

    page.click_submit_button()

    code = input("Enter code:")
    page.fill_code(code)
    page.click_submit_code_button()

    page.open_pikadon_ampunt_page()

    amount = page.get_pikadon_amount()
    print("The pikadon amount is :{0}".format(amount))

    # Execute logout script

    print("------------------------------------------------")

    browser.close()


main()
