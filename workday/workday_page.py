""" Workday automation main module """
from locators import Locators
from Page import *



WORKDAY_PRODUCTION_BASE_URL = 'https://wd3.myworkday.com/sanofi/d/inst/15$5312/2500$'
WORKDAY_START_SESSION_URL = '1.htmld#TABINDEX=0&SUBTABINDEX=0'



class WorkdayPage(Page):
    """ Main Workday automation process """
    def __init__(self, base_url=''):
        self.base_url = base_url
        super().__init__(base_url)

    def start_session(self, forced_page):
        self.start_session_driver(forced_page)
        self.presence_of_element_located(Locators.WAIT_CONTENT)
        print("OK !\n")
    
    def end_session(self):
        self.tear_down()

    def load_organization_details(self, organization_id):
        self.change_page("{}.htmld#TABINDEX=0&SUBTABINDEX=3".format(organization_id))
        self.wait_for_element_present(30, *Locators.ORGANIZATION_DETAILS)

    def load_organization_members(self, organization_id):
        self.change_page("{}.htmld#TABINDEX=0&SUBTABINDEX=0".format(organization_id))
        self.wait_for_element_present(30, *Locators.ORGANIZATION_MEMBERS)

    def get_organization_header(self):
        return self.find_element(*Locators.ORGANIZATION_HEADER)

    def wait_for_sub_organization(self):
        return self.wait_for_element_present(1, *Locators.SUB_ORGANIZATION)

    def develop_sub_org_if_longer_than_five(self):
        return self.click_element_if_appears(1, *Locators.PLUS)
    
    def get_organization_list(self):
        return self.find_elements(*Locators.ORGANISATION_LIST)

    def get_organization_members(self):
        return self.find_elements(*Locators.MEMBERS)

    
