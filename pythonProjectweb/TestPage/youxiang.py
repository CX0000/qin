#coding="utf-8"
from selenium.webdriver.common.by import By
import hh
#定位浏览器
driver=hh.getDriver(hh.yx_163)
#定位
ifram=hh.findElement(driver,By.CSS_SELECTOR,"[id^='x-URS-iframe']")
#ifram=driver.find_element_by_css_selector("[id^='x-URS-iframe']")
#将光标移到小页面下
driver.switch_to.frame(ifram)
#定位账号,密码，登录
#a1=driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input")
a1=hh.findElement(driver,By.XPATH,"//div[@id='account-box']/div[2]/input")
#a2=driver.find_element_by_css_selector("[name='password']")
a2=hh.findElement(driver,By.CSS_SELECTOR,"[name='password']")
#a3=driver.find_element_by_xpath("//div/a[@id='dologin']")
a3=hh.findElement(driver,By.XPATH,"//div/a[@id='dologin']")
#输入
# a1.send_keys("3123765166")
# a2.send_keys("12345678")
hh.doInputValue(a1,"3123765166")
hh.doInputValue(a2,"12345678")
#点击登录按钮
# a3.click()
hh.doClick(a3)
driver.implicitly_wait(9)
#截图
hh.dophoto(driver,"1")
#打印当前信息
hh.printCurInfo(driver)

driver.switch_to.default_content()

hh.printCurInfo(driver)

driver.implicitly_wait(3)

vip=hh.findElement(driver,By.LINK_TEXT,"会员")
#点击会员
#vip.click()
hh.doClick(vip)
#句柄转移
handlers=driver.window_handles
driver.switch_to.window(handlers[-1])
#截图
hh.dophoto(driver,"2")

driver.implicitly_wait(8)

#退出
driver.quit()









