#!/usr/bin/python

import sys
from framework.web.browsers import FirefoxBrowser
from framework.websites.moiApplicationStatus import MoiApplicationStatus
from framework.checkers.moiApplicationStatusChecker import MoiApplicationStatusChecker


def main():
    browser = FirefoxBrowser(headless=True, slowRun=True)
    page = MoiApplicationStatus(browser)
    checker = MoiApplicationStatusChecker(page)

    page.load()

    checker.check_title(
        "Informace o stavu řízení | Internetové objednávání pro cizince")

    application_number = str(sys.argv[1])
    application_type = str(sys.argv[2])
    application_year = str(sys.argv[3])

    page.fill_application_details(
        application_number, application_type, application_year)

    page.click_submit_button()

    status = page.get_result_status()
    print("The status of your application 'OAM-{0}/{1}-{2}' is '{3}'".format(
        application_number, application_type, application_year, status))

    browser.close()


main()
