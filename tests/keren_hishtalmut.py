#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.kerenHishtalmut import KerenHishtalmut


def setUp():
    global browser, website

    browser = FirefoxBrowser()
    website = KerenHishtalmut(browser)

    global israel_id, phone_number
    israel_id = str(sys.argv[1])
    phone_number = str(sys.argv[2])


def get_keren_amount():
    amount = website.get_keren_amount()
    print("The Keren Hishtalmut amount is :{0}".format(amount))


def main():
    setUp()
    website.load()
    website.login(israel_id, phone_number)
    get_keren_amount()
    website.logout()
    browser.close()


if __name__ == "__main__":
    main()
