#coding='utf-8'
#测试浏览器驱动

from selenium import webdriver  #输出
from time import sleep   #输出延迟时间

#定义浏览器驱动
driver=webdriver.Chrome()
#打开页面
driver.get("http://www.baidu.com")
#sleep(2)   #sleep（延迟时间）
#最大化
# driver.maximize_window()
# sleep(2)
#最小化
#driver.minimize_window()
#sleep(3)

#打开新页面
#driver.get("http://www.w3school.com.cn")
#sleep(2)

#刷新
#driver.refresh()
#sleep(2)

#回到上一个页面
# driver.back()
# sleep(2)

#回到下一个页面
# driver.forward()
# sleep(2)
#
# #关闭窗口,当前页面
# driver.close()
# sleep(2)

#退出浏览器

#元素定位
#通过id定位 百度一下首页的输入框
#inp=driver.find_element_by_id("kw")

#通过name定位百度一下首页的输入框
#inp=driver.find_element_by_name("wd")

#通过class_name查找
#inp=driver.find_element_by_class_name("s_ipt")

#通过标签定位页面元素,tag_name不唯一，一般不使用
#inp=driver.find_element_by_tag_name()

#通过xpath-绝对路径定位输入框
#inp=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[1]/div[1]/form/span[1]/input")

#通过xpath:相对路径定位输入框，相对加绝对
#inp=driver.find_element_by_xpath('//form/span[1]/input')

#通过xpath:相对路径定位输入框，属性
# inp=driver.find_element_by_xpath("//input[@id='kw']")
#
# #向文本框输入内容
# #inp.send_keys("bilibili")
# #sleep(3)
#
# #向
# #but=driver.find_element_by_xpath("//input[contains(@class,'s_btn')]")
#
#
# #inp=driver.find_element_by_xpath("//input[@id'su']")
# #inp.click()
#
# #通过text值，text（）方法定位元素
# #setting=driver.find_element_by_xpath("//span[text()='设置']")
#
# #通过超链接定位元素
# # a1=driver.find_element_by_link_text("新闻")
# # a2=driver.find_element_by_partial_link_text('中国空天变化')
# # a2.click()
#
#
# #通过css定位
# #inp=driver.find_element_by_css_selector("#kw")
# #通过css选择器定位
# #inp=driver.find_element_by_css_selector(".s_ipt")
# #inp=driver.find_element_by_css_selector("[name='wd']")
# #inp=driver.find_element_by_css_selector(".bg.s_btn")
# #inp=driver.find_element_by_css_selector("[type='submit']")
#
# inp.send_keys("bilibili")
# sleep(3)
#
#
# #关闭当前窗口
# #driver.close()
# #通过css定位元素：父子
# #login=driver.find_element_by_css_selector("#u>a:nth-child(3)")
# #login.click()
# #通过css选择器定位元素模糊匹配前半部分
# #login=driver.find_element_by_css_selector("a[class^='s-top-login-btn']")
# #通过css定位模糊后半部分
# #login=driver.find_elements_by_css_selector("a[id$='loginbtn']")
# #通过css选择器模糊定位部分
# login=driver.find_element_by_css_selector("a[class*='c-btn-mini']")
# login.find_element(By.CSS_SEELECTOR,"a[class*='s-top-login-btn']")
# login.click()
sleep(5)

driver.quit()


