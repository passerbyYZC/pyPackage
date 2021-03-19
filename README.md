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
dmd.connect()

# 数据表数据查询
df = dmd.select("SG_ORG_SUBAREA_B")
print(df)

# 数据表数据清空
print(dmd.delete("SG_ORG_SUBAREA_B"))

# 数据表数据插入
print(dmd.insert(df, "SG_ORG_SUBAREA_B"))
```

### 1.2. 数据读取器（CIME、DT）
```
## 添加 dataReader 包到工程目录
sys.path.append(baseDir+"/IO/dataReader")

## 引用 dataReader 类
from dataReader import dataReader

# 读取CIME文件
cimeReader = dataReader(cimeFile)
cimeData_dict = cimeReader.getdata()

# 读取DT文件
dtReader = dataReader(dtFile)
dtData_dict = dtReader.getdata()
```

## 依赖包下载语句
```
pip download -d requirements -r requirements.txt --trusted-host mirrors.aliyun.com
```
