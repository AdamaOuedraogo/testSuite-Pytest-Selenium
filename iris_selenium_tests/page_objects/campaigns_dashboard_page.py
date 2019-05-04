from campaigns_dashboard_locators import CampaignsDashboardPageLocator


class CampaignsDashboardPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.locator = CampaignsDashboardPageLocator

    def click_element(self, locator):
        self.find_element(locator).click()


    def click_new_campaign_btn(self):
        self.click_element(*self.locator.NEW_CAMPAIGN_BTN)
