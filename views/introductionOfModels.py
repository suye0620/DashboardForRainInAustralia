from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
from dash import dcc

# introduction Of Models
introductionOfModelsContent = html.Div(
    html.Div([
        fac.AntdImage(
            src = '/assets/imgs/introductionOfModels/introductionOfModels_{}.png'.format(i+1),
            preview= False,
        ) for i in range(5)
    ],
    style={
        'width': '70%',
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
