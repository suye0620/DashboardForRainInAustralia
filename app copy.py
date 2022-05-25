import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架

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
                    size=60,
                    shape='square',
                    src='/assets/imgs/Australia.jpg'
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
                        fac.AntdIcon(icon='antd-github'),
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
                fac.AntdDivider(fac.AntdText('导航栏',strong=True,style={'fontSize':'2.5rem'})),

                # NavigationBar
                fac.AntdLayout(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                            fac.AntdButton(
                                            fac.AntdText('项目简介',strong=True,style={'fontSize':'2 rem'}),
                                            block=True,
                                            type='primary',
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
                                            fac.AntdText('模型简介',strong=True,style={'fontSize':'2 rem'}),
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
                                            fac.AntdText('数据看板',strong=True,style={'fontSize':'2 rem'}),
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
                                            fac.AntdText('团队成员',strong=True,style={'fontSize':'2 rem'}),
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
                    html.Div(

                        fac.AntdCarousel(
                            [
                                html.Div(
                                    f'子元素{i}',
                                    style={
                                        'color': 'white',
                                        'fontSize': '36px',
                                        'height': '400px',
                                        'width': '400px',
                                        'backgroundColor': color,
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                )
                                for i, color in
                                enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
                            ],
                            autoplay=True,
                            effect='fade'
                        ),

                        id = 'render-page-contentrender-page-content',
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        },
                    ),
                    # content area background
                    style={
                        'backgroundColor': 'f0f2f5'
                    }
                ),
            ]                   
        )
    ],
    className='app__container'
)
if __name__ == '__main__':

    app.run_server(debug=True)