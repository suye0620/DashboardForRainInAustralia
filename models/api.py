
import pandas as pd

def getMemberInfo() -> pd.DataFrame:
    """
    desc: 获得团队成员信息
    return: DataFrame
    """
    return pd.read_csv('models/data/membersInfo.csv',encoding='utf-8')

def getWeatherAUS() -> pd.DataFrame:
    """
    desc: 获得天气数据
    return: DataFrame
    """
    return pd.read_csv('models/data/weatherAUS.csv',encoding='utf-8')