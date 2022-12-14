from selenium.webdriver.common.by import By
import hh
driver=hh.getDriver(hh.lxf_url)
#定位注册
xx=hh.findElement(driver,By.XPATH,"//form//a[@class='register']")
xx.click()
driver.back()
driver.implicitly_wait(3)
#定位忘记密码
gg=hh.findElement(driver,By.PARTIAL_LINK_TEXT,'忘记密码？')
gg.click()
driver.implicitly_wait(3)
driver.back()
driver.implicitly_wait(3)
#定位账号密码
cp=hh.findElement(driver,By.XPATH,"//span//input[@placeholder='请输入手机号码']")
op=hh.findElement(driver,By.XPATH,"//span//input[@type='password']")
#输入账号密码
cp.send_keys('15003807446')
driver.implicitly_wait(3)
op.send_keys('12345678qwe')
driver.implicitly_wait(3)
#记住密码
# wq=hh.findElement(driver,By.XPATH,"//span//input[@type='checkbox']")
# wq.click()
# driver.implicitly_wait(5)
# wq=hh.findElement(driver,By.XPATH,"//span//input[@type='checkbox']")
# wq.click()
# driver.implicitly_wait(5)
#定位立即登录
ss=hh.findElement(driver,By.XPATH,"//form//button[@nztype='primary']")
ss.click()
driver.implicitly_wait(6)

driver.quit()