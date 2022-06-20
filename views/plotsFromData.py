from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
# import dash_bootstrap_components as dbc # 导入dbc，用于绘制表格
# use dcc to generate graphs 
from dash import dcc
import plotly.express as px

df = px.data.iris()
df.insert(0, 'index', df.index)
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]

fig = px.scatter_matrix(
    df,
    dimensions=features,
    color="species"
)
fig.update_traces(diagonal_visible=False)

# plots From Data
plotsFromDataContent = [
    html.Div([
        dcc.Graph(figure=fig),
        html.Br(),
        fac.AntdTable(
            id='dash-table',
            data=df.to_dict('records'),
            # 列表生成式
            columns=[
                {'title': column, 'dataIndex': column} for column in df.columns
            ],
            # size=15,  # 设置单页显示15行记录行数
            # style_header={
            #     'font-family': 'Times New Roman',
            #     'font-weight': 'bold',
            #     'text-align': 'center'
            # },
            # style_data={
            #     'font-family': 'Times New Roman',
            #     'text-align': 'center'
            # }
        )

        # dcc.Graph(
        #     figure = fig,
        #     id = 'y_label_chart'
        # ),
    ],
    style={
        # control div size
        'width': '100%',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    }
    )
]
