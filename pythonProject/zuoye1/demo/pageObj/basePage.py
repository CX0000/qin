#coding'utf-8'
#基础页面类：存放所有页面可能用到的公共方法及属性
from common import config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#所有page类均继承该基础类

class BasePage(object):
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
        else:
            print("未发生异常，页面打开成功！%s"%self.url)    #定位元素

    #定位元素
    def findElement(self,*locater):
        try:
            ele=WebDriverWait(self.driver,5,0.1).\
                until(EC.visibility_of_element_located(locater))
        except Exception as e:
            print("元素定位失败，错误信息是：%s,该元素是：%s"%(e,str(locater)))
        else:
            print("元素定位成功，%s"%str(locater))
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
        else:
            print("输入内容成功！")

    #获取标签值
    def getElementValue(self,element):
        #定位这个元素
        ele=self.findElement(*element)
        #获取这个文本值
        try:
            eleText=ele.text
        except Exception as e:
            print("获取文本%s失败，\n错误信息是：%s"%(str(element),e))
        else:
            print("文本获取成功，值是：%s"%eleText)
            return eleText

    #截图
    def doPhoto(self,name):
        filename=config.photo_path+config.cur_time+name+".png"
        try:
            self.driver.get_screenshot_as_file(filename)
        except Exception as e:
            print("截图失败，原因是：%s"%e)
        else:
            print("截图成功！")

    #元素点击
    def doClick(self,element):
        ele=self.findElement(*element)
        try:
            ele.click()
        except Exception as e:
            print("元素%s点击失败，原因是：%s"%(str(element),e))
        else:
            print("元素%s点击成功！"%str(element))