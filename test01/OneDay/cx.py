#class addfuntion():
   # def __init__(self,x,y):
    #3       print(f"{x} + {y} =", x + y)
      #  else:
       #     print(("加法运算区间为100-200"))
#class sub():
 #   def __init__(self,x,y):
  #      if 99 >= x >= 40 and 99 >= y >= 40:
   #         print(f"{x} - {y} =", abs(x - y))
    #    else:
     #       print("减法运算区间为40-99")
#class mul():
  #  def __init__(self,x,y):
   #     if 39 >= x >= 20 and 39 >= y >= 20:
    #        print(f"{x} * {y} =", abs(x * y))
     #   else:
      #      print("乘法运算区间为20-39")
#class d#iv():
    #def __init__(self,x,y):
        #if 19 >= x >= 0 and 19 >= y >= 0:
         #   if y == 0:
          #      if x == 11 and y == 2:
           #         print(f"{x} % {y} =", x % y)
            #    elif x == 18 and y == 3:
             #       print(f"{x} // {y} =", x // y)
              #  else:
               #     print(f"{x} / {y} =", x / y)
            #else:
             #   print("两数都为0，不能进行计算！")
        #else:
         #   print("除法运算区间为0-19")
#class calcFunction():
 #   def __init__(self):
  #      first = eval(input("请输入第一个数："))
   #     operator= input("请输入运算符：")
    #    second = eval(input("请输入第二个数："))
     #   if 200 >= first >= 0 and 200 >= second >= 0:
      #      if operator == "+":
       #         addfuntion(first, second)
        #    elif operator == "-":
         #       sub(first, second)
          #  elif operator == "*":
           #     mul(first, second)
            #elif operator == "/":
             #   div(first, second)
            #else:
             #   print("运算符不合法！")
        #else:
          #  print("运算数不在0-200区间范围内")
#if __name__ == '__main__':
 #   calcFunction()


#读取Excel数据（xlrd）
    #def readExcelData(self,sheetname,x,y):
     #   import xlrd
      #  ExcelPath='../poolData/user.xls'
       # OpenFile=xlrd.open_workbook(ExcelPath)
        #sheetpage=OpenFile.sheet_by_name(sheetname)
        # print(sheetpage.nrows)
        # userName=[]
        # for i in range(1,sheetpage.nrows):
        #     userName.append(sheetpage.cell_value(i,0))
        # return userName
       # return sheetpage.cell_value(x,y)


    #def readExcelData(self, sheetname):
       # import xlrd
        #ExcelPath = '../poolData/user.xls'
        #OpenFile = xlrd.open_workbook(ExcelPath)
   #     sheetpage = OpenFile.sheet_by_name(sheetname)
    #    print(sheetpage.nrows)
     #   userName = []
      #  for i in range(1, sheetpage.nrows):
       #     userName.append(sheetpage.cell_value(i, 0))
        #return userName
"""

"""
import pytest
#单参数
#search_list=['aaa','vvvvv','cccc']
#@pytest.mark.parametrize('key_word',['aaaa','vvvv','ccc'])
#def test_search(key_word):
 #   assert key_word in search_list
#多参数
@pytest.mark.vvv
def test_login_001():
    print('用户名登陆成功')
@pytest.mark.vvv
def test_login_002():
    print('用户名密码登录失败')
@pytest.mark.vvv
def test_login_003():
    print('手机一键登录')
