from datetime import datetime
import pandas as pd

# 定义一个日期存放类
class dateMemory:
    def __init__(self,date1:str,date2:str) -> None:
        """
        desc: 获得两个字符串表示的时间,格式为'%Y-%m-%d',
              然后转化为起止的时间戳
        """
        self.start = datetime.strptime(date1, '%Y-%m-%d')
        self.end = datetime.strptime(date2, '%Y-%m-%d')
    def strWhetherInDateRange(self,date3:str) -> bool:
        """
        desc: 如果在这两个之间,则为True
        param: 表示日期的字符串,格式为'%Y-%m-%d'
        return: bool
        """
        currentdate = datetime.strptime(date3, '%Y-%m-%d')
        if currentdate>=self.start and currentdate<=self.end:
            return True
        else:
            return False
    def changeDateRange(self,date1:str,date2:str) -> None:
        """
        desc: 获得两个字符串表示的时间,格式为'%Y-%m-%d',
              改变原有的两个时间戳
        """
        self.start = datetime.strptime(date1, '%Y-%m-%d')
        self.end = datetime.strptime(date2, '%Y-%m-%d')
    def __str__(self) -> str:
        return '当前日期范围为{}至{}'.format(self.start.strftime('%Y-%m-%d'),self.end.strftime('%Y-%m-%d'))

def NA2str(x):
    if pd.isna(x):
        return '缺失'
    else:
        return x