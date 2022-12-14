#coding'utf-8'
from selenium.webdriver.common.by import By
import hh
from time import sleep
#定位浏览器
driver=hh.getDriver(hh.qq_yx)



#定位账号,密码
hh.cuowu_denglu(driver)
errtext=hh.findElement(driver,By.CSS_SELECTOR,'#err_m').text

print("登录失败，信息是：%s"%errtext)
#登录失败，获取登录错误信息

#回到主页面，定位右上角手机版超链接
driver.switch_to.default_content()
mobile=hh.findElement(driver,By.LINK_TEXT,"手机版")
mobile.click()
driver.implicitly_wait(2)
#sleep(6)
#转移句柄到新页面
handles=driver.window_handles
driver.switch_to.window(handles[-1])
#滚动条最后一行
js="window,scrollTo(0,20000)"
driver.execute_script(js)
sleep(2)
#关闭当前窗口
driver.close()
sleep(5)
#将句柄转移之第一个页面
driver.switch_to.window(handles[0])
#再次定位framea、用户名、密码、登录按钮
driver=hh.zhanghao_mima_denglu(driver)
errtext=hh.findElement(driver,By.CSS_SELECTOR,"#err_m").text
sleep(6)
print("登录失败，信息是：%s"%errtext)
sleep(3)
#再次登录，登录失败

#关闭窗口
driver.quit()
