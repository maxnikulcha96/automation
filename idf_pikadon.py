#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.idfPikadon import IDFPikadon


def setUp():
    global browser, website

    browser = FirefoxBrowser()
    website = IDFPikadon(browser)

    global israel_id, phone_number
    israel_id = str(sys.argv[1])
    phone_number = str(sys.argv[2])


def get_pikadon_amount():
    amount = website.get_pikadon_amount()
    print("The pikadon amount is :{0}".format(amount))


def main():
    setUp()
    website.load()
    website.login(israel_id, phone_number)
    get_pikadon_amount()
    browser.close()


if __name__ == "__main__":
    main()
