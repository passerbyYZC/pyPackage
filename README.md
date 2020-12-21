# python 公共函数包

## 1. IO -- 数据输入输出包

### 1.1. 达梦7数据库
```
## 添加 DM7Python 包到工程目录
import sys, os
baseDir = os.path.dirname(os.path.abspath('__file__')).replace('\\','/')  # 工程所在目录
sys.path.append(baseDir+"/IO/DM7Python")

## 引用 DM7Driver 类
from Dm7jdbcDriver17 import DM7Driver

# DM7Driver类实例化
dmd = DM7Driver(configFile="DB_config.ini", attributeName="DM7JDBC_connect")

# 数据库连接
dmd.connectDM()

# 数据表数据查询
df = dmd.selectSQL("SG_ORG_SUBAREA_B")
print(df)

# 数据表数据清空
print(dmd.deleteSQL("SG_ORG_SUBAREA_B"))

# 数据表数据插入
print(dmd.insertSQL(df, "SG_ORG_SUBAREA_B"))
```