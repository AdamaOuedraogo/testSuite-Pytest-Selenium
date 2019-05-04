# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class CampaignEditPageLocator(object):
    SAVE_BTN = (By.XPATH, '//*[@id="elm"]/c-page/c-header/c-button[2]')
    LAUNCH_BTN =(By.XPATH, '//*[@id="elm"]/c-page/c-header/c-button[1]')

    ROOT_NAME = (By.TAG_NAME, 'c-input')
    TEXTBOX_NAME = (By.CLASS_NAME, 'input')
    HEADER = (By.TAG_NAME, 'c-header')
    TAB_SCENARIO = (By.CSS_SELECTOR, '#elm > c-page > c-tabs > c-tab-item:nth-child(2)')