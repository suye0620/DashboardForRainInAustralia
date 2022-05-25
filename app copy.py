import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
from dash import dcc
import feffery_antd_components as fac  # 导入fac框架
from dash.dependencies import Input, Output
from models.func import getMemberInfo

app = dash.Dash(
    __name__,
    # stylesheet
    external_stylesheets=[
        './assets/css/style.css',
        ],

    # meta tags
    meta_tags=[
        {"charset":"utf-8"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

# Page title
app.title = "Rain in Australia"

# server = app.server

# app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

app.layout = html.Div(
    [
        fac.AntdLayout(
            [   
                # header
                fac.AntdHeader([
                    fac.AntdAvatar(
                    mode='image',
                    size=80,
                    shape='square',
                    src='/assets/imgs/academyLogo.png'
                    ),
                    fac.AntdTitle(
                        '基于澳洲气象数据的短期降水预测',
                        level=1,
                        style={
                            'color': 'black',
                            'margin': '0',
                            # 'fontSize': '4.5 rem',
                        }
                    ),
                    fac.AntdButton(
                        fac.AntdIcon(icon='antd-github',style={'fontSize':'1.5rem'}),
                        shape = 'circle',
                        href = 'https://github.com/suye0620/DashboardForRainInAustralia',
                        # style={"margin-top":'0 rem'}
                        )
                    ],
                    style={
                        'margin-top': '2rem',
                        'margin-left': '1rem',
                        'display': 'flex',
                        'justifyContent': 'left',
                        'alignItems': 'center',
                        'background-color': '#f0f2f5',
                    }
                ),

                # Divider
                fac.AntdDivider([
                                fac.AntdIcon(icon='antd-send',style={'fontSize':'2.5rem'}),
                                fac.AntdText(' 导航栏 ',strong=True,style={'fontSize':'2.5rem'})
                                ]),

                # NavigationBar
                dcc.Location(id='url'),
                fac.AntdLayout(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                            fac.AntdButton(
                                            dcc.Link(
                                                fac.AntdText('项目简介',strong=True,style={'fontSize':'2 rem'}),
                                                # link to homepage
                                                href = '/',
                                                # refresh = True,
                                                ),                                            
                                            block=True,
                                            type='default',
                                            # shape='round',
                                            size='large',
                                            ),
                                        style={
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        },
                                    ),
                                    span=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                            fac.AntdButton(
                                            dcc.Link(
                                                fac.AntdText('模型选用',strong=True,style={'fontSize':'2 rem'}),
                                                # link to homepage
                                                href = '/introductionOfModels',
                                                # refresh = True,
                                                ),
                                            block=True,
                                            type='default',
                                            # shape='round',
                                            size='large',
                                            ),
                                        style={
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                            fac.AntdButton(
                                            dcc.Link(
                                                fac.AntdText('数据看板',strong=True,style={'fontSize':'2 rem'}),
                                                # link to homepage
                                                href = '/plotsFromData',
                                                # refresh = True,
                                                ),
                                            block=True,
                                            type='default',
                                            # shape='round',
                                            size='large',
                                            ),
                                        style={
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                            fac.AntdButton(
                                            dcc.Link(
                                                fac.AntdText('团队成员',strong=True,style={'fontSize':'2 rem'}),
                                                # link to homepage
                                                href = '/teamMembers',
                                                # refresh = True,
                                                ),
                                            block=True,
                                            type='default',
                                            # shape='round',
                                            size='large',
                                            ),
                                        style={
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=6
                                ),
                            ],
                            gutter=1
                        )
                    ]
                ),

                # content area
                fac.AntdContent(
                    # fac.AntdLayout(
                    # ),

                    # content area background
                    id = 'render-page-content',
                    style={
                        'backgroundColor': '#f0f2f5'
                    }
                ),
            ]                   
        )
    ],
    className='app__container'
)

# Homepage content
# the first bug: 不小心在列表后面加了逗号，导致回调函数以为传的参数是嵌套列表
HomepageContent = [
        # 澳洲风情Divider
        fac.AntdDivider([
            fac.AntdIcon(icon='antd-cloud',style={'fontSize':'2.5rem'}),
            fac.AntdText('澳洲风情',strong=True,style={'fontSize':'2.5rem'})]
        ),
        
        # 走马灯
        fac.AntdCarousel(
            [   
                # 使用Div包裹antdImage，可以调整图片的位置。div一般不设置背景图片
                html.Div(
                    fac.AntdImage(
                        src='./assets/imgs/AustraliaPic{}.jpeg'.format(i+1),
                        preview=False,
                        # control pic size
                        style={
                            'height': '600px',
                            'width': 'auto',
                        }
                    ),
                    style={
                        'color': 'white',
                        'fontSize': '36px',
                        # control div size
                        'height': '600px',
                        'width': '100%',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center'
                    }
                )
                for i, color in enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
            ],
            autoplay=True,
            effect='fade'
        ),
    ]

# Page 404
Page404 = [
    html.Div(
        fac.AntdImage(
            src='./assets/imgs/404.webp',
            preview=False,
            # control pic size
            style={
                'height': '600px',
                'width': 'auto',
            }
        ),
        style={
            'color': 'white',
            'fontSize': '36px',
            # control div size
            'height': '600px',
            'width': '100%',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center'
        }
    )
]

# team members content
df_membersInfo = getMemberInfo("./data/membersInfo.csv")
teamMembersContent=[
    # 关于我们Divider
    fac.AntdDivider([
        fac.AntdIcon(icon='antd-team',style={'fontSize':'2.5rem'}),
        fac.AntdText('关于我们',strong=True,style={'fontSize':'2.5rem'})]
    ),

    html.Div(
    fac.AntdCol([
        fac.AntdRow(
            # 卡片网格
            fac.AntdCard([
                # 头像
                fac.AntdAvatar(
                    mode='image',
                    size=100,
                    shape='square',
                    src='{}'.format(url)
                ),
                # 描述
                fac.AntdParagraph('{}'.format(df_membersInfo.iloc[i,1]))
            ],
            title='{}'.format(df_membersInfo.iloc[i,0]),
            headStyle = {
                'font-weight': 'bold',
                'justifyContent': 'center',
                'display': 'flex',
            },
            bodyStyle={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            hoverable=True,
            # 卡片样式
            style={
                # 卡片撑到row的宽
                'width': '100%',
                # 'justifyContent': 'center',
            }),

            # row 的参数
            # wrap换行
            wrap=True,

            style={
                # row撑到col的列宽
                'width': '100%',
                
            }
            )
            for i,url in enumerate(['/assets/imgs/sy.png','/assets/imgs/chn.png',
            '/assets/imgs/wpy.png','/assets/imgs/wrz.png','/assets/imgs/lkn.png',
            ])
        ],
        style={
            # col的列宽占页面宽度的大小
            'width': '60%',
            
        }
    ), #col结束
    # 外层属性
    style={
        'background-color': '#f0f2f5',

        # control div size
        # 'height': '600px',
        'width': '100%',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'start'
    }
    )
]

# plots From Data
plotsFromDataContent = [
    html.Div(
    fac.AntdImage(
        src='./assets/imgs/dashboard.gif',
            preview=True,
            # control pic size
            style={
                'height': '600px',
                'width': 'auto',
            }
    ),
    style={
        # control div size
        'height': '600px',
        'width': '100%',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    }
    )
]

# introduction Of Models
introductionOfModelsContent = html.Div(
    html.Div([
    dcc.Markdown('''
## LightGBM
在介绍LightGBM之前，我们有必要先介绍一下同样基于GBDT模型的梯度提升决策树模型XGBoost。XGBoost集成了多棵分类回归树（CART）以弥补单棵 CART 预测精度的不足的问题，是GBDT的改进boosting算法，具有速度快、精度高、能处理大规模数据等优点。然而，由于XGBoost使用Pre-sorted algorithm寻找数据分割点，在计算时占用大量内存，严重影响缓存优化。LightGBM在XGBoost的基础上有所提高，它使用Histogram algorithm寻找最佳数据分割点，占用的内存更低，数据分割的复杂度更低。Histogram algorithm寻找最优的分割点的流程如图所示。

![]('https://pic2.zhimg.com/v2-974aa7fb3ad236e22ec0b702316d00ac_1440w.jpg')

''',
        dangerously_allow_html=True,
        dedent=True)
    ],
    style={
        'width': '60%',
        'background-color':'white',
    }
    ),
    style={
        # control div size
        'width': '100%',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    }
)

# callback functions
# multi-pages
@app.callback(
    Output('render-page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/':
        return HomepageContent

    if pathname == '/introductionOfModels':
        return introductionOfModelsContent

    elif pathname == '/plotsFromData':
        return plotsFromDataContent

    elif pathname == '/teamMembers':
        return teamMembersContent

    else:
        return Page404

if __name__ == '__main__':

    app.run_server(debug=True)
    # app.run_server(debug=False)