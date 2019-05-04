import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from iris_selenium_tests.page_objects.audience_dashboard_page import AudienceDashboardPage
from iris_selenium_tests.page_objects.audience_edit_page import AudienceEditPage
from iris_selenium_tests.page_objects.login_page import LoginPage
from iris_selenium_tests.page_objects.sidebar_handler import SidebarHandler
import time
import uuid

@pytest.fixture(scope="session")
def test_session_id(request):
    test_session_id = uuid.uuid4()
    campaign = request.config.getoption("--campaign")
    if campaign is not None:
        test_session_id = campaign

    print "\n"
    print ">>>>>>>>>>>>>>>>>>>>>>>>>> TEST SESSION ID <<<<<<<<<<<<<<<<<<<<<<<<<<<"
    print ">>>>>>>>>>>>>>>>>>>>>>>>>> {} <<<<<<<<<<<<<<<<<<<<<<<<<<<".format(test_session_id)
    print ">>>>>>>>>>>>>>>>>>>>>>>>>> TEST SESSION ID <<<<<<<<<<<<<<<<<<<<<<<<<<<"
    return test_session_id


@pytest.fixture(scope="function")
def get_driver(request, test_session_id):
    """Fixture that will return a driver or a connector to the remote zalenium"""
    app_url = request.config.getoption("--app-url")
    driver = request.config.getoption("--driver")
    remote = request.config.getoption("--remote")
    zalenium_hub_url = request.config.getoption("--zalenium-hub")

    # Retrieving the Function name (test function name)
    # Adding test name in capability so that it will appear in zalenium
    test_function_name = request.function.func_name
    DesiredCapabilities.CHROME.update({"name": "{}-{}".format(test_session_id, test_function_name),
                                       "recordVideo": True})

    if remote == True:
        #current_driver= webdriver.Chrome()
        if driver =='chrome':
            current_driver = webdriver.Remote(
            command_executor= zalenium_hub_url,
            desired_capabilities=DesiredCapabilities.CHROME)
        else :
            current_driver = webdriver.Remote(
            command_executor=zalenium_hub_url,
            desired_capabilities=DesiredCapabilities.FIREFOX)
        current_driver.get(app_url)
        current_driver.maximize_window()
        return current_driver
    else:
        if driver == 'chrome':
            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument(kiosk)
            # chrome_options.add_argument(app)
            # chrome_options.add_argument(disable_infobars)
            # current_driver = webdriver.Chrome(chrome_options=chrome_options)
            current_driver = webdriver.Chrome()
            current_driver.get(app_url)
            current_driver.implicitly_wait(10)
            WebDriverWait(current_driver, 30)
            return current_driver



@pytest.fixture(scope="function")
def login(request, get_driver):
    """ This fixture helps to log in as a user"""
    # As this fixture needs parameters, we need to create a function in it
    # And return the function
    def login_with_user(user='USER_RIGHTS'):
        credentials = os.environ.get(user, None)
        if credentials is not None:
            user, password = os.environ[user].split(':')
        else:
            user, password = user.split(':')

        current_page = LoginPage(get_driver)
        current_page.enter_email(user)
        current_page.enter_password(password)
        current_page.click_login()

        def final():
            get_driver.close()
        request.addfinalizer(final)
    return login_with_user

@pytest.fixture(scope="function")
def logout(request, get_driver,login):
    """ This fixture helps to logout as a user"""
    def logout_with_right_user():
        sidebar = SidebarHandler(get_driver)
        sidebar.click_logout()
    return logout_with_right_user


@pytest.fixture(scope='function')
def audience_create(request, get_driver, login):

    def audience_creation(audience_name=None):
        if audience_name is None:
            audience_name = 'TESTAUTO-AUDIENCE-' + "%s" % time.time()
        login()
        sidebar_handler = SidebarHandler(get_driver)
        sidebar_handler.navigate_to_audience_dashboard()
        audience_dashboard_page = AudienceDashboardPage(get_driver)
        audience_dashboard_page.click_new_audience_button()
        audience_edit_page = AudienceEditPage(get_driver)
        audience_edit_page.set_name(audience_name)
        audience_edit_page.click_save_btn()
        return audience_name

    return audience_creation    

