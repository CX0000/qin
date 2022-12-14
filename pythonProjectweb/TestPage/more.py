#="utf-8"
from selenium import webdriver
from time import sleep
import hh
from selenium.webdriver.common.by import By
#多窗口切换
#定义实例，并打开页面：百度一下
driver=webdriver.Chrome()
driver.get(hh.bd_url)

#点击百度一下页面的超链接：hao123
a123=hh.findElement(driver,By.LINK_TEXT,"hao123")
a123.click()
sleep(2)
#关键性一步：移交句柄
handlers=driver.window_handles
onehandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口标题是：%s,当前窗口的url是：%s"%(title,cur_URL))
print("当前窗口的句柄是：%s"%onehandler)
print("当前所有的窗口的句柄有哪些：%s"% str(handlers))
#句柄转移
driver.switch_to.window(handlers[-1])
#获取当前句柄
twohandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("移交句柄后,当前窗口的句柄是：%s,\n转移后的窗口的URL是：%s,\n转移后的窗口标题是：%s"%(twohandler,cur_URL,title))
#操作hao123
driver.close()
sleep(3)

#再次切换到最初页面
driver.switch_to.window(onehandler)


driver.quit()
