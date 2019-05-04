# -*- coding: utf-8 -*-
import time

from audience_edit_locator import AudienceEditPageLocator
from . import BasePage


class AudienceEditPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.locator = AudienceEditPageLocator

    def get_time(self):
        return "%s" % time.time()

    def set_name(self, name):
        input_name = self.get_element_from_shadow_root(AudienceEditPageLocator.AUDIENCE_NAME_FILED_ROOT,
                                                       AudienceEditPageLocator.AUDIENCE_NAME_FILED)
        input_name.clear()
        for x in xrange(0, len(name)):
            input_name.send_keys(name[x])

    def click_save_btn(self):
        self.click_element(self.locator.SAVE_BTN)

    def get_name(self):
        return self.find_element(self.locator.HEADER).get_attribute('c-title')
