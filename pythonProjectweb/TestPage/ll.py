from selenium import webdriver
from time import sleep
import hh
#定义浏览器
driver=webdriver.Chrome()
driver.get(hh.url)
sleep(5)
#定位第一个按钮
op=driver.find_element_by_css_selector("[id='1']")
#点击按钮
op.click()
sleep(2)
#将光标移交到弹窗
alert=driver.switch_to.alert

#获取窗口信息并打印
sp=alert.text
sleep(2)
print("确认第一弹窗内容：%s",sp)
#输入框输入内容
#alert.send_keys("1")
alert.send_keys("2")
sleep(2)
#点击确定或取消按钮
s=alert.accept()
#s=alert.dismiss()
sleep(2)
#定位最终结果，并打印
qwe=driver.find_element_by_css_selector("#textSpan>font")
#print("最终结果为：%s"%qwe.text)

if s ==2:
    print("点击确认结果为：%s"%qwe.text)
else:
    print("点击取消结果为：%s"%qwe.text)

driver.quit()