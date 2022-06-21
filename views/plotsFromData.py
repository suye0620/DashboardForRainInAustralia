import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
# use dcc to generate graphs 
from dash import dcc
from dash.dependencies import Input, Output 
import plotly.express as px
from models.api import getWeatherAUS
from server import app


df_weatherAUS = getWeatherAUS()

plotsFromDataContent = [
    # divider
    fac.AntdDivider([
        fac.AntdIcon(icon='fc-data-sheet',style={'fontSize':'2.5rem'}),
        fac.AntdText('数据',strong=True,style={'fontSize':'2.5rem'})]
    ),
    
    # data table
    fac.AntdSpin(
        fac.AntdTable(
            id='weatherAUS-table',
            # 服务端模式
            mode='server-side',
            data=df_weatherAUS.head(10).to_dict('records'),
            # 列表生成式
            columns=[
                {'title': column, 'dataIndex': column,} for column in df_weatherAUS.columns
            ],
            # 是否在表格周围添加网格线
            bordered=True,
            pagination={
            'current': 1,
            'total': df_weatherAUS.shape[0],
            'pageSize': 10,
            'pageSizeOptions': [10,5]
            },
            maxWidth=400,
        ),
        text='奋力回调中···',
    ),

    # divider
    fac.AntdDivider([
        fac.AntdIcon(icon='fc-bullish',style={'fontSize':'2.5rem'}),
        fac.AntdText('看板',strong=True,style={'fontSize':'2.5rem'})]
    ),

    # plots from data
    html.Div(
        html.Div([
            # Pre is a wrapper for the <pre> HTML5 element.
            html.Pre('[]', id='select-demo-output'),
            fac.AntdSelect(
                id='select-city',
                placeholder='共{}城市,请选择城市：'.format(
                    len(df_weatherAUS.Location.unique())
                ),
                # 单选，返回一个值
                mode=None,
                options=[
                    {'label': i, 'value': i} for i in df_weatherAUS.Location.unique()
                ],
                style={
                    # 使用css样式固定宽度
                    'width': '200px'
                }
            )
        ],
        style={
            # col的列宽占页面宽度的大小
            'width': '60%',
        }
        ),
        # 外层Div样式
        style={
            # 背景颜色与之前保持一致
            'background-color': '#f0f2f5',

            # control div size
            'width': '100%',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'start'
        }
    )
]

# 回调函数：下拉菜单选择城市，然后显示日历
@app.callback(
    Output('select-demo-output', 'children'),
    Input('select-city', 'value'),
    prevent_initial_call=True
)
def button_callback_demo(value):

    # value is a str
    df_oneCity = df_weatherAUS[df_weatherAUS['Location'] == value]
    startDate = df_oneCity.Date.min().strftime("%Y-%m-%d")
    endDate = df_oneCity.Date.max().strftime("%Y-%m-%d")
    
    return '城市{0}的日期范围为{1}-{2}'.format(str(value),startDate,endDate)

# 回调函数：数据表翻页的 
@app.callback(
    # Output('weatherAUS-table', 'data'),
    [Output('weatherAUS-table', 'data'),
     Output('weatherAUS-table', 'pagination')],

    # 被修饰的函数是Input和Output之间的连接 
    Input('weatherAUS-table', 'pagination'),
    prevent_initial_call=True
    # suppress_callback_exceptions=True
)

def table_server_side_callback(pagination):

    # 构造临时副本数据框，防止有操作对原始数据框做更改；而且页面其他的地方还会用到原始数据框
    batch_df = df_weatherAUS.copy()

    # 在前面的条件组合基础上，输出对应页的数据帧
    # pageSize是pagination的key
    start_index = (pagination['current'] - 1) * pagination['pageSize']
    end_index = pagination['current'] * pagination['pageSize']

    # 更新data与pagination参数
    return (
        batch_df.iloc[start_index:end_index, :].to_dict('records'),
        dash.no_update
    )
    