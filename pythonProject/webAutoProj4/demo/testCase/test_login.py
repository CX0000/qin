#coding='utf-8'
import logging
import unittest
from time import sleep

from common.dolog import Logger
import logging
from demo.testCase.baseUnittest import BaseUnitTest

log=Logger(__name__,logging.INFO)
#登录页面测试用例

class TestLogin(BaseUnitTest):
    #第一步：执行的代码：setUpClass（）类前置
    #第二步：执行的代码：setU()方法前置
    #第三步；执行的代码是测试方法 OK
    #第四步：执行的代码是测试方法
    #第五步：执行的代码：tearDown（）方法后置
    #第六步：找还没有测试方法，有的话，执行方法前置setUp()
    #第七步：第六步有的话，执行测试方法中的代码，知道完毕
    #第八步：第六步有的话，执行tearDown（）方法后置
    #第九步：还有没有测试方法，无的话，执行代码是：tearDownClass()  类后置

    #登陆成功-用户名密码均正确
    def test_login_name_pwd_ok(self):
        self.loginPage.loginFun()
        #self.driver.implicitly_wait(10)
        sleep(3)
        #获取登陆成功后的url
        self.url=self.driver.current_url
        #判断是否是登录成功后的页面信息
        try:
            self.assertIn("dashboard",self.url)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        #退出登录
        self.loginPage.logoutFun(self.driver)

    #登陆失败-用户名密码均为空
    def test_login_name_pwd_no(self):
        #self.loginPage.loginFun("","")
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[1][0],self.loginPage.lginDataList[1][1])
        #判断是登陆失败
        #判断手机号
        nameText = self.loginPage.getElementValue(self.loginPage.erro)
        try:
            self.assertEqual("请输入手机号码",nameText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        #判断密码
        pwdText=self.loginPage.getElementValue(self.loginPage.erro2)
        self.assertEqual("请输入6-20位账户密码",pwdText)

    #登陆失败，用户名空，密码正确
    def test_login_name_no_pwd_ok(self):
        #self.loginPage.loginFun("","2000zhang")
        self.loginPage.loginFun \
            (self.loginPage.lginDataList[2][0], self.loginPage.lginDataList[2][1])
        #判断是登陆失败
        #判断手机号
        nameText = self.loginPage.getElementValue(self.loginPage.erro)

        try:
            self.assertEqual("请输入手机号码", nameText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        #判断密码
        #pwdText=self.loginPage.getElementValue(self.loginPage.erro2)
        #self.assertNotEqual("请输入6-20位账户密码",pwdText)

    #登陆失败，用户名正确，密码空
    def test_login_name_ok_pwd_no(self):
        #self.loginPage.loginFun("15555211512","")
        self.loginPage.loginFun \
            (self.loginPage.lginDataList[3][0], self.loginPage.lginDataList[3][1])
        sleep(5)
        #self.driver.implicitly_wait(5)
        #判断是登陆失败
        #判断密码
        pwdText=self.loginPage.getElementValue(self.loginPage.erro2)
        try:
            self.assertEqual("请输入6-20位账户密码",pwdText)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")




    #登陆失败，用户名错误(用户名不存在)，密码正确
    def test_login_name_true_pwd_false(self):
        #self.loginPage.loginFun("11555521151","2000zhang")
        self.loginPage.loginFun \
            (self.loginPage.lginDataList[4][0], self.loginPage.lginDataList[4][1])
        sleep(3)
        #获取弹窗错误信息
        errTxt=self.loginPage.getElementValue(self.loginPage.errMesage)
        #断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误，请重新输入！",errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        #点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)

    #登陆失败，用户名正确，密码错误
    def test_login_name_false_pwd_true(self):
        #self.loginPage.loginFun("15555211512","2000zh")
        self.loginPage.loginFun \
            (self.loginPage.lginDataList[5][0], self.loginPage.lginDataList[5][1])
        # 获取弹窗错误信息
        errTxt = self.loginPage.getElementValue(self.loginPage.errMesage)
        # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误", errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        # 点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)

    # 登录失败-用户名错误密码错误
    def test_login_name_false_pwd_false(self):
        #self.loginPage.loginFun("11555521151","1234567cx")
        self.loginPage.loginFun \
            (self.loginPage.lginDataList[6][0], self.loginPage.lginDataList[6][1])
        # 获取弹窗错误信息
        errTxt = self.loginPage.getElementValue(self.loginPage.errMesage)
        sleep(3)
        # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误", errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        sleep(3)
        # 点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)
        sleep(3)

        ##用户名超过12，密码正确
    def test_login_name1_false_pwd_false(self):
        self.loginPage.loginFun \
            (self.loginPage.lginDataList[7][0], self.loginPage.lginDataList[7][1])
        # 获取弹窗错误信息
        errTxt = self.loginPage.getElementValue(self.loginPage.errMesage)
        sleep(3)
        # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误", errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        sleep(3)
        # 点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)
        sleep(3)

    ##用户名少于，密码正确
    def test_login_name2_false_pwd_false(self):
        self.loginPage.loginFun \
            (self.loginPage.lginDataList[8][0], self.loginPage.lginDataList[8][1])

        nameText = self.loginPage.getElementValue(self.loginPage.erro)
        try:
            self.assertEqual("请输入手机号码", nameText)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")

    #用户名正确，密码大于21
    def test_login_name3_false_pwd_false(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[9][0], self.loginPage.lginDataList[9][1])
        # # 获取弹窗错误信息
        errTxt = self.loginPage.getElementValue(self.loginPage.errMesage)
        # # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误", errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        # # 点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)

    # 用户名正确，密码少于6
    def test_login_name4_false_pwd_false(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[10][0], self.loginPage.lginDataList[10][1])
        # 判断密码
        pwdText = self.loginPage.getElementValue(self.loginPage.erro2)
        try:
            self.assertEqual("请输入6-20位账户密码", pwdText)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")














if __name__ == '__main__':
    unittest.main()
