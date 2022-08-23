#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.idfPikadon import IDFPikadon
from framework.checkers.checkers import BaseWebsiteChecker


def main():
    browser = FirefoxBrowser()
    website = IDFPikadon(browser)
    checker = BaseWebsiteChecker(website)

    website.load()

    checker.check_title("הזדהות")

    israel_id = str(sys.argv[1])
    website.fill_israel_id(israel_id)

    phone_number = str(sys.argv[2])
    website.fill_phone_number(phone_number)

    website.click_submit_button()

    code = input("Enter code:")
    website.fill_code(code)
    website.click_submit_code_button()

    website.open_pikadon_ampunt_website()

    amount = website.get_pikadon_amount()
    print("The pikadon amount is :{0}".format(amount))

    website.logout()

    print("------------------------------------------------")

    browser.close()


if __name__=="__main__":
    main()
