import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from AppTestCase import param
#from selenium.webdriver.common.by import By
des_caps={}
des_caps["platformName"]=param.PlatformName
des_caps["platformVersion"]=param.PlatformVersion
des_caps["deviceName"]=param.DeviceName
des_caps["app"]=param.App
des_caps["noReset"]=param.NoReset
des_caps["appPackage"]=param.AppPackage
des_caps["appActivity"]=param.AppActivity
des_caps['chromedriverExecutable']='D:\\pythonCoding\\AppiumDemo\\chrome\\chromedriver.exe'
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',des_caps)
driver.implicitly_wait(20)
#driver.find_element(By.ID,"id、name、clas、tag、xpath、csss、link、p_link")
#driver.find_element(MobileBy.ID,"home_search").click()
driver.find_element(By.ACCESSIBILITY_ID,"content-desc值")
"""
ANDROID_UIAUTOMATOR   定位方法是Android原生定位方法。和xpath有点类似，比xpath更加好用：
支持元素的全部属性定位，使用函数uiSelector
表达式：new UiSelector()，函数名称(“定位表达式”)
    实例化一个uiSelector对象，通过实例对象调用对应的方法，每个方法都会返回实例对象
函数：
1，id方法
resourceId("id值")
resourceIdMatches("id部分值")   id正则表达式

2，text方法
text("文本值")
textContains("文本部分")  文本包含
textStartWith(文本头部)   文本头部
textMatches(""文本部分值)  文本正则表达式

3，描述方法
description("desc")  描述
descriptionContains("desc")  描述包含
descriptionStartWith("desc")  描述开头
descriptionMatches("desc")  描述正则表达式

4，class方法
className('class值')类名

5，索引、实例方法
index('index值')  编号
instance('')  索引

6，特殊属性
checked('布尔值')  选择属性
checkable('布尔值点击属性')  点击属性
longClickable('布尔值')  长按属性

7、多属性组合
示例：
newUiSelector().resourceId("id值").text("text文本值")
newUiSelector().className('class值').checkable('布尔值')
"""

