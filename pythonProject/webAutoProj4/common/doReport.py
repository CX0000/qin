#coding="utf-8"
#处理不同的测试报告
import logging
from unittest import TextTestRunner
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from htmltestreport import HTMLTestReport
from common import config
from common.dolog import Logger

#生成text格式的测试报告
log=Logger(__name__,logging.ERROR)
def doTextReport(suit):
    filename=config.report_path+config.cur_time+"_report.txt"
    try:
        with open(filename,"w",encoding="utf-8") as f:
            runner=TextTestRunner(stream=f,verbosity=2)
            runner.run(suit)
    except Exception as e:
        log.logger.exception("报告生产失败，原因是：%s"%e,exc_info=True)
    else:
        log.logger.info("报告生产成功！")



#生成html格式的测试报告
def doHTMLReport(suit):
    filename=config.report_path+config.cur_time+"_report.html"
    try:
        with open(filename,"w",encoding="utf-8") as f:
            ruener=HTMLTestRunner\
                (stream=f,
                 verbosity=2,
                 title="雷小锋项目测试报告",
                 description="html格式的测试报告. v1.0版本")
            ruener.run(suit)
    except Exception as e:
        log.logger.exception\
            ("html格式的测试报告生成失败.原因是：%s"%e,exc_info=True)
    else:
        log.logger.info("html格式的测试报告生成成功！")


#生成更美观的html格式的测试报告
def doHMLReportBuf(suit):
    filename=config.report_path+config.cur_time+"_bufReport.html"
    runner=HTMLTestReport(filename,title="雷小锋项目漂亮的报告",
                          description="雷小锋项目漂亮的测试报告. v1.0版本")
    runner.run(suit)