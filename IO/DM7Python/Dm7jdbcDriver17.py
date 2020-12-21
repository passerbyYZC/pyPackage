# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2020-10-03 22:43:03
    LastEditTime: 2020-12-21 14:29:31
    FilePath: /pyPackage/IO/DM7Python/Dm7jdbcDriver17.py
"""
import jaydebeapi
import configparser
import pandas as pd
import os
folder_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")

class DM7Driver(object):
    """DM7数据库操作驱动
        
    Args: 
        configFile: 数据库配置信息文件名
        attributeName: 配置属性名称
        
    """
    conn = None
    curs = None
    def __init__(self, configFile, attributeName):
        self.attributeName = attributeName
        self.__config = configparser.ConfigParser()
        self.__config.read(folder_path+"/config/{configFile}".format(configFile=configFile))

    def connect(self):
        """数据库连接"""
        self.conn = jaydebeapi.connect(
            self.__config[self.attributeName]['jdbcString'],
            self.__config[self.attributeName]['urlString'],
            [self.__config[self.attributeName]['userName'], self.__config[self.attributeName]['password']],
            folder_path + self.__config[self.attributeName]['DMJdbcDriver']
        )
        self.curs = self.conn.cursor()


    def select(self, tableName, sql=None):
        """执行 SELECT 语句
            
        Args: 
            tableName: 数据表名称
            sql: SELECT 语句模板

        Returns: 
            df: SQL语句执行结果，数据类型为：pandas.DataFrame() 
        """
        sql = self.__config["Select_sql"]["select_df"].format(table_name=tableName) if sql == None else sql
        try:
            self.curs.execute(sql)
            data_list = [list(x) for x in self.curs.fetchall()]  
            self.curs.execute(self.__config["Select_sql"]["columns_name"].format(table_name=tableName))
            colnames = [x[0] for x in self.curs.fetchall()]   
            df = pd.DataFrame(data=data_list, columns=colnames)
            return df
        except:
            print("Error: 数据表{table_name}读取数据失败!!!".format(table_name=tableName))
            print("出错语句: {}".format(sql))
            return pd.DataFrame()

    def insert(self, df, tableName, sql=None):
        """执行 INSERT INTO 语句
            
        Args: 
            df: 需插入的DataFrame数据
            tableName: 数据表名称
            sql: INSERT INTO 语句模板

        Returns: 
            插入成功标识，0:失败; 1:成功
        """
        if sql == None:
            columns_str = ", ".join(str(x) for x in df.columns.tolist())
            data_str = ""
            for ind in df.index:
                data_temp = "'"+"', '".join(str(x) for x in df.loc[ind, :].tolist())
                data_str += data_temp+"'),("
            data_str = data_str.replace("nan", "").replace("None", "")
            sql = self.__config["Insert_sql"]["insert_df"].format(table_name=tableName, columns_name=columns_str, row_data=data_str).replace(",()", "")
        try:
            self.curs.execute(sql)
            self.conn.commit()  # 提交到数据库执行 
            return 1
        except:
            print("Error: 数据表{table_name}插入数据失败!!!".format(table_name=tableName))
            print("出错语句: {}".format(sql))
            return 0

    def delete(self, tableName, sql=None):    
        """执行 DELETE 语句
            
        Args: 
            tableName: 数据表名称
            sql: DELETE 语句模板

        Returns: 
            删除成功标识，0:失败; 1:成功
        """
        sql = self.__config["Delete_sql"]["clean_table"].format(table_name=tableName) if sql == None else sql 
        try:
            self.curs.execute(sql)
            self.conn.commit()  # 提交到数据库执行 
            return 1
        except:
            print("Error: 数据表{table_name}删除数据失败!!!".format(table_name=tableName))
            print("出错语句: {}".format(sql))
            return 0