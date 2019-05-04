# -*- coding: utf-8 -*-
import pytest

from iris_selenium_tests.page_objects.login_page import LoginPage
from iris_selenium_tests.page_objects.sidebar_handler import SidebarHandler
from fixtures import login, get_driver, logout


def test_logout(get_driver, login, logout):
    """
        Test_id: LOGOUT_FROM_IRIS_APP
        Preconditions:
          - URL of the application
        Test:
          - Click on Deconnexion in the sidebar
        Verification:
          - verify the presence of connexion button
          - verify current url is http://v2.iris-dev.cabestan.com/
    """
    login()
    logout()
    current_loginpage = LoginPage(get_driver)
    assert current_loginpage.get_connexion_element_text() =="Connexion"