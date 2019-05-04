import json
import time


class Common(object):

    def __init__(self, driver):
        self.driver = driver

    def read_file(self, path, key):
        FILE_PATH = path
        with open(FILE_PATH) as data_file:
            CONFIG = json.load(data_file)
            value = CONFIG[key]
            return value

    def get_browser(self, path='resources/configs/local.json', key='browser'):
        return Common.read_file(path, key)

    def get_url(self, path='resources/configs/local.json', key='url'):
        return Common.read_file(path, key)

    def navigate(self, address):
        self.driver.get(address)


    def open_iris(self, path, key):
        base_url = Common.read_file(path, key)
        Common.navigate(base_url)

    def fill(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click_element(self, locator):
        self.find_element(locator).click()

    def get_page_title(self):
        return self.driver.title

    def delayby(self, seconds):
        time.sleep(seconds)

    def get_time(self):
        return "%s" % time.time()

    def expand_shadow_element(self, element):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def write_to_file(self, path, content):
        f = open(path, 'w')
        f.write(content)
        f.close()

    def read_from_file(self, path):
        f = open(path, "r")
        return f.read()

