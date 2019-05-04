# -*- coding: utf-8 -*-
import pyautogui


from campaign_edit_locators import CampaignEditPageLocator
from iris_selenium_tests.methods.common import Common


class CampaignEditPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.locator = CampaignEditPageLocator

    def click_element(self, locator):
        self.find_element(locator).click()

    def expand_shadow_element(self, element):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def get_element(self, locator):
        return self.find_element(locator)

    def get_element_from_shadow_root(self, locator1, locator2):
        root = self.get_element(locator1)
        sr = self.expand_shadow_element(root)
        return sr.find_element_by_css_selector(locator2[1])

    def click_save_btn(self):
        self.click_element(self.locator.SAVE_BTN)

    def click_scenario_tab(self):
        self.find_element(self.locator.TAB_SCENARIO).click()

    def click_parameter_tab(self):
        pass

    def click_launch_btn(self):
        pass


    def set_name(self, name):

        input_name = self.get_element_from_shadow_root('c-input', ".input")
        input_name.clear()
        Common.delayby(2)
        for x in xrange(0, len(name)):
            input_name.send_keys(name[x])

    def get_name(self):
        return self.find_element(self.locator.HEADER).get_attribute('c-title')

    def expand_collapser(self, type):
        Common.delayby(2)
        collapser_list = self.find_elements_by_tag_name('c-collapser-panel')
        collapser = None
        for x in xrange(0, len(collapser_list)):
            if type == collapser_list[x].get_attribute('c-title'):
                collapser = collapser_list[x]
        shadow_root = world.functions_library.expand_shadow_element(collapser)
        shadow_root.find_element_by_css_selector('div > div.collapser-panel-title').click()

    def drag_n_drop_first_element_to_board(self, element):
        world.functions_library.delayby(2)
        drop_board_location = self.find_element_by_class_name('page-container').location
        root_list = self.find_elements_by_tag_name('c-campaign-component')
        root_1 = None
        if element == 'target':
            for x in xrange(0, len(root_list)):
                if root_list[x].get_attribute('type') == 'source-audience':
                    root_1 = root_list[x]
        if element == 'email':
            for x in xrange(0, len(root_list)):
                if root_list[x].get_attribute('type') == 'channel-email':
                    root_1 = root_list[x]
        shadow_root_1 = world.functions_library.expand_shadow_element(root_1)
        root_2 = shadow_root_1.find_element_by_css_selector('div > div > c-campaign-icon')
        shadow_root_2 = world.functions_library.expand_shadow_element(root_2)
        icon_to_drag = shadow_root_2.find_element_by_css_selector('div > div > c-icon')
        pyautogui.mouseDown(icon_to_drag.location['x'], icon_to_drag.location['y'], button='left')
        world.functions_library.delayby(1)
        pyautogui.dragTo(drop_board_location['x'] * 2 + 50, drop_board_location['y'] * 2 + 180, duration=0.5)
        pyautogui.mouseUp(drop_board_location['x'] * 2 + 50, drop_board_location['y'] * 2 + 180, button='left')

    def drag_n_drop_second_element_to_first(self, element_1, element_2):
        world.functions_library.delayby(2)
        drop_board_location = self.find_element_by_class_name('page-container').location
        root_list = self.find_elements_by_tag_name('c-campaign-component')
        if element_1 == 'target':
            for x in xrange(0, len(root_list)):
                if root_list[x].get_attribute('type') == 'source-audience':
                    root_1 = root_list[x]
        if element_1 == 'email':
            for x in xrange(0, len(root_list)):
                if root_list[x].get_attribute('type') == 'channel-email':
                    root_1 = root_list[x]
        shadow_root_1 = world.functions_library.expand_shadow_element(root_1)
        root_2 = shadow_root_1.find_element_by_css_selector('div > div > c-campaign-icon')
        shadow_root_2 = world.functions_library.expand_shadow_element(root_2)
        icon_to_drag = shadow_root_2.find_element_by_css_selector('div > div > c-icon')
        pyautogui.mouseDown(icon_to_drag.location['x'], icon_to_drag.location['y'], button='left')
        pyautogui.moveTo(drop_board_location['x'] * 2 + 50, drop_board_location['y'] * 2 + 300, duration=1)
        world.functions_library.delayby(2)
        if element_2 == 'target':
            icon_to_drop = self.find_element_by_class_name('graph__branch__dep__card__right')
            pyautogui.dragTo(icon_to_drop.location['x'] + 50, icon_to_drop.location['y'], duration=0.5)
            pyautogui.mouseUp(icon_to_drop.location['x'] + 50, icon_to_drop.location['y'], button='left')
        if element_2 == 'email':
            icon_to_drop = self.find_element_by_class_name('graph__branch__dep__card__left')
            pyautogui.dragTo(icon_to_drop.location['x'], icon_to_drop.location['y'], duration=0.5)
            pyautogui.mouseUp(icon_to_drop.location['x'], icon_to_drop.location['y'], button='left')

    def get_button_status(self, element):
        world.functions_library.delayby(2)
        buttons = self.find_elements(self.locator.BUTTON)
        i = 0
        while i < len(buttons):
            if element == 'saved':
                if buttons[i].text.encode('utf-8') == "Enregistré":
                    return True
            i += 1
        return False

    def navigate_tab(self, element):
        if element == 'scenario':
            self.find_element(self.locator.TAB_SCENARIO).click()




    def confirmation_popup_handler(self):
        pass
