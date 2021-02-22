# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2021-02-22 08:41:34
    LastEditTime: 2021-02-22 08:42:30
    FilePath: \pyPackage\tool\decorator.py
"""

## 函数运行时长装饰器
from datetime import datetime
def getRunTime(func):
    def int_time(*args, **kwargs):
        time0 = datetime.now()
        print("{}开始运行······".format(func))
        res = func(*args, **kwargs)
        print("运行时长：{}".format(datetime.now()-time0))
        return res
    return int_time