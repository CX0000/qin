from selenium import webdriver
from time import sleep
import hh
#定义浏览器
driver=webdriver.Chrome()
driver.get(hh.url)
sleep(5)
#定位第二弹窗
op=driver.find_element_by_css_selector("[id='2']")
#点击按钮
op.click()
sleep(2)
#操作弹出框
alter=driver.switch_to.alert
#获取窗口信息并打印
sp=alter.text
sleep(2)
print("确认第二弹窗内容：%s",sp)
#点击确定或取消按钮
s=alter.accept()
#s=alter.dismiss()
sleep(2)

#操作浏览器
hello=driver.find_element_by_xpath("//div/input[3]")
sleep(2)
text=hello.get_attribute('value')
print("我现在在浏览器页面，标题内容是：%s"% text)


driver.quit()