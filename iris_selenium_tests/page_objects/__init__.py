from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

EXPLICIT_BROWSER_TIMEOUT = 30


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

#check the presence of element before return this element if is visible
    def get_element(self, locator):
        if WebDriverWait(self.driver, EXPLICIT_BROWSER_TIMEOUT).until(
            expected_conditions.presence_of_element_located(locator)):
            return WebDriverWait(self.driver, EXPLICIT_BROWSER_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.get_element(locator)

    def click_element(self, locator):
        self.get_element(locator).click()

    def expand_shadow_element(self, element):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def get_element_from_shadow_root(self, locator1, locator2):

        root = self.get_element(locator1)
        sr = self.expand_shadow_element(root)
        return sr.find_element_by_css_selector(locator2[1])
    def wait_page_load(self, locator):
        WebDriverWait(self.driver, EXPLICIT_BROWSER_TIMEOUT).until(
            expected_conditions.visibility_of_element_located(locator))

