#coding'utf-8'
#处理异常信息

def dotry(v1=6,v2=1):
    i=v1+v2
    j=v1*v2
    m = v1 - v2
    try:
        print("除法之前~~~~")
        n = v1 / v2
        #1a="123"

        print("除法之后~~~~")
    # except ZeroDivisionError as z:
    #     print("除零异常错误，信息是：%s" % z)
    #     n="发生异常了，没有值"
    # except ArithmeticError as a:
    #    print("算术计算异常错误：%s"%a)

    except Exception as e:
        print("基础异常信息，内容是%s"%e)
        n = "发生异常了，没有值"
    # except:
    #     print("发生了异常！！！！")
    else:
        print("未发生异常~~~~~")
    finally:
        print("除法之后~~~~")

    print("加法结果是：%s\n减法结果是：%s\n乘法结果是：%s\n除法结果是：%s"%(i,m,j,n))
if __name__=="__main__":
    print("请用方法之前~~~~~~~~~~")
    dotry(8,0)
    print("请用方法之后~~~~~~~~~~")
    dotry()