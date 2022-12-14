from selenium import webdriver
from time import sleep
import hh
#定义浏览器
driver=webdriver.Chrome()
driver.get(hh.url)
sleep(5)
#定位第三弹窗
op=driver.find_element_by_css_selector("[value='确认弹窗按钮']")
#点击按钮
op.click()
sleep(2)
#操作弹出框
alter=driver.switch_to.alert
#获取窗口信息并打印
sp=alter.text
sleep(2)
print("确认第三弹窗内容：%s"%sp)
sleep(2)
#点击确定或取消按钮
alter.accept()
#s=alter.dismiss()
sleep(2)
#定位最终结果，并打印
qwe=driver.find_element_by_css_selector("#textSpan>font")

rut1="您为何如此自信"
rut2="您为何如此谦虚"
if qwe.text==rut1:
    print("你点击的确定按钮")
else:
    print("你点击的取消按钮")

driver.quit()