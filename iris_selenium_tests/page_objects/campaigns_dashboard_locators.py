# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CampaignsDashboardPageLocator(object):
    BUTTON = (By.TAG_NAME, 'c-button')
    NEW_CAMPAIGN_BTN = (By.XPATH, '//*[@id="elm"]/div/c-button')