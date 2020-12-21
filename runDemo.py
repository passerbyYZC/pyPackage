# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2020-12-21 14:35:41
    LastEditTime: 2020-12-21 15:29:31
    FilePath: /pyPackage/runDemo.py
"""
import sys, os
baseDir = os.path.dirname(os.path.abspath('__file__'))
baseDir = baseDir.replace('\\','/')
sys.path.append(baseDir+"/IO/DM7Python")
sys.path.append(baseDir+"/IO/redisPython")

from Dm7jdbcDriver17 import DM7Driver
dmd = DM7Driver(configFile="DB_config.ini", attributeName="DM7JDBC_connect")
dmd.connect()
df = dmd.select("SG_ORG_SUBAREA_B")
print(df)
print(dmd.delete("SG_ORG_SUBAREA_B"))
print(dmd.select("SG_ORG_SUBAREA_B"))
print(dmd.insert(df, "SG_ORG_SUBAREA_B"))
print(dmd.select("SG_ORG_SUBAREA_B"))