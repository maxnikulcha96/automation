#!/usr/bin/python

import sys
from datetime import datetime
from framework.checkers.checkers import BaseWebsiteChecker
from framework.web.browsers import FirefoxBrowser
from framework.websites.moiApplicationStatus import MoiApplicationStatus


def main():
    browser = FirefoxBrowser(headless=True, slowRun=True)
    page = MoiApplicationStatus(browser)
    checker = BaseWebsiteChecker(page)

    page.load()

    checker.check_title(
        "Informace o stavu řízení | Internetové objednávání pro cizince")

    person_name = str(sys.argv[1])
    application_number = str(sys.argv[2])
    application_type = str(sys.argv[3])
    application_year = str(sys.argv[4])

    page.fill_application_details(
        application_number, application_type, application_year)

    page.click_submit_button()

    status = page.get_result_status()

    # browser.take_screenshot("{0}_OAM-{1}_{2}_{3}_{4}_{5}.png".format(
    #     person_name, application_number, application_type, application_year, status, datetime.now()))

    print("{0}, the status of your application 'OAM-{1}/{2}-{3}' is '{4}'".format(
        person_name, application_number, application_type, application_year, status))

    print("------------------------------------------------")

    browser.close()


main()
