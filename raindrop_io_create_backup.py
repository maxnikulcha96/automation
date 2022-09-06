#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.raindropio import RaindropIO
from tests.baseTest import BaseTest


def setUp():
    global browser, website, baseTest

    browser = FirefoxBrowser()
    website = RaindropIO(browser)

    baseTest = BaseTest(browser, website)

    global email, password
    email = str(sys.argv[1])
    password = str(sys.argv[2])


def create_backup():
    website.login_website(email, password)

    website.create_backup()


def main():
    setUp()
    baseTest.load()
    create_backup()
    baseTest.tearDown()


if __name__ == "__main__":
    main()
