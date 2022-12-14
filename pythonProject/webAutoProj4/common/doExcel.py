#coding='utf-8'
#处理excel文件
import logging

import xlrd

from common import config
from common.dolog import Logger

log=Logger(__name__,logging.DEBUG)
class DoExcel(object):
    #重构初始化方法
    def __init__(self,wk="testData.xlsx",st="elements"):
        try:
            filename=config.data_path+wk
        #打开工作簿
            self.workbook=xlrd.open_workbook(filename)
        # #获取sheet页，三种方法获取sheet页
        # stnames = self.workbook.sheet_names()
        # print(stnames)
        # #第一种方法：列表的下表
        # self.sheet = self.workbook.sheet_names()[0]
        # #第二种方法：索引 index
        # self.sheet=self.workbook.sheet_by_index(0)
        #第三种方法：sheet名称
            self.sheet=self.workbook.sheet_by_name(st)
        except Exception as e:
            log.logger.error("工作簿或者sheet页为实例化成功，原因是：%s"%e,exc_info=True)
        else:
            log.logger.info("工作簿%s，sheet页面%s打开成功"%(self.workbook,self.sheet))

    #读取单元格的值
    def readExcel(self,rownum,colnum):
        try:
            value=self.sheet.cell_value(rownum,colnum)
        except Exception as e:
            print("读取文件异常")
            log.logger.error("该单元格值是(%s,%s)获取失败"%(rownum,colnum))
        else:
            #print("读取文件成功，值是：%s"%value)
            log.logger.info("单元格值(%s,%s)文件获取成功，值是：%s"%(rownum,colnum,value))
            return value


#自测方法
if __name__=="__main__":
    ex=DoExcel()
    value=ex.readExcel(1,4)
    print(value)

