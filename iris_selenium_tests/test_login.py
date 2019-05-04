import pytest
from selenium.webdriver.support.wait import WebDriverWait

from iris_selenium_tests.fixtures import get_driver, login, test_session_id
from iris_selenium_tests.page_objects.login_page import LoginPage
from iris_selenium_tests.page_objects.sidebar_handler import SidebarHandler
from iris_selenium_tests.page_objects.sidebar_locators import SidebarPageLocator



@pytest.mark.parametrize('user', ['USER_RIGHTS', 'USER_NO_RIGHTS'])
def test_login_correct_credentials(test_session_id, get_driver, login, user):
    """
        Test_id: LOGIN_CORRECT_CREDENTIALS
        Preconditions:
          - URL of the application
        Test:
          - Open application Login url
          - Enter email and password
          - Click on Login
        Verification:
          - Check that we are on campaigns page
    """

    login(user)
    current_page = SidebarHandler(get_driver)
    current_page.wait_page_load(SidebarPageLocator.BUTTON_LOGOUT)
    assert get_driver.current_url.endswith("campaigns")


def test_login_wrong_credentials(get_driver, login):
    """
        Test_id: LOGIN_WRONG_CREDENTIALS
        Preconditions:
          - URL of the application
        Test:
          - Open application Login url
          - Enter email and password
          - Click on Login
        Verification:
          - Error message on the login page
    """
    login_page = LoginPage(get_driver)
    login('user@user.com:wrong_password')
    assert login_page.get_error_message() == "Wrong email or password."
    assert get_driver.current_url == "http://v2.iris-dev.cabestan.com/"
