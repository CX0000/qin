#conding='utf-8'
#元素的常用属性
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
#
import hh
#定义浏览器对象
driver=webdriver.Chrome()
#打开页面
driver.get(hh.url)
sleep(5)
#定位输入框
#inpt=driver.find_element_by_css_selector("#kw")

#输入内容
# inpt.send_keys("bilibili")
# sleep(3)
# #模拟回车键
# inpt.submit()
# sleep(5)

# #获取大小
# print(inpt.size)
# #判定是否可见
# print("输入框是否可见:",inpt.is_displayed())
# #判断是否可用
# print("输入框是否可用:",inpt.is_enabled())
# #判断是否选中
# print("输入框是否选中:",inpt.is_selected())


# #清除文本内容
# inpt.clear()
# sleep(3)
#定位右上角的登录，并点击
# loga=driver.find_element_by_css_selector("#u1>a")
# loga.click()
# sleep(3)
# #定位登陆框中的登录按钮并点击
# log=driver.find_element_by_id("TANGRAM__PSP_11__submit")
# log.click()
# print(log.get_attribute("class"))
# print(log.get_attribute("id"))
# sleep(2)
#定位错误的提示信息
#error=driver.find_element_by_id("TANGRAM__PSP_11__error")
#
#获取错误信息并打印
#print("错误信息:",error.text)
#print("错误信息是:%s"% error.text)
#
#sleep(3)


#
#弹出框
#定位第一个按钮
# bt3=driver.find_element_by_xpath("//body//input[@value='确认弹窗按钮']")
# bt3.click()
# sleep(3)
# #操作弹出框
# alert=driver.switch_to.alert


#第一个弹窗
# #获取弹窗的文本信息。并打印
# altext=alert.text
# print("弹出框中的文本内容是:%s",altext)
# #向输入框中输入内容
# alert.send_keys("1")
#
# #点击弹窗中的取消按钮
#alert.dismiss()
#
# #点击弹窗中的确定按钮
# alert.accept()
# sleep(5)

#定位页面中的结果
#第二个弹窗和第三个弹窗
#info=alert.text
#print("第三个弹窗文本信息：%s"%info)
#点击alert的确定按钮
#alert.accept()
#点击alert的取消按钮
#alert.dismiss()
#定位结果
#result=driver.find_element_by_css_selector("#textSpan>font")
#print("他把窗关闭之后，页面中的结果是:%s",result.text)
op=driver.find_element_by_css_selector("[value='确认弹窗按钮']")
op.click()
sleep(3)
alert=driver.switch_to.alert
sp=alert.text
sleep(2)
print("确认第三个弹窗内容：%s"%sp)
#alert.accept()
alert.dismiss()
sleep(3)
#关闭浏览器
driver.quit()
