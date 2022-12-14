#完成输出Hello,world
#查看关键字
#import keyword
#print(keyword.kwlist)
#
#a="姓名张三"
#b="年龄18"
#c="手机号13812345678"
#d="Email：13812345678@163.com"
#e="地址:河南省郑州市金水区农业路18号"

#print(f"姓名{a}"+f"年龄{b}"+f"手机号{c}"+f"Email{d}"+f"Address{e}")

#a=input("请输入姓名")
#b=input("请输入年龄")
#c=input("请输入手机号")
#d=input("请输入Email")
#e=input("请输入地址")

#print("姓名{}".format(a))
#print("年龄{}".format(b))
#print("手机号{}".format(c))
#print("Email{}".format(d))
#print("地址{}".format(e))

#a="123456789"

#print(a[-1])
#print(a[2:7:1])

#li=[1,2,1,2,3]
#print(set(li))
#print(list(set(li)))
#a=()
#b=tuple()
#c=(1,2)
#d=(1,2)
#print(type(a))
#print(type(b))
#print(type(c))

#dict1={}
#dict2=dict()
#dict3={"key":"value","name":"zhangsan"}
#dict4=dict(name="zhangsanfeng")
#print(dict3)
#for i in [1,2,3,4]:
 #   if i==3:
  #      continue
   # print(i)
#result=0
#for i in range(1,101,):
 #   if i%2==0:
  #      print(i)
   # result=result+i
#print(result)


def check1(u,v,list):
    if u in list.keys():
        if v == list[u]:
            return '登陆成功'
    else:
        return '账号或密码错误'

def check2(u, v, s, list):
    if u in list.keys():
        return '用户名不能重复'
    else:
        if len(u) < 6 or len(u) > 18:
            return '用户名长度为6-18位'
        elif len(v) < 6 or len(v) > 20 or v.isdigit() == True or v != s:
            return '密码长度位6-20，不能为纯数字'
        else:
            return '注册成功'
def Signin():
    u=input('请输入账号')
    v=input('请输入密码')
    s=input('请在次输入')
    return check2(u,s,v,userList)
def register():
    u=input('请输入用户名')
    v=input('请输入密码')
    return check1(u,v,userList)
def mainPage():
    while True:
        choose=int(input('1登录页面\n'+'2注册页面\n''请输入你的选择:'))
        if choose==1:
            print(register())
            break
        elif choose==2:
            print(Signin())
            break
        else:
            print('请点击登录或注册')
if __name__ == '__main__':
    userList = {'甘雨': "12345678",
                '钟离': '123456789',
                '凝光': '12345678990'
                }
    mainPage()



userList = {'甘雨': "12345678",'钟离': '123456789','凝光': '12345678990'}
class Signin():
    def __init__(self,u,v):
        if u in userList.keys():
            if v ==userList[u]:
                print('登录成功')
            else:
                print('用户名或密码不一致')
        else:
            print('用户名或密码不一致')
class register():
    def register1(self):
        u = input('请输入用户名')
        if len(u) < 6 or len(u) > 18:
            v = input('请输入密码')
            if u not in userList.keys():
                if len(v) < 6 or len(v) > 20:
                    if v.isdigit():
                        return "密码不能纯数字"
                    else:
                        v1 = int(input('请输入密码'))
                        if v == v1:
                            return '注册成功'
                        else:
                            return '两次密码不一致'
                else:
                    return '请输入密码6-20位'
            else:
                return '用户名已存在'
        else:
            return '用户名不符合规则'


class mainPage():
    def __init__(self,choose):
        if choose == 1:
            a = Signin(input("请输入用户名："),input("请输入密码："))
            print(a)
            if choose == 2:
                b=register().register1()
                print(b)
            else:
                return

if __name__ == '__main__':
    e = mainPage(int(input("请输入一个数字:")))
    print(e)








































