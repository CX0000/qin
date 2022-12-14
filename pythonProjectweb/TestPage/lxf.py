#="utf-8"
from selenium import webdriver
from time import sleep
import hh
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#多窗口切换
#定义实例，并打开页面：雷小锋
driver=webdriver.Chrome()
driver.get(hh.lxf_url)
#移交句柄
hh.printCurInfo(driver)
#定位账号密码
#cp=driver.find_element_by_xpath("//span//input[@placeholder='请输入手机号码']")
cp=hh.findElement(driver,By.XPATH,"//span//input[@placeholder='请输入手机号码']")
#op=driver.find_element_by_xpath("//span//input[@type='password']")
op=hh.findElement(driver,By.XPATH,"//span//input[@type='password']")
#输入账号密码
#cp.send_keys('15003807446')
hh.doInputValue(cp,"15003807446")
#sleep(2)
#op.send_keys('12345678qwe')
hh.doInputValue(op,'12345678qwe')
#sleep(2)

#定位立即登录
#ss=driver.find_element_by_xpath("//form//button[@nztype='primary']")
ss=hh.findElement(driver,By.XPATH,"//form//button[@nztype='primary']")
# ss.click()
hh.doClick(ss)
hh.dophoto(driver,"1")
#sleep(8)
#移交句柄

hh.printCurInfo(driver)

#鼠标类
action=ActionChains(driver)
#sp=driver.find_element_by_xpath("//span[@style='font-size: .14rem;color: #999;padding-left: .1rem']")
sp=hh.findElement(driver,By.XPATH,"//span[@style='font-size: .14rem;color: #999;padding-left: .1rem']")
action.move_to_element(sp)
#sleep(2)
#执行
action.perform()
#sleep(5)
#定位退出账号
#op=driver.find_element_by_css_selector(".userInfo-popPanel>:nth-child(4)")
op=hh.findElement(driver,By.CSS_SELECTOR,".userInfo-popPanel>:nth-child(4)")
#点击
# op.click()
hh.doClick(op)
#截图
hh.dophoto(driver,"2")
#操作弹出框
#alert=driver.switch_to.alert
#定位确认按钮
#lp=driver.find_element_by_css_selector(".ant-modal-confirm-btns>button:nth-child(2)")
lp=hh.findElement(driver,By.CSS_SELECTOR,".ant-modal-confirm-btns>button:nth-child(2)")
#sleep(3)
#点击
# lp.click()
hh.doClick(lp)
#截图
hh.dophoto(driver,"3")
#sleep(2)
driver.implicitly_wait(8)
driver.quit()