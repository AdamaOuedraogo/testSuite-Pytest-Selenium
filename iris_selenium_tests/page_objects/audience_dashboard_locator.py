# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By



class AudiencePageLocator(object):
    # Audience Page Locators


    NEW_AUDIENCE_BTN = (By.XPATH, '//*[@id="elm"]/div/c-button')
    CONTAINER_TITLE = (By.XPATH, '//*[@id="elm"]/div/c-title')
    LOGOUT_BTN = (By.XPATH, '//*[@id="elm"]/div/div[3]/a')
    HEAD_DATE = (By.XPATH, '//*[@id="elm"]/div/c-table/c-table-row[1]/c-table-cell[1]/c-text')
    HEAD_NOM = (By.XPATH, '//*[@id="elm"]/div/c-table/c-table-row[1]/c-table-cell[2]/c-text')
    HEAD_CREATEUR = (By.XPATH, '//*[@id="elm"]/div/c-table/c-table-row[1]/c-table-cell[3]/c-text')
    HEAD_NB_CONTACT = (By.XPATH, '//*[@id="elm"]/div/c-table/c-table-row[1]/c-table-cell[4]/c-text')
    HEAD_STATUT = (By.XPATH, '//*[@id="elm"]/div/c-table/c-table-row[1]/c-table-cell[5]/c-text')

    #manage shadow_root
    C_HEADER_SR = (By.CSS_SELECTOR, '#elm > c-header')
    HEADER_TITLE = (By.CSS_SELECTOR, 'header > div.header-inner.header-left > h1')






