#="utf-8"
from selenium import webdriver
from time import sleep
import hh
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#多窗口切换
#定义实例，并打开页面：百度一下
driver=webdriver.Chrome()
driver.get(hh.bd_url)
#点击百度一下的超链接：登录
#a1=driver.find_element_by_link_text("登录")
loginA=hh.findElement(driver,By.CSS_SELECTOR,"#u1>a")
locaterA=(By.CSS_SELECTOR,"#u1>a")
#显示等待，及定位有做判断是否可见
#a1=WebDriverWait(driver,5,0.1).until(EC.visibility_of_element_located(locaterA))
#显示等待，仅仅判断元素是否存在
#loginA=WebDriverWait(driver,5,0.1).until(EC.visibility_of(loginA))

#显示等待，元素出现(两件事情：定位并判断)
#loginA=WebDriverWait(driver,5,0.1).until(EC.presence_of_element_located(locaterA))
#判断右上角登录true按钮的文本值是否与预期一致、预期值是：登录做两件事、即定位又做判断，如果一直返回true
result=WebDriverWait(driver,5,0.1).until(EC.text_to_be_present_in_element((locaterA),"登录"))

#百度一下但你的定位方式
bd_locator=(By.CSS_SELECTOR,"#su")
#判断百度一下按钮的value的属性的值是否一致：预期的值是：百度一下
result2=WebDriverWait(driver,5,0.1).until(EC.text_to_be_present_in_element_value(bd_locator,"百度一下"))
print("百度按钮的value值是否正确：%s"%result2)
if result==True:
    print("登录按钮的文本值是否正确:%s"%result)
    loginA.click()
#sleep(3)
driver.implicitly_wait(5)
#定位百度协议
a2=hh.findElement(driver,By.LINK_TEXT,"百度用户协议")
a2.click()
sleep(3)
#打印出当前页面的标题，句柄，url
s1=driver.window_handles
s2=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口标题是：%s,当前窗口的url是：%s"%(title,cur_URL))
print("当前窗口的句柄是：%s"%s2)
print("当前所有的窗口的句柄有哪些：%s"% str(s1))


#获取当前title
sjtitle="百度用户协议"
#result=WebDriverWait(driver,5,0.1).until(EC.title_is(title))
result=WebDriverWait(driver,5,0.1).until(EC.title_contains(title))
print(result)
#句柄转移
driver.switch_to.window(s1[-1])
#获取当前句柄
hh.printCurInfo(driver)
#操作hao123
driver.close()
sleep(5)

#再次切换到最初页面
driver.switch_to.window(s2)

driver.quit()