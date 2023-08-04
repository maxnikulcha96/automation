#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.sodexo import Sodexo


def setUp():
    global browser, website

    browser = FirefoxBrowser()
    website = Sodexo(browser)

    global email, password
    email = str(sys.argv[1])
    password = str(sys.argv[2])


def get_balance():
    balance = website.get_balance()
    print("The benefits balance is :{0}".format(balance))


def main():
    setUp()
    website.load()
    website.login(email, password)
    get_balance()
    browser.close()


if __name__ == "__main__":
    main()
