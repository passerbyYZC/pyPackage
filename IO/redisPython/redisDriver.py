# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2020-11-26 11:43:56
    LastEditTime: 2020-12-14 09:40:30
    FilePath: /topoDataAnalysis/src/redisPython/redisDriver.py
"""
import redis, json
import pandas as pd

def redisConnect(config):
    """连接redis
        
    Args: 
        config: redis配置信息
        
    Returns: 
        redis连接
    """
    connect = redis.StrictRedis(
        host=config["host"],
        port=config["port"],
        db=config["db"],
        password=config["password"],
        decode_responses=True
    )
    return connect

def getData(json_str):
    """获取redis数据并进行数据处理
        
    Args: 
        json_str: redis 获取到的数据
        
    Returns: 
        dict格式数据，key值为组件英文名，value为key所对应的解析数据，格式为pandas.DateFrame()
    """
    json_dict  = json.loads(json_str)
    topoTab_dict = {}
    for key, value in json_dict.items():
        if key in ["CIME", "DT", "QS"]:
            topoTab_dict[key] = {}
            for k, v in value.items():
                topoTab_dict[key][k] = pd.read_json(v, orient="split", dtype=False)
            continue
        topoTab_dict[key] = pd.read_json(value, orient="split", dtype=False)
    return topoTab_dict

def output(data_dict, outputType, filePath="./data"):
    """redis数据输出
        
    Args: 
        data_dict： 输入的redis数据，格式为：dict
        outputType： 输出数据格式，支持：excel文件、json数据流
        filePath： excel文件输出路径，默认为：./data
        
    Returns: 
        输出格式为excel则返回目录路径；为json则返回json数据流
    """
    if outputType == "excel":
        for key, value in data_dict.items():
            value.to_excel("{}/{}.xlsx".format(filePath,key))
        return {"filePath": "{}/".format(filePath)}
    if outputType == "json":
        json_dict = {}
        for key, value in data_dict.items():
           json_dict[key] = value.to_json(orient="split")
        return json_dict