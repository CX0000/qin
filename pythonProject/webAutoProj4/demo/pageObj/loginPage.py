from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.doExcel import DoExcel
from demo.pageObj.basePage import BasePage, testData
loginData=DoExcel(wk="testData.xlsx",st="loginData")
class personal(BasePage):
    #个人信息
    a1=(By.XPATH,"//div[@class='userInfo-popPanel']/div[1]")



class LoginPage(BasePage):
    #用户名
    zh=(By.XPATH,testData.readExcel(1,4))
    #密码
    mm=(By.XPATH,testData.readExcel(2,4))
    #登录按钮
    dl=(By.XPATH,testData.readExcel(3,4))
    #错误信息
    erro=(By.XPATH,testData.readExcel(4,4))
    erro2=(By.XPATH,testData.readExcel(5,4))
    #错误信息，登陆信息失败时候的弹窗错误信息
    errMesage=(By.CSS_SELECTOR,testData.readExcel(6,4))
    #错误信息，弹窗中的确认按钮
    errBut=(By.CSS_SELECTOR,testData.readExcel(7,4))

    #登陆数据
    lginDataList=[[int(loginData.readExcel(1,2)),loginData.readExcel(1,4)],#正确的用户名、正确的密码
                  [loginData.readExcel(2,2),loginData.readExcel(2,3)],#登陆失败-用户名密码均为空
                  [loginData.readExcel(3,2),loginData.readExcel(3,3)],#登陆失败，用户名空，密码正确
                  [int(loginData.readExcel(4,2)),loginData.readExcel(4,3)],#登陆失败，用户名正确，密码空
                  [int(loginData.readExcel(5,2)),loginData.readExcel(5,3)],#登陆失败，用户名错误(用户名不存在)，密码正确
                  [int(loginData.readExcel(6,2)),loginData.readExcel(6,3)],#登陆失败，用户名正确，密码错误
                  [int(loginData.readExcel(7,2)),loginData.readExcel(7,3)],#登录失败-用户名错误密码错误
                  [int(loginData.readExcel(8,2)),loginData.readExcel(8,3)],#用户名超过12，密码正确
                  [int(loginData.readExcel(9,2)),loginData.readExcel(9,3)],#用户名少于，密码正确
                  [int(loginData.readExcel(10,2)),loginData.readExcel(10,3)],#用户名正确，密码大于21
                  [int(loginData.readExcel(11,2)),loginData.readExcel(11,3)]]#用户名正确，密码少于6
    #登录方法
    #def loginFun(self,vanme="15555211512",vpwd="2000zhang"):
    def loginFun(self,vanme=lginDataList[0][0],vpwd="2000zhang"):
        #输入账号
        self.inputValue(self.zh,vanme)
        #输入密码
        self.inputValue(self.mm,vpwd)
        #点击登录
        self.doClick(self.dl)
        sleep(2)

#自测方法
if __name__=="__main__":
    driver=webdriver.Chrome()
    login=LoginPage(driver)
    login.open()
    login.loginFun()
    #登录失败，空值
    # login.loginFun("","")
    # #获取错误信息的值，并打印
    # errorName=login.getElementValue(login.erro)
    # print(errorName)
    #
    # errotPwd=login.getElementValue(login.erro2)
    # print(errotPwd)

    # #登陆失败，值错误
    # login.loginFun("15555211512","200zhang")
    # #login.loginFun(testdata1.readExcel(1,1),testdata1.readExcel(1,2))
    # #获取弹窗错误信息，并打印
    # errMasg=login.getElementValue(login.errMesage)
    # print(errMasg)
    # #点击弹窗中的确定按钮
    # login.doClick(login.errBut)
    print("我的登录数据是：",login.lginDataList)




