#coding='utf-8'
from time import sleep
import hh
from selenium.webdriver.common.by import By
#定位百度
driver=hh.getDriver(hh.bd_url)
#定义右上角登录超链接
a1=hh.findElement(driver,By.LINK_TEXT,"登录")
a1.click()
sleep(3)
#登录页面定义百度用户协议
a2=hh.findElement(driver,By.LINK_TEXT,"百度用户协议")
#点击超链接
a2.click()
sleep(3)
#移交句柄
handlers=driver.window_handles
#句柄转移
driver.switch_to.window(handlers[-1])
#打印当前的标题，句柄，url
hh.printCurInfo(driver)
#操作滚动条
#定义js字符串
js="window,scrollTo(0,5000)"
#执行js脚本
driver.execute_script(js)
sleep(3)
#关闭当前页面
driver.close()
sleep(3)
#退出浏览器
driver.quit()