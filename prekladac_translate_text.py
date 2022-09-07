#!/usr/bin/python

from framework.web.browsers import FirefoxBrowser
from framework.websites.prekladac import Prekladac
from tests.baseTest import BaseTest


def setUp():
    global browser, website, baseTest

    browser = FirefoxBrowser()
    website = Prekladac(browser)

    baseTest = BaseTest(browser, website)


def translate_text():
    src_lang = input("Enter source language:")
    text_to_translate = input("Enter text to translate:")
    dest_lang = input("Enter destination language:")

    result = website.translate_text(src_lang, text_to_translate, dest_lang)
    print("The translation is :{0}".format(result))


def main():
    setUp()
    baseTest.load()
    translate_text()
    baseTest.tearDown()


if __name__ == "__main__":
    main()
