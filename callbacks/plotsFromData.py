from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
# use dcc to generate graphs 
from dash import dcc
import plotly.express as px
from models.api import getWeatherAUS

# get data
df_weatherAUS = getWeatherAUS()

# @app.callback(
#     Output('statistics-chart', 'figure'),
#     Input('statistics-chart-switch', 'value'),
# )
# def statistics_switch_chart(value):
