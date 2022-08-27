#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.idfPikadon import IDFPikadon
from framework.checkers.checkers import BaseWebsiteChecker


def setUp():
    global browser, website, checker

    browser = FirefoxBrowser()
    website = IDFPikadon(browser)
    checker = BaseWebsiteChecker(website)

    global israel_id, phone_number
    israel_id = str(sys.argv[1])
    phone_number = str(sys.argv[2])


def get_pikadon_amount():
    website.load()

    checker.check_title("הזדהות")

    website.fill_israel_id(israel_id)

    website.fill_phone_number(phone_number)

    website.click_submit_button()

    code = input("Enter code:")
    website.fill_code(code)
    website.click_submit_code_button()

    website.open_pikadon_ampunt_website()

    amount = website.get_pikadon_amount()
    print("The pikadon amount is :{0}".format(amount))


def tearDown():
    website.logout()

    browser.close()

    print("------------------------------------------------")


def main():
    setUp()
    get_pikadon_amount()
    tearDown()


if __name__ == "__main__":
    main()
