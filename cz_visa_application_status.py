#!/usr/bin/python

from datetime import datetime
import sys
from framework.checkers.checkers import BaseWebsiteChecker
from framework.web.browsers import FirefoxBrowser
from framework.websites.moiApplicationStatus import MoiApplicationStatus
from tests.baseTest import BaseTest


def setUp():
    global browser, website, checker, baseTest

    browser = FirefoxBrowser()
    website = MoiApplicationStatus(browser)
    checker = BaseWebsiteChecker(website)

    baseTest = BaseTest(browser, website)

    global person_name, application_number, application_type, application_year, screenshot_path
    person_name = str(sys.argv[1])
    application_number = str(sys.argv[2])
    application_type = str(sys.argv[3])
    application_year = str(sys.argv[4])
    screenshot_path = str(sys.argv[5])


def get_application_status():
    checker.check_title(
        "Informace o stavu řízení | Internetové objednávání pro cizince")

    website.fill_application_details(
        application_number, application_type, application_year)

    website.click_submit_button()

    status = website.get_result_status()

    print("{0}, the status of your application 'OAM-{1}/{2}-{3}' is '{4}'".format(
        person_name, application_number, application_type, application_year, status))

    browser.take_screenshot("{0}/{1}_OAM-{2}_{3}_{4}_{5}_{6}.png".format(
        screenshot_path, person_name, application_number, application_type, application_year, status, datetime.now()))


def main():
    setUp()
    baseTest.load()
    get_application_status()
    baseTest.tearDown()


if __name__ == "__main__":
    main()
