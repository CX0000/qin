from selenium import webdriver
from time import sleep
import hh
from selenium.webdriver import ActionChains
#定义浏览器
driver=webdriver.Chrome()
driver.get(hh.url)
sleep(2)

driver.maximize_window()
sleep(2)

action=ActionChains(driver)
#定位超链接更多
sp=driver.find_element_by_link_text("更多")
#悬停
action.move_to_element(sp)
#点击
action.click(sp)
#右击
action.context_click(sp)
#双击
action.double_click(sp)
#定位输入框
a=driver.find_element_by_partial_link_text("网盘")
b=driver.find_element_by_partial_link_text("新征程")
#拖拽
action.drag_and_drop(b,a)
sleep(2)

#执行
action.perform()
sleep(2)
driver.quit()

