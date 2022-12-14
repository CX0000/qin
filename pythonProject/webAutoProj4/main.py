# 这是一个示例 Python 脚本。
import unittest

from common import doSuit, doReport

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
if __name__ == '__main__':
#     #获取测试套件
#     suit=unittest.TestSuite()
     #通过第一种方式获取，需要第一步的suit空对象
#     suit=doSuit.addTestByMethod(suit)
     #通过第二种方式获取，需要第一步suit空对象
#     suit=doSuit.addTestByClass(suit)
     #通过点三种方式获取，不需要第一步suit空对象，会自动生成一个
     suit=doSuit.addTestByAuto()


#     #执行套件，并在控制台打印测试用例执行情况
#     run=unittest.TextTestRunner()
#     run.run(suit)



     #执行并生成测试报告，text格式的
     #doReport.doTextReport(suit)
     #执行并生成测试报告，html格式的
     #doReport.doHTMLReport(suit)
     #执行并生成测试报告，html格式更美观
     doReport.doHMLReportBuf(suit)





    # list1=[29,12,89,30,90,49]
#冒泡排序,从大到小
    # i=0
    # for i in range(0,len(list1)-1):
    #     for j in range(i+1,len(list1)):
    #         if list1[i]<list1[j]:
    #             list1[i],list1[j]=list1[j],list1[i]
    #
    #
    #             print("第%s大循环"%j,list1)
    #         print("第%d次大循环"%(i+1),list1)
    #     print("循环结束",list1)


    #     ipt=int(input("请输入第一个数字："))
    #     a=["hello"]
    #     c=ipt*a
    #     print(c)