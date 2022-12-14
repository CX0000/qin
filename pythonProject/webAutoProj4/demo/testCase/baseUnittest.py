#coding='utf-8'
#基础的Unittest，前置后置方法
import unittest
from time import sleep
from selenium import webdriver

from demo.pageObj.loginPage import LoginPage


#from demo.pageObj.loginPage import LoginPage, personal


class BaseUnitTest(unittest.TestCase):
    #类方法的前置
    @classmethod
    def setUpClass(cls) -> None:
        #实例化浏览器
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        print("我是setUpClass方法")

    #类方法的后置
    @classmethod
    def tearDownClass(cls) -> None:
        #退出浏览器
        cls.driver.quit()
        print("我是tearDownClass")

    #方法级别的前置
    def setUp(self) -> None:
        #定义登陆页面的实例化
        self.loginPage=LoginPage(self.driver)
        #self.loginPage=personal(self.driver)
        #打开该页面
        self.loginPage.open()
        print("我是setUp")

    #方法级别的后置
    def tearDown(self) -> None:
        #刷新页面
        self.driver.refresh()
        sleep(5)
        print("我是tearDown")

