from appium.webdriver.webdriver import WebDriver
class BasePage:
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    def find(self,loctor,value:str=None):
        if isinstance(loctor,tuple):
            self._driver.find_element(*loctor)
        else:
            self._driver.find_element(loctor,value)
