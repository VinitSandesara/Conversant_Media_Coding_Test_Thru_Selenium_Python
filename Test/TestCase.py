

from selenium import webdriver

from Test.BaseDriver import BaseDriver
from Test.DriverExe.Locators import Locators
from Test.SeleniumUtil import SeleniumUtil


class TestCase():
    driver = BaseDriver().getDriverBasedOnBrowser("chrome")
    driver.get("https://www.conversantmedia.com/")

    # Click the Careers button.
    SeleniumUtil(driver).elementClick(Locators().Careers_Link,"xpath")

    # Click the Join our team button.
    SeleniumUtil(driver).elementClick(Locators().Join_Our_Team_Link)

    # Switch to new tab before performing any action on it
    SeleniumUtil(driver).switchToTabOrWindow()

    # Wait for full page load
    SeleniumUtil(driver).waitForElement(Locators().Search_Input_TextBox)

    # Input requisition number 0096105 into the SEARCH ALL OPENINGS & JOB DESCRIPTIONS input field.
    SeleniumUtil(driver).sendKeys("0096105", Locators().Search_Input_TextBox)

    # Press the magnifying glass button.
    SeleniumUtil(driver).elementClick(Locators().Search_Button)

    # Click the requisition title: Senior QA Engineer, Automation
    SeleniumUtil(driver).elementClick(Locators().Search_Result_Selection, "link")