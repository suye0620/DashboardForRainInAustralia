import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
# use dcc to generate graphs 
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output ,State
from models.api import getWeatherAUS,getCityAUS,getDemoData
from server import app
# json用来调试回调函数的多输入值
# import json
from tools import *
import dash_daq as daq
import plotly.express as px
import plotly.graph_objects as go
import pickle,catboost

df_CityAUS = getCityAUS()
df_weatherAUS = getWeatherAUS()
demo_data = getDemoData()

# make plots
fig_CityAUS = go.Figure(data=go.Scattergeo(
        lon = df_CityAUS['Long'],
        lat = df_CityAUS['Lat'],
        text = df_CityAUS['city'],
        mode = 'markers',
        marker_color = 'blue',
        ))

fig_CityAUS.update_layout(
        title = '<b>澳洲各城市的地理位置</b>',
        geo_scope='world',
        margin = {"t": 50, "r": 35, "b": 10, "l": 50},
        font=dict(
        family="Times New Roman, Microsoft YaHei",
        size=18
        )
    )

# 随机初始化一个实例
dateMemory1 = dateMemory('2015-6-1','2015-6-1')

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
            fac.AntdTitle(
                '🕍选择城市',
                level=3,
                style={
                    'color': 'black',
                    # 'fontSize': '4.5 rem',
                }
            ),
            # Pre is a wrapper for the <pre> HTML5 element.
            # html.Pre('[]', id='select-demo-output'),

            # 下拉选择框
            fac.AntdSelect(
                id='select-city',
                placeholder='共{}座城市,请选择城市：'.format(
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
            ),
            
            # 地理位置图
            dcc.Graph(id='cityAUS-graph',figure=fig_CityAUS),

            # title: '选择日期'
            fac.AntdTitle(
                '📅选择日期',
                # id='dateRange-title',
                level=3,
                style={
                    'color': 'black',
                    # 'fontSize': '4.5 rem',
                }
            ),

            # 日期选择框
            fac.AntdDatePicker(
                id='select-date',
                picker='date',
                placeholder='请选择日期',
                # 默认禁用组件
                disabled=True,
            ),

            # text tips
            # 没有选择城市时没有提示，用于占位，一旦选择了城市就有提示
            html.Div(id='dateRange-warning'),

            # 用于占位，一旦选择了日期就有
            html.Div(id='oneDayWeather-div'),

            # title: '整体数据侧写'
            fac.AntdTitle(
                '🌎整体情况',
                # id='dateRange-title',
                level=3,
                style={
                    'color': 'black',
                    # 'fontSize': '4.5 rem',
                }
            ),

            fac.AntdTitle(
                '变量分布',
                # id='dateRange-title',
                level=4,
                style={
                    'color': 'black',
                    # 'fontSize': '4.5 rem',
                }
            ),

            html.Div(
                # fill the external 60% div
                fac.AntdImage(src='/assets/imgs/distribution.png',style = {'width':'100%'},preview=False),
                style={
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),

            fac.AntdTitle(
                '变量相关性',
                # id='dateRange-title',
                level=4,
                style={
                    'color': 'black',
                    # 'fontSize': '4.5 rem',
                }
            ),

            html.Div(
                # fill the external 60% div
                fac.AntdImage(src='/assets/imgs/corrPlot.png',style = {'width':'100%'},preview=False),
                style={
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
        ],
        style={
            # col的列宽占页面宽度的大小
            'width': '70%',
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
    ),

    # divider
    fac.AntdDivider([
        fac.AntdIcon(icon='fc-questions',style={'fontSize':'2.5rem'}),
        fac.AntdText('预测',strong=True,style={'fontSize':'2.5rem'})]
    ),

    html.Div(
        html.Div([
            # 标题提示
            fac.AntdTitle(
                '🔢请输入你要预测的某日观测:',
                # id='dateRange-title',
                level=4,
                style={
                    'color': 'black',
                    # 'fontSize': '4.5 rem',
                }
            ),
            html.Br(),
            fac.AntdParagraph('格式要求', strong=True),
            fac.AntdParagraph('逗号分隔,依次输入:Location,MinTemp,MaxTemp,Rainfall,'+
            'WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,WindSpeed9am,WindSpeed3pm,'+
            'Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Temp9am,Temp3pm', strong=True),
            fac.AntdParagraph('一些例子,预测时注意不要复制最后一项', strong=True),
            fac.AntdParagraph('倒数两个下雨样本预测对了,嘿嘿(●ˇ∀ˇ●)', strong=True),
            html.Plaintext(demo_data,style={
                'font-size': '1.5rem',
                'font-weight': 'bold',
                # 'font-family': 'sans-serif',
            }),



            # 预测区
            html.Span([
                # 输入框
                fac.AntdInput(
                    id = 'oneday-observation-input',
                    mode='default',
                    placeholder='请输入你要预测的观测',
                    style={
                            'width': '600px',
                            'marginBottom': '5px'
                        }
                ),
                fac.AntdButton(
                    children = '开始预测',
                    type='primary',
                    id='prediction-button',
                    nClicks=0,
                ),

                fac.AntdText(id='prediction-result'),
            ]),
        ],
        style={
            # col的列宽占页面宽度的大小
            'width': '70%',
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


# 回调函数：点击预测
@app.callback(
    Output('prediction-result', 'children'),
    Input('prediction-button', 'nClicks'),
    State('oneday-observation-input', 'value'),
    prevent_initial_call=True
)
def input_value_callback_demo(nClicks,value):
    if nClicks:
        model_catboost = pickle.load(open("assets/catboost_model.pickle", "rb"))
        list_inputData = value.strip(',').split(',')
        df_inputData = pd.DataFrame(list_inputData).T.values
        prediction = model_catboost.predict(df_inputData)
        if str(prediction) == '[1]':
            return '第二天天气: 下雨🌧'
        elif str(prediction) == '[0]':
            return '第二天天气: 晴朗☀'

# 回调函数：查询某日天气C
@app.callback(
    Output('oneDayWeather-div','children'),
    [
        Input('select-date','value'),
        Input('select-city', 'value'),
    ],
    prevent_initial_call=True
)
def select_date(datevalue,cityvalue):
    # cityvalue经过第一步选择肯定非空，不需要检查
    # 检查日期是否非空,空的话no_update
    if datevalue:
        # 如果没找到选中日期
        if not dateMemory1.strWhetherInDateRange(datevalue):
            return fac.AntdMessage(
                content='您选择的日期没有对应的天气数据！',
                type='error',
            )
        
        # 有选中日期,回调
        else:
            # search
            df_oneday = df_weatherAUS[(df_weatherAUS['Location'] == cityvalue) & (df_weatherAUS['Date'] == datevalue)]
            # deal with NA
            df_oneday = df_oneday.iloc[0,:].map(lambda x: NA2str(x))
            
            if df_oneday.RainToday == 'No':
                imgSrc = 'https://img.icons8.com/color/96/000000/smiling-sun.png'
            else:
                imgSrc = 'https://img.icons8.com/color/96/000000/rainy-weather.png'

            # generate components
            list_components=[
                # 单日天气数据
                # 下雨还是不下雨
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('当日天气', strong=True),
                                style={
                                    # 'backgroundColor': 'rgba(64, 173, 255, 1)',
                                    'color': 'black',
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=8
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdImage(src=imgSrc,preview=False),
                                style={
                                    # 'backgroundColor': 'rgba(64, 173, 255, 1)',
                                    'color': 'white',
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=16
                        ),
                    ],
                    gutter=10
                ),

                # 温度计
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('最低温(°C)', strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=3
                        ),
                        fac.AntdCol(
                            html.Div(
                                daq.Thermometer(
                                    value=df_oneday.MinTemp,
                                    min=0,
                                    max=50,
                                    height=100,
                                    width = 10,
                                    color = 'red',
                                    style={
                                        'margin-bottom': '5%'
                                    }
                                ),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=5
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('最高温(°C)', strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=3
                        ),
                        fac.AntdCol(
                            html.Div(
                                daq.Thermometer(
                                    value=df_oneday.MaxTemp,
                                    min=0,
                                    max=50,
                                    height=100,
                                    width = 10,
                                    color = 'red',
                                    style={
                                        'margin-bottom': '5%'
                                    }
                                ),
                                style={
                                    # 外层无法控制内层颜色
                                    # 'color': 'white',
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=5
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('降雨量(mm)', strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=3
                        ),
                        fac.AntdCol(
                            html.Div(
                                daq.Thermometer(
                                    min=0,
                                    max=30,
                                    height=100,
                                    width = 10,
                                    value=df_oneday.Rainfall,
                                    className='dark-theme-control'
                                ),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=5
                        ),
                    ],
                    gutter=5
                ),

                # 风向加风速
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('上午九点风向(罗经点)', strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=2
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText(df_oneday.WindDir9am, strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=3
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('上午九点风速(km/h)', strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=2
                        ),
                        fac.AntdCol(
                            html.Div(
                                daq.Gauge(
                                    min=0,
                                    max=77,
                                    value=df_oneday.WindSpeed9am,
                                    size = 120,
                                    units='km/h',
                                    showCurrentValue=False,
                                    color="#4c9be8",
                                    style={
                                        "align": "center",
                                        "display": "flex",
                                        "marginTop": "-30%",
                                        "marginBottom": "-40%",
                                    },
                                ),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=5
                        ),

                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('下午三时风向(罗经点)', strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=2
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText(df_oneday.WindDir3pm, strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=3
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('下午三时风速(km/h)', strong=True),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=2
                        ),
                        fac.AntdCol(
                            html.Div(
                                daq.Gauge(
                                    min=0,
                                    max=77,
                                    value=df_oneday.WindSpeed3pm,
                                    size = 120,
                                    units='km/h',
                                    showCurrentValue=False,
                                    color="#4c9be8",
                                    style={
                                        "align": "center",
                                        "display": "flex",
                                        "marginTop": "-30%",
                                        "marginBottom": "-40%",
                                    },
                                ),
                                style={
                                    'height': '150px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=5
                        ),

                    ],
                    gutter=5
                ),

                # 湿度+气压
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('上午九时湿度(%)', strong=True),
                                style={
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=2
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('{}'.format(str(df_oneday.Humidity9am)), strong=True),
                                style={
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=4
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('下午三时湿度(%)', strong=True),
                                style={
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=2
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('{}'.format(str(df_oneday.Humidity3pm)), strong=True),
                                style={
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=4
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('上午九时气压(百帕)', strong=True),
                                style={
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=2
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('{}'.format(str(df_oneday.Pressure9am)), strong=True),
                                style={
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=4
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('下午三时气压(百帕)', strong=True),
                                style={
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=2
                        ),
                        fac.AntdCol(
                            html.Div(
                                fac.AntdText('{}'.format(str(df_oneday.Pressure3pm)), strong=True),
                                style={
                                    'height': '100px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),
                            span=4
                        ),
                    ],
                    gutter=5
                ), #行结束括号

            ]
            return list_components

    return dash.no_update

# 回调函数：下拉菜单选择城市，然后显示日期范围
@app.callback(
    [
        Output('dateRange-warning', 'children'),
        Output('cityAUS-graph', 'figure'),
        Output('select-date', 'disabled'),
        Output('select-date', 'defaultPickerValue'),
        # Output('raw-json', 'children')
    ],
    [
        Input('select-city', 'value'),
    ],
    prevent_initial_call=True
)
def select_city(value):

    # # 获取本轮回调状态下的上下文信息
    # ctx = dash.callback_context

    # # 取出对应State、最近一次触发部件以及Input信息
    # ctx_msg = json.dumps({
    #     'states': ctx.states,
    #     'triggered': ctx.triggered,
    #     'inputs': ctx.inputs
    # }, indent=2)

    # value is a str
    # get onCity's data in weatherAUS.csv
    df_oneCity = df_weatherAUS[df_weatherAUS['Location'] == value]
    # start and end
    startDate = df_oneCity.Date.min().strftime("%Y-%m-%d")
    endDate = df_oneCity.Date.max().strftime("%Y-%m-%d")
    # use dateMemory1 to remember the date range when the callback happen
    dateMemory1.changeDateRange(startDate,endDate)
    


    # update the cityAUS-graph
    # get onCity's geo data in cityAUS.csv
    df_oneCity2geoinfo = df_CityAUS[df_CityAUS['city'] == value]
    fig_CityAUS = go.Figure(data=go.Scattergeo(
        lon = df_oneCity2geoinfo['Long'],
        lat = df_oneCity2geoinfo['Lat'],
        text = df_oneCity2geoinfo['city'],
        mode = 'markers',
        marker_color = 'blue',
        ))

    # select-date 'disabled'启用
    select_date_disabled = False

    # select-date defaultValue设置
    select_date_defaultValue = startDate
    
    return (
        fac.AntdAlert(message='城市{0}可查询的日期范围为{1}至{2}'.format(str(value),startDate,endDate),
        type='warning', showIcon=True,style={'fontSize':'2 rem'}),
        fig_CityAUS,
        select_date_disabled,
        select_date_defaultValue,
        # ctx_msg
    )

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
    