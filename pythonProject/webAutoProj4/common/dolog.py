#coding='utf-8'
#log类，处理log文件
import logging

from common import config


class Logger(object):
    #实例化方法，初始化
    def __init__(self,name,fileLevel=logging.WARNING):
        #定义记录器，日志对象，日志文件的实例
        self.logger=logging.Logger(name)

        #定义日志输出等级
        self.logger.setLevel(fileLevel)
        #格式化日志模板
        fmt = logging.Formatter\
            ('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        #处理器，写信息到日志文件
        logname=config.log_path+config.cur_date+".log"
        fh=logging.FileHandler(logname,encoding="utf-8")
        #指定要让处理器按照什么格式来书写日志
        fh.setFormatter(fmt)

        #将处理器加入记录器中：让处理器处理谁   就是让处理器给谁干活~~~
        self.logger.addHandler(fh)

if __name__=="__main__":
    #实例化log日志对象
    logger=Logger(__name__,logging.DEBUG)

    #写日志
    # CRITICAL = 50
    # ERROR = 40
    # WARNING = 30
    # INFO = 20
    # DEBUG = 10

    #debug级别日志
    #logger.logger.log(logging.DEBUG,"我是练习时长两年半的蔡徐坤，等级10")
    logger.logger.debug("我是练习时长两年半的蔡徐坤，等级10")
    #info级别日志
    #logger.logger.log(logging.INFO, "你干嘛~哎呦，等级20")
    logger.logger.info("你干嘛~哎呦，等级20")
    #woring级别日志
    #logger.logger.log(logging.WARNING,"擅长唱，跳，rap，篮球，等级30")
    logger.logger.warning("擅长唱，跳，rap，篮球，等级30")
    #error级别日志
    #logger.logger.log(logging.ERROR, "披肩称王，伴坤远航，等级40")
    logger.logger.error("披肩称王，伴坤远航，等级40")
    #critical级别日志
    #logger.logger.log(logging.CRITICAL, "美国有苹果，中国有坤坤，坤坤手机，等级50")
    logger.logger.critical("美国有苹果，中国有坤坤，坤坤手机，等级50")
