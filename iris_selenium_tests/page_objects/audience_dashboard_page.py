# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from audience_dashboard_locator import AudiencePageLocator
from iris_selenium_tests.page_objects import BasePage


class AudienceDashboardPage(BasePage):
    # Audience Page Actions

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.locator = AudiencePageLocator

    def get_page_title(self):
        return self.driver.title

    def get_header_title(self):
        return self.get_element_from_shadow_root(AudiencePageLocator.C_HEADER_SR, AudiencePageLocator.HEADER_TITLE).text

    def get_container_title(self):
        return self.get_element(AudiencePageLocator.CONTAINER_TITLE).text

    # def find_search_result(self, search_result):
    #     return self.get_element(By.LINK_TEXT, search_result)
    #
    # def click_logout_btn(self):
    #     self.click_element(*AudiencePageLocator.LOGOUT_BTN)
    #
    # def get_head_table_audience(self):
    #     head_table = {}
    #     head_table['DATE'] = self.get_element(*AudiencePageLocator.HEAD_DATE).text
    #     head_table['NOM'] = self.get_element(*AudiencePageLocator.HEAD_NOM).text
    #     head_table['CREATEUR'] = self.get_element(*AudiencePageLocator.HEAD_CREATEUR).text
    #     head_table['STATUT'] = self.get_element(*AudiencePageLocator.HEAD_STATUT).text
    #     head_table['NB_CONTACT'] = self.get_element(*AudiencePageLocator.HEAD_NB_CONTACT).text
    #     return head_table


    def click_new_audience_button(self):
        self.click_element(AudiencePageLocator.NEW_AUDIENCE_BTN)
