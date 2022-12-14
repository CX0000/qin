from page.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

from page.phote import Photo
from page.search import Search
import time
class Main(BasePage):
    def goto_my_page(self):
        self.find(By.ID,"profile_image").click()
        time.sleep(3)
        return Photo(self._driver)
    def goto_search_page(self):
        self.find(By.ID,"home_search").click()
        time.sleep(3)
        return Search(self._driver)
