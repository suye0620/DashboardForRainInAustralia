import dash
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架

app = dash.Dash(
    __name__,
    # stylesheet
    external_stylesheets=[
        './assets/css/app.css',
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
        # header
        html.Div(
            [
                # first line: title, logo, github icon
                html.Div(
                    [   
                        html.Div([
                        fac.AntdImage(
                        src='assets/imgs/Australia.jpg',
                        height = 72 ,
                        width = 96 ,
                        ),
                        html.H1("基于澳洲气象数据的短期降水预测", className="app__header__title"),
                        ],style={'display':'inline'}),
                        html.P(
                            "2022春学期大数据案例分析",
                            className="app__header__title--grey",
                        ),
                    ],
                    className="app__header__desc",
                ),
            ],
            className='app__header'
        )
    ],
    className='app__container'
)

if __name__ == '__main__':

    app.run_server(debug=True)