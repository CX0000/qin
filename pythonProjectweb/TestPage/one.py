#定义项目地址
url="file:///C:/Users/apple/Desktop/alert.html"
from selenium import webdriver


def getDriver():
    driver = webdriver.Chrome()


    return driver


def printCurInfo(driver):
    twohandler = driver.current_window_handle
    cur_URL = driver.current_url
    title = driver.title
    print("移交句柄后,当前窗口的句柄是：%s,\n转移后的窗口的URL是：%s,\n转移后的窗口标题是：%s" % (twohandler, cur_URL, title))



