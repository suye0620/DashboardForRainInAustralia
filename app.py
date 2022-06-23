import dash
from dash import dcc
# import app
from server import app

# html用于构建Dash应用中最基础的html元素
from dash import html

# load fac framework
import feffery_antd_components as fac 

# Requriements for callback functions
from dash.dependencies import Input, Output 

# all contents of each view are as follows
from views.Homepage import HomepageContent
from views.introductionOfModels import introductionOfModelsContent
from views.Page404 import Page404
from views.plotsFromData import plotsFromDataContent
from views.teamMembers import teamMembersContent



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
                                fac.AntdIcon(icon='fc-menu',style={'fontSize':'2.5rem'}),
                                fac.AntdText(' 导航栏 ',strong=True,style={'fontSize':'2.5rem'})
                                ]),

                # NavigationBar
                # multi-page anchor point
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

# 其余的回调函数我们放到callback包
# multi-pages(路由总控)
@app.callback(
    Output('render-page-content', 'children'),
    Input('url', 'pathname'),

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

    # app.run_server(debug=True)
    app.run_server(debug=False)