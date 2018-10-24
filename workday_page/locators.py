from selenium.webdriver.common.by import By

class Locators(object):
    DETAIL = (By.XPATH, '//ul[@data-automation-id="tabBar"]//div[@data-automation-id="tabLabel" and text()="Détail"]')
    PLUS = (By.XPATH, "//div[@data-automation-id='subTabPanel']//div[@data-automation-id='wd-MoreLink' and not(contains(@style,'display: none'))]//span[@data-automation-id='moreLinkLabel' and starts-with(@title, 'Plus (')]")
    INPUT = (By.XPATH, '//input[@type="search"]')
    SEARCH_INPUT = (By.XPATH, '//input')
    ORG = (By.XPATH, "//div[@data-automation-id='compositeSubHeaderTwo' and starts-with(text(),'Organisation')]/../..//div[@class='WBUO WMSO WGTO']")
    ORGANIZATION_HEADER = (By.XPATH, '//div[@id="mainContent"]/div[1]/div[@data-automation-id="pageHeader"]//div[@data-automation-id="menuItem"]//div[starts-with(@data-automation-id, "selectedItem_")]//div[@data-automation-id="promptOption"]')
    ORGANIZATION_DETAILS = (By.XPATH, '//label[@data-automation-id="formLabel" and text()="Site principal"]')
    ORGANIZATION_MEMBERS = (By.XPATH, '//div[@data-automation-id="tabContent"]//label[@data-automation-id="rowCountLabel"]')
    SUB_ORGANIZATION = (By.XPATH, '//label[@data-automation-id="formLabel" and text()="Organisations subordonnées"]')
    ORGANISATION_LIST = (By.XPATH, '//label[@data-automation-id="formLabel" and text()="Organisations subordonnées"]/../..//div[starts-with(@data-automation-id, "selectedItem_")]')
    MEMBERS = (By.XPATH, '//div[@data-automation-id="MainTable-0"]//tbody/tr')
    WAIT_CONTENT = "mainContent"