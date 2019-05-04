# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class AudienceEditPageLocator(object):

    SAVE_BTN = (By.XPATH, '//*[@id="elm"]/c-page/c-header/c-button')
    HEADER = (By.TAG_NAME, 'c-header')
    BUTTON = (By.TAG_NAME, 'c-button')
    AUDIENCE_NAME_FILED_ROOT = (By.XPATH, '//*[@id="elm"]/c-page/div/div/div/div/div/div/c-input')
    AUDIENCE_NAME_FILED = (By.CSS_SELECTOR, 'div > div > input')
    PARAMETERS_TAB = (By.XPATH, '//*[@id="elm"]/c-page/c-tabs/c-tab-item[1]')
    COMPOSITION_TAB = (By.XPATH, '//*[@id="elm"]/c-page/c-tabs/c-tab-item[2]')
    NEXT_BTN_ROOT = (By.XPATH, '//*[@id="elm"]/c-page/c-tabs/c-tab-item[2]')
    NEXT_BTN = (By.CSS_SELECTOR, 'div > button')
    CALCULATE_BTN = (By.XPATH, '//*[@id="elm"]/c-page/div/div/div[2]/button')




