# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2021-03-26 11:19:09
    LastEditTime: 2021-03-29 10:10:27
    FilePath: /pyPackage/IO/log/main.py
"""
import sys, os
import logging
import logging.config

logging.config.fileConfig("config/logging_config.ini")
logger = logging.getLogger("developer")

from datetime import datetime
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
except Exception as error:
    logger.exception(sys.exc_info())