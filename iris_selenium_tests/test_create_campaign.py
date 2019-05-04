from iris_selenium_tests.fixtures import campaign_name
from iris_selenium_tests.tests.check.campaign_page_check import CampaignPageTest
from iris_selenium_tests.page_objects.campaigns_dashboard_page import CampaignsDashboardPage
from iris_selenium_tests.page_objects.campaign_edit_page import CampaignEditPage


def test_create_campaign_without_scenario(get_driver, login, campaign_name):
    """
        Test_id: CREATE_CAMPAIGN_WITHOUT_SCENARIO
        Preconditions:
          - URL of the application
        Test:
          - As a user with full rights connected to Iris
          - User clicks on new campaign button
          - User sets new campaign's name and save the campaign
        Verification:
          - Check that the campaign is created
    """
    login()
    current_campaign_dashboard_page = CampaignsDashboardPage(get_driver)
    current_campaign_dashboard_page.click_new_campaign_btn()
    current_campaign_edit_page = CampaignEditPage(get_driver)
    current_campaign_edit_page.set_name(campaign_name)
    current_campaign_edit_page.click_save_btn()
    CampaignPageTest.check_campaign_is_saved()





    assert True


def test_create_campaign_and_set_secenario_email_to_target(get_driver, login):
    """
        Test_id: CREATE_CAMPAIGN_WITH_SCENARIO_EMAIL_TO_TARGET
        Preconditions:
          - URL of the application
        Test:
          - As a user with full rights connected to Iris
          - User clicks on new campaign button
          - User sets new campaign's name
          - User sets scenario by drag and drop target before email
          - User saves the campaign
        Verification:
          - Check that the campaign is created
    """
    login()
    current_campaign_dashboard_page = CampaignsDashboardPage(get_driver)
    current_campaign_dashboard_page.click_new_campaign_btn()
    current_campaign_edit_page = CampaignEditPage(get_driver)
    current_campaign_edit_page.set_name(campaign_name)
    current_campaign_edit_page.click_scenario_tab()
    current_campaign_edit_page.drag_n_drop_second_element_to_first("target","email")
    current_campaign_edit_page.click_save_btn()
    CampaignPageTest.check_campaign_is_saved()



def test_create_campaign_and_set_secenario_target_to_email(get_driver, login):
    """
        Test_id: CREATE_CAMPAIGN_WITH_SCENARIO_EMAIL_TO_TARGET
        Preconditions:
          - URL of the application
        Test:
          - As a user with full rights connected to Iris
          - User clicks on new campaign button
          - User sets new campaign's name
          - User sets scenario by drag and drop email before target
          - User saves the campaign
        Verification:
          - Check that the campaign is created
    """
    login()
    current_campaign_dashboard_page = CampaignsDashboardPage(get_driver)
    current_campaign_dashboard_page.click_new_campaign_btn()
    current_campaign_edit_page = CampaignEditPage(get_driver)
    current_campaign_edit_page.set_name(campaign_name)
    current_campaign_edit_page.click_scenario_tab()
    current_campaign_edit_page.drag_n_drop_second_element_to_first("email", "target")
    current_campaign_edit_page.click_save_btn()
    CampaignPageTest.check_campaign_is_saved()


