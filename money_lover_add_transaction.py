#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.moneyLover import MoneyLover


def setUp():
    global browser, website

    browser = FirefoxBrowser(headless=False)
    website = MoneyLover(browser)

    global email, password, category, amount, note
    email = str(sys.argv[1])
    password = str(sys.argv[2])
    category = str(sys.argv[3])
    amount = str(sys.argv[4])
    note = str(sys.argv[5])


def add_transaction():
    website.add_transaction(category, amount, note)


def main():
    setUp()
    website.load()
    website.login_website(email, password)
    add_transaction()
    website.logout()
    browser.close()


if __name__ == "__main__":
    main()
