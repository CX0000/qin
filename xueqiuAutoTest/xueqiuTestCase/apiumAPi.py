import time
from appium import webdriver
_AppPackage = 'com.xueqiu.android'
_AppActivity = '.view.WelcomeActivityAlias'
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
#caps['deviceName'] = '127.0.0.1:62001'
caps['uuid']='127.0.0.1:62001'
caps['appPackage'] = _AppPackage
caps['appActivity'] = _AppActivity
caps['noReset'] = True
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
driver.implicitly_wait(30)
#关闭app，一般与launch_app（）配合使用
driver.close_app()
#app是否被安装
print(driver.is_app_installed(_AppPackage))
#卸载app
driver.remove_app(_AppPackage)
time.sleep(5)
#安装app
driver.install_app('C:\\Users\\apple\\Desktop\\xueqiu.apk')
time.sleep(2)
#打开app指定页面
driver.start_activity(_AppPackage,_AppActivity)
time.sleep(5)
#置后台
driver.background_app(5)
time.sleep(2)
#重置
#driver.reset()
driver.press_keycode(26)
#手势类的操作，滑动，长按，拖拽
from appium.webdriver.common.touch_action import TouchAction
#按压控件，element或坐标点二选一，不能填写两个,release（）结束动作，释放按压指针：perform（）执行
TouchAction(driver).press(element/坐标点[x,y]).release().perform()
#长按先执行后释放
TouchAction(driver).long_press(element).perform().release()
#点击，注意：语法[(x,y)],1,内置tap函数：2，使用TouchAction类
driver.tap([(100,200)])
TouchAction(driver).tap(element=).perform().release()
#暂停,单位是毫秒
TouchAction(driver).wait(2000)
#移动,element目标位置元素
TouchAction(driver).move_to(element).perform().release()
TouchAction(driver).long_press().move_to().perform().release()
#滑动
driver.swipe(x1,y1,x2,y2,times)
#收起键盘
driver.hide_keyboard()
#摇一摇
driver.shake()
#滚动从A元素到B元素第一种scroll系统给的，第二种flick自带的内置函数
driver.scroll(A_element,B_element)
driver.flick(x1,y1,x2,y2)
#放大与缩小
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
action1=TouchAction(driver)
action2=TouchAction(driver)
zoom=MultiAction(driver)
action1.press(x1,y1).wait(1000).move_to(x1,y1).wait(1000)
action2.press(x1.y1).wait(1000).move_to(x1,y1).wait(1000)
zoom.add(action1,action2)
#获取屏幕的分辨率
x=driver.get_window_size()["width"]
y=driver.get_window_size()['height']

driver.swipe(0.8*x,0.5*y,0.2*x,0.1*y,2000)
#网络
driver.set_network_connection(4)
#通知栏
driver.open_notifications()
#修改经纬度
driver.set_location(latitude=18,longitude=21,altitude=None)
#is_enable编辑，is_selected选中，is_dispalyed可见
driver.find_element().is_selected()
assert driver.find_element().is_enabled() is True
from appium.webdriver.common.mobileby import MobileBy
driver.find_element(MobileBy.ID)
driver.switch_to.context("webview")