#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.raindropio import RaindropIO


def setUp():
    global browser, website

    browser = FirefoxBrowser()
    website = RaindropIO(browser)

    global email, password
    email = str(sys.argv[1])
    password = str(sys.argv[2])


def create_backup():
    website.create_backup()


def main():
    setUp()
    website.load()
    website.login(email, password)
    create_backup()
    website.logout()
    browser.close()


if __name__ == "__main__":
    main()
