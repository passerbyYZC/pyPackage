# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2020-12-21 14:35:41
    LastEditTime: 2020-12-21 14:37:15
    FilePath: /pyPackage/runDemo.py
"""
import sys, os
baseDir = os.path.dirname(os.path.abspath('__file__'))
baseDir = baseDir.replace('\\','/')
sys.path.append(baseDir+"/IO/DM7Python")
sys.path.append(baseDir+"/IO/redisPython")

from Dm7jdbcDriver17 import DM7Driver
dmd = DM7Driver(configFile="DB_config.ini", attributeName="DM7JDBC_connect")
dmd.connectDM()
df = dmd.selectSQL("SG_ORG_SUBAREA_B")
print(df)
print(dmd.deleteSQL("SG_ORG_SUBAREA_B"))
print(dmd.selectSQL("SG_ORG_SUBAREA_B"))
print(dmd.insertSQL(df, "SG_ORG_SUBAREA_B"))
print(dmd.selectSQL("SG_ORG_SUBAREA_B"))