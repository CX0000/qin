from time import sleep
from selenium.webdriver.common.by import By
from demo.testCase.baseUnittest import BaseUnitTest


class Test_lxf(BaseUnitTest):
     def test_personal (self):
         self.loginPage.loginFun()
         # self.driver.implicitly_wait(10)
         sleep(3)
         #self.url=self.driver.current_url
         #self.assertIn("dashboard",self.url)
         self.loginPage.gexinxinxi(self.driver)
         sleep(5)
         # 定位家庭住址信息
         A1 = (By.XPATH, '/html/body/app-root/layout-default/section/app-info/div[1]/div/div/div[2]/div[3]')
         A2=self.loginPage.getElementValue(A1)
         # 断言是否成功
         self.assertIn("河南省郑州市金水区国奥大厦", A2)




# class test_lxf(BaseUnitTest):
#      def test_login_name_pwd(self):
#          self.loginPage.loginFun()
#          sleep(3)
#          # 获取登录后的URL
#          self.url = self.driver.current_url
#          # 判断是否登录成功后的页面信息
#          self.assertIn("dashboard", self.url)
#          # 定位个人信息界面，并点击
#          self.loginPage.GRXX(self.driver)
#          # 定位家庭住址信息
#          jtzz = (By.XPATH, '/html/body/app-root/layout-default/section/app-info/div[1]/div/div/div[2]/div[3]')
#          # 断言是否成功
#          self.assertEqual(" 家庭住址： 河南省郑州市金水区国奥大厦", jtzz)




