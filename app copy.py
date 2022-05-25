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
        # './assets/css/app.css',
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
teamMembersContent=[
    # 关于我们Divider
    fac.AntdDivider([
        fac.AntdIcon(icon='antd-team',style={'fontSize':'2.5rem'}),
        fac.AntdText('关于我们',strong=True,style={'fontSize':'2.5rem'})]
    ),

    # 卡片网格
    fac.AntdCard(
        [
            fac.AntdCardGrid(
                f'网格{i}',
                style={
                    'width': '25%',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            )
            for i in range(10)
        ],
        title='卡片网格示例',
        style={
            'width': '400px',
            'marginBottom': '10px'
        }
    )

]


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
        return '欢迎来到页面A'

    elif pathname == '/plotsFromData':
        return '欢迎来到页面B'

    elif pathname == '/teamMembers':
        df_membersInfo = getMemberInfo("./data/membersInfo.csv")
        return '欢迎来到页面C'

    else:
        return Page404

if __name__ == '__main__':

    app.run_server(debug=True)