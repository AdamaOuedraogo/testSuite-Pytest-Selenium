# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from login_locators import LoginPageLocator
from selenium.webdriver.common.by import By
from iris_selenium_tests.page_objects import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        #self.driver = driver
        BasePage.__init__(self, driver)
        self.locator = LoginPageLocator

    def enter_email(self, email):
        self.find_element(self.locator.TEXTBOX_EMAIL).clear()
        self.find_element(self.locator.TEXTBOX_EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(self.locator.TEXTBOX_PASSWORD).clear()
        self.find_element(self.locator.TEXTBOX_PASSWORD).send_keys(password)

    def click_login(self):
        self.find_element(self.locator.BUTTON_LOGIN).click()

    def get_campaign_header(self):
        return self.find_element(self.locator.HEADER).get_attribute('c-title')

    def get_error_message(self):
        return self.find_element(self.locator.MSG_ERROR).text

    def check_login_page(self):
        try:
            self.find_element(self.locator.TEXTBOX_EMAIL)
        except NoSuchElementException:
            return False
        return True
    def get_connexion_element_text(self):
        return self.get_element(LoginPageLocator.BUTTON_LOGIN).text
