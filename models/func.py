import pandas as pd

def getMemberInfo(infoCsvPath: str) -> pd.DataFrame:
    """
    desc: 获得团队成员信息
    return: DataFrame
    """
    return pd.read_csv(infoCsvPath)