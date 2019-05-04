# -*- coding: utf-8 -*-
import page_objects.campaign_edit_page

from iris_selenium_tests.page_objects.campaign_edit_page import CampaignEditPage

class CampaignPageTest(object):

    def checkPageTitle(self):
        actualvalue = CampaignEditPage.get_page_title()
        assert actualvalue == "Cabestan -- Reloaded", "The title of the page is different to the expected value. Actual value is :" + actualvalue


    def checkHeaderTitle(self):
        actualvalue = CampaignEditPage.get_header_title()
        assert (actualvalue == "Audiences", "The title of the header is different to the expected value. Actual value is :" + actualvalue)


    def checkContainerTitle(self):
        actualvalue = CampaignEditPage.get_container_title()
        assert actualvalue == u"Dernières audiences", "The title of the container is different to the expected value. Actual value is :" + actualvalue


    def checkTiltles(self):
        self.checkPageTitle()
        self.checkHeaderTitle()
        self.checkContainerTitle()


    def checkHeaderOfTable(self):
        haed_table = CampaignEditPage.get_head_table_audience()
        assert haed_table['DATE'] == u"Date"
        assert haed_table['NOM'] == u"Nom"
        assert haed_table['CREATEUR'] == u"Créateur"
        assert haed_table['NB_CONTACT'] == u"Nb de contacts"
        assert haed_table['STATUT'] == u"Statut"

    def check_campaign_is_saved(self):
        assert False