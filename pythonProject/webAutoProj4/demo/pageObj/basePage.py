#coding'utf-8'
#基础页面类：存放所有页面可能用到的公共方法及属性
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from common import config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from common.doExcel import DoExcel
from common.dolog import Logger

#所有page类均继承该基础类
#定义log对象
log=Logger(__name__,logging.DEBUG)
#元素定位
testData=DoExcel()





class BasePage(object):
    #定位登陆成功后右上角退出登录按钮
    #右上角个人头像
    img=(By.CSS_SELECTOR,".teachHeadPic.ng-star-inserted")
    #退出账号
    #logout=(By.XPATH,"[//div[text()='退出账号']")
    logout=(By.XPATH,"//div[@class='userInfo-popPanel']/div[4]")
    #个人信息
    #personal_information=(By.XPATH,"//div[@class='userInfo-popPanel']/div[1]")
    #退出账号的弹窗的确定按钮
    logoutOK=(By.CSS_SELECTOR,".ant-modal-confirm-btns>button:nth-child(2)")




    # 右上角个人信息
    s1 = (By.XPATH, '//*[@id="headerH"]/div[2]/div[5]/div[2]/div[1]')
    # # 点击右上角个人信息按钮
    s2 = (By.XPATH, "//div[@class='userInfo-popPanel']/div[1]")



    #重构初始方法
    def __init__(self,driver,url=config.base_url):
        self.driver=driver
        self.url=url



    #打开页面
    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("异常发生,页面打开失败，失败内容是：%s\n失败的页面是：%s"%(e,self.url))
            log.logger.critical\
                ("异常发生,页面打开失败，失败内容是：%s\n失败的页面是：%s"%(e,self.url),exc_info=True)
        else:
            print("未发生异常，页面打开成功！%s"%self.url)    #定位元素
            log.logger.info("未发生异常，页面打开成功！%s"%self.url)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()


            #定位元素
    def findElement(self,*locater):
        try:
            ele=WebDriverWait(self.driver,5,0.1).\
                until(EC.visibility_of_element_located(locater))
        except Exception as e:
            print("元素定位失败，错误信息是：%s,该元素是：%s"%(e,str(locater)))
            log.logger.error\
                ("元素定位失败，错误信息是：%s,该元素是：%s"%(e,str(locater)),exc_info=True)
        else:
            print("元素定位成功，%s"%str(locater))
            log.logger.info("元素定位成功，%s"%str(locater))
            return ele



    #文本框输入
    def inputValue(self,inputBox,value):
        #定位元素
        ele=self.findElement(*inputBox)
        #输入内容
        try:
            ele.send_keys(value)
        except Exception as e:
            print("输入内容%s失败，原因是：%s"%(value,e))
            log.logger.critical\
                ("输入内容%s失败，原因是：%s"%(value,e),exc_info=True)
        else:
            print("输入内容成功！")
            log.logger.info("输入内容成功！")

    #获取标签值
    def getElementValue(self,element):
        #定位这个元素
        ele=self.findElement(*element)
        #获取这个文本值
        try:
            eleText=ele.text
        except Exception as e:
            print("获取文本%s失败，\n错误信息是：%s"%(str(element),e))
            log.logger.warning\
                ("获取文本%s失败，\n错误信息是：%s"%(str(element),e),exc_info=True)
        else:
            print("文本获取成功，值是：%s"%eleText)
            log.logger.info("文本获取成功，值是：%s"%eleText)
            return eleText



    #截图
    def doPhoto(self,name):
        filename=config.photo_path+config.cur_time+name+".png"
        try:
            self.driver.get_screenshot_as_file(filename)
        except Exception as e:
            print("截图失败，原因是：%s"%e)
            log.logger.error\
                ("截图失败，原因是：%s"%e,exc_info=True)
        else:
            print("截图成功！")
            log.logger.info("截图成功！")



    #元素点击
    def doClick(self,element):
        ele=self.findElement(*element)
        try:
            #ele.click()
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception as e:
            print("元素%s点击失败，原因是：%s"%(str(element),e))
            log.logger.error\
                ("元素%s点击失败，原因是：%s"%(str(element),e),exc_info=True)
        else:
            print("元素%s点击成功！"%str(element))
            log.logger.info("元素%s点击成功！"%str(element))

    def gexinxinxi(self,driver):
        action = ActionChains(driver)
        # 悬浮到头像上
        action.move_to_element(self.findElement(*self.img))
        action.perform()
        sleep(3)
        self.doClick(self.s1)
        self.doClick(self.s2)
        # self.doClick(self.personal_information)
        # self.doClick(self.a3)

    #退出登录
    def logoutFun(self,driver):
        action=ActionChains(driver)
        #悬浮到头像上
        action.move_to_element(self.findElement(*self.img))
        action.perform()
        sleep(3)
        #点击退出登录按钮
        self.doClick(self.logout)
        #点击个人信息
        #self.doClick(self.personal_information)
        #点击弹窗中的确定按钮
        self.doClick(self.logoutOK)
        sleep(3)









if __name__=="__main__":
    driver=webdriver.Chrome()
    url="http://www.baidu.com"
    bspage=BasePage(driver,url)

    #调用open方法
    bspage.open()
    bspage.driver.implicitly_wait(10)

    #获取文本值
    seting=(By.LINK_TEXT,"设置")
    print(bspage.getElementValue(seting))

    #调用输入内容
    locater=(By.ID,"kw")
    bspage.inputValue(locater,"python")

