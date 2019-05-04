import pytest
from iris_selenium_tests.fixtures import get_driver, login
from iris_selenium_tests.page_objects.login_page import LoginPage
from iris_selenium_tests.page_objects.sidebar_handler import SidebarHandler


@pytest.mark.parametrize('user', ['USER_RIGHTS', 'USER_NO_RIGHTS'])
def test_sidebar_with_user(get_driver, login, user):
    """
        Test_id: SIDEBAR_USER_RIGHTS
        Preconditions:
          - URL of the application
        Test:
          - Open application Login url
          - Enter email and password
          - Click on Login
        Verification:
          - Check that we are on campaigns page
        if 'USER_RIGHTS'
          -check user Sidebard have module campagne available
        else
          - check user Sidebard have not module campagne
    """
    current_sidebar_handler = SidebarHandler(get_driver)

    if login(user= 'USER_RIGHTS'):
         assert current_sidebar_handler.get_campaign_element().text == "Campagnes"
    else:
        assert not current_sidebar_handler.get_campaign_element().text



