# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class SidebarPageLocator(object):
    LOGO_AUDIENCE = (By.CLASS_NAME, 'audience')
    LOGO_CONTENT = (By.CLASS_NAME, 'content')
    LOGO_CAMPAIGN = (By.CLASS_NAME, 'camp')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, '#elm > div > div.sidebar-footer > a > div.sidebar-link-icon > span')

