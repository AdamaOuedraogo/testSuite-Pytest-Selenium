# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from iris_selenium_tests.methods.functions_library import *
from sidebar_locators import SidebarPageLocator
from iris_selenium_tests.page_objects import BasePage


class SidebarHandler(BasePage):

    def __init__(self, driver):
        #self.driver = driver
        BasePage.__init__(self,driver)
        self.locator = SidebarPageLocator

    def click_element(self, locator):
        self.find_element(locator).click()

    # def check_campaign_existence(self):
    #     try:
    #         self.find_element(self.locator.LOGO_CAMPAIGN)
    #     except NoSuchElementException:
    #         return False
    #     return True


    def get_campaign_element(self):
        return self.get_element(self.locator.LOGO_CAMPAIGN)

    def click_logout(self):
        self.click_element(self.locator.BUTTON_LOGOUT)

    def navigate_to_audience_dashboard(self):
        self.find_element(self.locator.LOGO_AUDIENCE).click()


    def navigate_to_content_dashboard(self):
        self.find_element(self.locator.LOGO_CONTENT).click()

    def navigate_to_campaign_dashboard(self):
        self.find_element(self.locator.LOGO_CAMPAIGN).click()
