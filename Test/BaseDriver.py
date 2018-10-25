import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaseDriver():

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    def getDriverBasedOnBrowser(self, browserName):
        bName = browserName.lower()
        if bName == "chrome":
            executable_path = self.PROJECT_ROOT + "/DriverExe/chromedriver"
            os.environ["webdriver.chrome.driver"] = executable_path
            driver = webdriver.Chrome(executable_path)
            driver.implicitly_wait(5)
            return driver
        elif bName == "firefox":
            driver = webdriver.Firefox(executable_path = self.PROJECT_ROOT + "/DriverExe/geckodriver")
            driver.implicitly_wait(5)
            return driver
        else:
            print("In Correct Browser")
            return False




