"""Překladač website."""

from framework.web.website import Website
from selenium.webdriver.common.by import By


class Prekladac(Website):
    def __init__(self, browser):
        """
        Initializes a new Prekladac instance.

        :param browser: The browser instance.
        :param url: The URL of the website.
        """

        self.browser = browser
        self.url = "https://www.prekladac.cz"

        self.locators = {
            "accept_cookies_button": (By.XPATH, '//button[contains(@class,"fc-cta-consent")]'),
            "lang_from_select": (By.ID, "lang_from"),
            "from_textarea": (By.ID, "from_text"),
            "lang_to_select": (By.ID, "lang_to"),
            "translate_button": (By.XPATH, '//input[contains(@class,"pull-right translate_string")]'),
            "translation_result_div": (By.ID, "result")
        }

        Website.__init__(self, browser, self.url)

    def __accept_cookies(self):
        self.browser.click(self.locators["accept_cookies_button"])
        print("Clicked 'accept cookies' button")

    def __select_source_language(self, source_lang):
        self.browser.select_item_from_dropdown_by_value(
            self.locators["lang_from_select"], source_lang)
        print("Choosen source language : {0}".format(source_lang))

    def __enter_source_text(self, source_text):
        self.browser.write_text(
            self.locators["from_textarea"], source_text)
        print("Filled source text: {0}".format(source_text))

    def __select_destination_language(self, dest_lang):
        self.browser.select_item_from_dropdown_by_value(
            self.locators["lang_to_select"], dest_lang)
        print("Choosen destination language : {0}".format(dest_lang))

    def __click_translate_button(self):
        self.browser.click(self.locators["translate_button"])
        print("Clicked 'translate' button")

    def __get_translation(self):
        return self.browser.get_element_text(self.locators["translation_result_div"])

    def translate_text(self, src_lang, text_to_translate, dest_lang):
        from time import sleep

        self.__accept_cookies()

        self.__select_source_language(src_lang)
        self.__enter_source_text(text_to_translate)
        self.__select_destination_language(dest_lang)
        self.__click_translate_button()

        sleep(5)

        return self.__get_translation()
