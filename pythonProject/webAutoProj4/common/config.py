#coding='utf-8'
#所有的配置文件信息
import os
import time

#基本的页面地址
base_url="http://139.199.0.102/passport/login"

#当前时间
cur_time=time.strftime("%Y_%m_%d %H_%M_%S")

#当前日期
cur_date=time.strftime("%Y_%m_%d")

#项目路径
base_path="D:\pythonCoding\pythonProject\webAutoProj4\\"

#截图路径
#photo_path=base_path+"/data/photos/"
photo_path=os.path.join(base_path,r"data\photos\\")
#log路径
#log_path=base_path+"/data/logs/"
log_path=os.path.join(base_path,r"data\logs\\")

lxf_url='http://139.199.0.102/dashboard'

#数据路径
data_path=os.path.join(base_path,r"data\testDatas\\")

#测试用例的路径
test_path=os.path.join(base_path,r"demo\testCase\\")

#测试报告路径
report_path=os.path.join(base_path,r"data\reports\\")