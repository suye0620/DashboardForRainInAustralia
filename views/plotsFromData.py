from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
# use dcc to generate graphs 
from dash import dcc
import plotly.express as px

df = px.data.iris()
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
        dcc.Graph(figure=fig)
    ],
    # fac.AntdImage(
    #     src='/assets/imgs/dashboard.gif',
    #         preview=True,
    #         # control pic size
    #         style={
    #             'height': '600px',
    #             'width': 'auto',
    #         }
    # ),
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
