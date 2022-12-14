from page.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
import time
class Search(BasePage):
    def searchinput(self,key):
        self.find(By.ID,"search_input_text").sent_keys(key)
        time.sleep(2)
        self.find(By.ID,"name").cleck()
        time.sleep(3)
        return self
    def get_price(self):
        self.find(By.ID,"com.xueqiu.android:id/search_input_text")