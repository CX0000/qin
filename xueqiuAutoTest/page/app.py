from appium import webdriver
from page.main import Main
from page.BasePage import BasePage
class APP(BasePage):
    def start(self):
        _AppPackage = 'com.xueqiu.android'
        _AppActivity = '.view.WelcomeActivityAlias'
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '7.1.2'
            #caps['deviceName'] = '127.0.0.1:62001'
            caps['uuid']='127.0.0.1:62001'
            caps['appPackage'] = _AppPackage
            caps['appActivity'] = _AppActivity
            caps['noReset'] = True
            self._driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
            self._driver.implicitly_wait(30)
        else:
            self._driver.start_activity(_AppPackage,_AppActivity)
            return self
    def main(self):
        return Main(self._driver)






