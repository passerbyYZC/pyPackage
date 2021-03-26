# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2021-03-26 11:19:09
    LastEditTime: 2021-03-26 17:11:38
    FilePath: /pyPackage/IO/log/main.py
"""
import sys, os
import logging
import logging.config

logging.config.fileConfig("config/logging_config.ini")
logger = logging.getLogger("developer")


logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')

try:
    a = 0/0
except Exception as error:
    logger.exception(sys.exc_info())