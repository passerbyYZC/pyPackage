# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2020-10-03 22:43:03
    LastEditTime: 2020-12-21 09:53:41
    FilePath: /pyPackage/IO/DM7Python/Dm7jdbcDriver17.py
"""
import os
import jaydebeapi
import pandas as pd


def connectDM(configFile="DB_config.ini", attributeName="DM7JDBC_connect"):
    """连接DM7数据库
        
    Args: 
        configFile: 数据库配置信息文件名
        attributeName: 配置属性名称
        
    Returns: 
        conn: 连接器
        curs: 游标
    """

    path = os.getcwd()
    config = 
    conn = jaydebeapi.connect(
        config[attributeName]['jdbcString'],
        config[attributeName]['urlString'],
        [config[attributeName]['userName'], config[attributeName]['password']],
        config[attributeName]['DMJdbcDriver']
    )
    curs = conn.cursor()
    return conn,curs

def selectSQL(curs, sql, colnames):
    """执行 SELECT 语句
        
    Args: 
        curs: 游标
        sql:  SELECT 语句
        colnames: 查询返回结果列名

    Returns: 
        df: SQL语句执行结果，数据类型为：pandas.DataFrame() 
    """
    try:
        curs.execute(sql)
        result_info = curs.fetchall()
    except IOError:
        print("Error: 从数据库读取数据失败!!!")
    finally:
		#数据转换成为DataFrame
        data_list = [list(x) for x in result_info]        
        df = pd.DataFrame(data = data_list, columns=colnames)
        df.fillna(None, inplace=True)
        return df

def insertSQL(conn, curs, sql, df):
    """执行 INSERT INTO 语句
        
    Args: 
        curs: 游标
        sql:  INSERT INTO 语句

    Returns: 
        插入成功标识，0:失败; 1:成功
    """
    columns_str = ", ".join(str(x) for x in df.columns.tolist())
    sql = sql.replace("columns_name", columns_str)

    data_str = ""
    for ind in df.index:
        data_temp = "'"+"', '".join(str(x) for x in df.loc[ind, :].tolist())
        data_str += data_temp+"'),("
    sql = sql.replace("row_data", data_str).replace("nan", "").replace("None", "").replace(",()", "")
    try:
        curs.execute(sql)
    except IOError:
        print("Error: 插入数据到数据库失败!!!")
        print("出错语句: {}".format(sql))
        return 0
    conn.commit()  # 提交到数据库执行 
    return 1

def deleteSQL(conn, curs, sql):    
    """执行 DELETE 语句
        
    Args: 
        curs: 游标
        sql:  DELETE 语句

    Returns: 
        删除成功标识，0:失败; 1:成功
    """
    try:
        curs.execute(sql)
    except IOError:
        print("Error: 从数据库删除数据失败!!!")
        print("出错语句: {}".format(sql))
        return 0
    conn.commit()  # 提交到数据库执行 
    return 1