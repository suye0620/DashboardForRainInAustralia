
from webbrowser import get
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
    return pd.read_csv('models/data/weatherAUS.csv',encoding='utf-8',parse_dates=['Date'])

def getCityAUS() -> pd.DataFrame:
    """
    desc: 获得各城市经纬度
    return: DataFrame
    """
    df_geo = pd.read_csv("models/data/cityAUS.csv",encoding='utf-8')
    return df_geo

def getDemoData() -> str:
    """
    desc: 获得各城市经纬度
    return: str
    """
    with open('models/data/demoData.csv',mode='r',encoding='utf-8') as f:
        all_text = f.read()
        f.close()
        return all_text

