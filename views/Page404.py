from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架

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