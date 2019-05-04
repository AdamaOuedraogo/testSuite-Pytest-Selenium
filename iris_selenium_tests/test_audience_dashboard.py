# -*- coding: utf-8 -*-
import pytest

from iris_selenium_tests.page_objects.audience_dashboard_locator import AudiencePageLocator
from iris_selenium_tests.page_objects.audience_dashboard_page import AudienceDashboardPage
from iris_selenium_tests.page_objects.sidebar_handler import SidebarHandler
from fixtures import login, get_driver


def test_check_audience_dashboard(get_driver, login):
    """
        Test_id: CHECK_AUDIENCE_DASHBOARD
        Preconditions:
            - URL of the application
        Test:
            - Open application Login URL
            - Enter email and password
            - Click on Login
            - Click on audience icon
        Verification:
            - Verify that audience dashboard page is displayed successfully
    """
    login()
    sidebar_handler = SidebarHandler(get_driver)
    sidebar_handler.navigate_to_audience_dashboard()
    audience_dashboard_page = AudienceDashboardPage(get_driver)
    assert audience_dashboard_page.get_page_title() == "Cabestan -- Reloaded"
    assert audience_dashboard_page.get_header_title() == "Audiences"
    assert audience_dashboard_page.get_container_title() == u"Dernières audiences"