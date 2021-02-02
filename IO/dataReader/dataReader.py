# -*- coding:utf-8 -*- 
"""
    Author: Yao Z.C.
    Date: 2021-02-02 15:13:18
    LastEditTime: 2021-02-02 17:30:25
    FilePath: /topoNet/src/pyTopo/dataReader.py
"""
import re
import pandas as pd

class dataReader(object):
    """文件数据读取器
        
    Args: 
        filename*: 文件路径名称
        
    Returns: 
        格式化后的数据，数据表格式为: pandas.DataFrame()
    """
    def __init__(self:object, filename:str):
        self.filename = filename

    def getdata(self):
        """获取CIME文件数据"""
        fileTab_dict = {}
        ## 读取文件数据
        try:
            with open(self.filename, "r+", encoding="utf-8") as dataFile:
                lines_str = dataFile.readlines()
                lines_str = [re.sub(r'\s+', '\t', x.upper()) for x in lines_str]
                lines_str = [re.sub(r'\t$', '', x) for x in lines_str]
        except:
            with open(self.filename, "r+", encoding="gb18030") as dataFile:
                lines_str = dataFile.readlines()
                lines_str = [re.sub(r'\s+', '\t', x.upper()) for x in lines_str]
                lines_str = [re.sub(r'\t$', '', x) for x in lines_str]
        
        for line_str in lines_str:
            # 文件头
            if re.match(r"<!.*>", line_str):
                pass
            # 起始标签
            elif re.search(r"<[^/!].*>", line_str):
                tag = re.findall(r"[A-Z]+", line_str)[0]
                fileTab_dict[tag] = {}
                data = []
            # 终止标签
            elif re.search(r"</.*>", line_str):
                endtag = re.findall(r"[A-Z]+", line_str)[0]
                assert tag==endtag, "数据表格开始标签({tag})和终止标签({endtag})不匹配".format(tag=tag, endtag=endtag)
                try:
                    fileTab_dict[tag]["note"] = note
                except:
                    pass
                fileTab_dict[tag]["data"] = pd.DataFrame(columns=columnsEN_list, data=data)
                try:
                    fileTab_dict[tag]["data"].set_index(["NUM"], inplace=True)
                except:
                    pass
            # 属性名英文
            elif re.search(r"@.*", line_str):
                line_str = re.sub(r"@\s", "", line_str)
                columnsEN_list = line_str.split("\t")
            # 属性名中文
            elif re.search(r"//.*", line_str):
                line_str = re.sub(r"//\s", "", line_str)
                columnsCN_list = line_str.split("\t")
                # assert len(columnsCN_list)==len(columnsEN_list), "{tag}数据中文列和英文列长度不等".format(tag=tag)
                note = dict(zip(columnsEN_list, columnsCN_list))
            # 数据
            elif re.search(r"#.*", line_str):
                line_str = re.sub(r"#\s", "", line_str)
                row_list = line_str.split("\t")
                data += [row_list]
            else:
                continue
        return fileTab_dict