# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginPageLocator(object):
    TEXTBOX_EMAIL = (By.ID, 'username')
    TEXTBOX_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.CLASS_NAME, 'button')
    HEADER = (By.TAG_NAME, 'c-header')
    MSG_ERROR = (By.CLASS_NAME, 'signin-error')
    FORM_SIGNIN = (By.ID, 'signin_form')
