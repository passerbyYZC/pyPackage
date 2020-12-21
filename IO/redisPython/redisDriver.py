# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2020-11-26 11:43:56
    LastEditTime: 2020-12-21 15:33:17
    FilePath: /pyPackage/IO/redisPython/redisDriver.py
"""
import redis, json
import pandas as pd
import os
folder_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")

class redisDriver(object):
    """redis操作驱动
        
    Args: 
        configFile: redis配置信息文件名
        attributeName: 配置属性名称
        
    """
    connect = None
    def __init__(self, configFile, attributeName):
        self.attributeName = attributeName
        self.__config = configparser.ConfigParser()
        self.__config.read(folder_path+"/config/{configFile}".format(configFile=configFile))

    def connect(self):
        """连接redis"""
        self.connect = redis.StrictRedis(
            host=self.__config["host"],
            port=self.__config["port"],
            db=self.__config["db"],
            password=self.__config["password"],
            decode_responses=True
        )
