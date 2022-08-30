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


def test():
    website.load()

    website.login_website(email, password)

    website.open_backups_page()

    website.click_create_new_backup()

    website.go_back_to_main_page()


def tearDown():
    website.logout()

    print("------------------------------------------------")


def main():
    setUp()
    test()
    tearDown()


if __name__ == "__main__":
    main()
