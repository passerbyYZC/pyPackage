# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2021-03-26 11:19:09
    LastEditTime: 2021-06-07 14:15:56
    FilePath: /pyPackage/log/main.py
"""
import sys, os
baseDir = os.getcwd().replace("\\","/")

# 获取负荷存储目录，如果目录不存在则创建该目录
import configparser
logConfig = configparser.ConfigParser()
logConfig.read(os.path.join(baseDir, "config", "logConfig.ini"))

logging_path = os.path.dirname(eval(logConfig["handler_fileHandler"]["args"])[0])
if not os.path.exists(logging_path):
    os.makedirs(logging_path)

import logging, logging.config
logging.config.fileConfig(os.path.join(baseDir, "config", "logConfig.ini"))
logger = logging.getLogger("developer")

from datetime import datetime, timedelta
def write2log(func):
    def int_time(*args, **kwargs):
        time0 = datetime.now()
        logger.info("{} 开始运行······".format(func))
        res = None
        try:
            res = func(*args, **kwargs)
        except Exception as error:
            logger.exception(sys.exc_info())
        logger.info("{} 运行耗时：{}".format(func, datetime.now()-time0))
        return res
    return int_time

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')

try:
    a = 0/0
except:
    logger.exception(sys.exc_info())