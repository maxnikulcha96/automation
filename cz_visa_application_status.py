#!/usr/bin/python

import sys
from framework.checkers.checkers import BaseWebsiteChecker
from framework.web.browsers import FirefoxBrowser
from framework.websites.moiApplicationStatus import MoiApplicationStatus


def setUp():
    global browser, website, checker

    browser = FirefoxBrowser()
    website = MoiApplicationStatus(browser)
    checker = BaseWebsiteChecker(website)

    global person_name, application_number, application_type, application_year
    person_name = str(sys.argv[1])
    application_number = str(sys.argv[2])
    application_type = str(sys.argv[3])
    application_year = str(sys.argv[4])


def get_application_status():
    website.load()

    checker.check_title(
        "Informace o stavu řízení | Internetové objednávání pro cizince")

    website.fill_application_details(
        application_number, application_type, application_year)

    website.click_submit_button()

    status = website.get_result_status()

    print("{0}, the status of your application 'OAM-{1}/{2}-{3}' is '{4}'".format(
        person_name, application_number, application_type, application_year, status))


def tearDown():
    browser.close()

    print("------------------------------------------------")


def main():
    setUp()
    get_application_status()
    tearDown()


if __name__ == "__main__":
    main()
