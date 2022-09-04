#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.sodexo import Sodexo
from tests.baseTest import BaseTest


def setUp():
    global browser, website, checker, baseTest

    browser = FirefoxBrowser()
    website = Sodexo(browser)

    baseTest = BaseTest(browser, website)

    global email, password
    email = str(sys.argv[1])
    password = str(sys.argv[2])


def get_balance():
    website.accept_cookies()

    website.login_website(email, password)

    balance = website.get_balance()
    print("The benefits balance is :{0}".format(balance))

def main():
    setUp()
    baseTest.load()
    get_balance()
    baseTest.tearDown()


if __name__ == "__main__":
    main()
