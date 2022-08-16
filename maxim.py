from framework.web.browsers import SafariBrowser, FirefoxBrowser
from framework.websites.moiApplicationStatus import MoiApplicationStatus
from framework.checkers.moiApplicationStatusChecker import MoiApplicationStatusChecker

application_number = "29159"
application_type = "DP"
application_year = "2022"

# browser = SafariBrowser(slowRun=True)
browser = FirefoxBrowser(headless=True, slowRun=True)
page = MoiApplicationStatus(browser)
checker = MoiApplicationStatusChecker(page)

page.load()

checker.check_title(
    "Informace o stavu řízení | Internetové objednávání pro cizince")

page.fill_application_details(
    application_number, application_type, application_year)
page.click_submit_button()

status = page.get_result_status()
print("The status of your application 'OAM-{0}/{1}-{2}' is '{3}'".format(
    application_number, application_type, application_year, status))

browser.close()
