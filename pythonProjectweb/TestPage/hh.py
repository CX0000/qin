#定义
import time
from selenium import webdriver
from time import sleep
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

bd_url="http://www.baidu.com"
url="file:///C:/Users/apple/Desktop/alert.html"
lxf_url='http://139.199.0.102/dashboard'
yx_163='https://mail.163.com/'
qq_yx='https://mail.qq.com/'

#定位当前时间变量，且格式化：2022_11_17 16_35_30
cur_time=time.strftime("%Y_%m_%d %H_%M_%S")

##定义图片的存放路径：当前项目目录下的data目录下的photos目录下
base_path="D:/pythonCoding/pythonProjectweb/data/photos/"

def getDriver(vurl):
    try:
        driver=webdriver.Chrome()
    except Exception as e:
        print("发生异常，浏览器实例化失败!\n错误信息是%s"%e)
    else:
        print("未发生异常，浏览器实例化成功")
    try:
        driver.get(vurl)
    except Exception as e:
        print("页面打开失败：%s，\n错误信息是：%s"%(vurl,e))
    else:
        #sleep(2)
        #隐式等待
        driver.implicitly_wait(4)
        return driver

def printCurInfo(driver):
    twohandler = driver.current_window_handle
    cur_URL = driver.current_url
    title = driver.title
    print("新页面信息开始打印~~~~~~~~~~~~~")
    print("移交句柄后,当前窗口的句柄是：%s,\n转移后的窗口的URL是：%s,\n转移后的窗口标题是：%s" % (twohandler, cur_URL, title))
    print("新页面结束打印~~~~~~~~~~~~~~~~")

def zhanghao_mima_denglu(driver):
    iframe = driver.find_element_by_css_selector("#login_frame")
    driver.switch_to.frame(iframe)
    a1 = driver.find_element_by_css_selector("[type='text']")
    a2 = driver.find_element_by_css_selector("[type='password']")
    a1.clear()
    a1.send_keys("3123765166")
    a2.clear()
    a2.send_keys("cx1636623140")
    a3 = driver.find_element_by_css_selector("[type='submit']")
    a3.click()
    #sleep(9)
    #隐式等待
    driver.implicitly_wait(1)

def cuowu_denglu(driver):
    # 定位iframe
    iframe = driver.find_element(By.CSS_SELECTOR, "#login_frame")
    # 将光标移到小页面下
    driver.switch_to.frame(iframe)
    # 定位账号,密码
    a1 = driver.find_element_by_css_selector("[type='text']")
    a2 = driver.find_element_by_css_selector("[type='password']")
    a1.clear()
    a1.send_keys("3123765166")
    a2.clear()
    a2.send_keys("12345678")
    # 定位登录
    a3 = driver.find_element_by_css_selector("[type='submit']")
    # 登录失败，获取登录错误信息
    a3.click()
    sleep(5)

def findElement(driver,locater,value):
    #异常处理容易出错的代码块
    try:
        #ele=driver.find_element(locater,value)
        ele=WebDriverWait(driver,5,0.1).\
            until(EC.visibility_of_element_located((locater,value)))
        #ele=WebDriverWait
    #发生异常时捕获异常并让程序继续执行
    #异常类型是Exception 且定义别名为e，并打印异常信息
    except Exception as e:
        print("元素定位失败！%s \n错误信息是：%s"%(value,e))
    #未发生异常时执行的代码块
    else:
        print("元素定位成功！%s"%value)
        return ele
    #不管是否发生异常，均执行的代码块
    finally:
        print("不管你成功还是失败你都要执行我!!!")

def doClick(ele):
    try:
        ele.click()
    except Exception as e:
        print("发生异常，点击失败，错误信息是：%s"%e)
    else:
        print("未发生异常，点击成功")

#对输入文本进行异常处理
def doInputValue(ele,value):
    try:
        ele.send_keys(value)
    except Exception as e:
        print("异常发生，输入内容失败内容是：%s\n错误信息是：%s"%(value,e))
    else:
        print("异常发生，输入内容成功")

#截图
def dophoto(driver,value):
    filename=base_path+cur_time+value+".png"
    driver.get_screenshot_as_file(filename)
    try:
        driver.get_screenshot_as_file(filename)
    except Exception as e:
        print("截图失败，错误信息是：%s"%e)
    else:
        print("截图成功!!!")



