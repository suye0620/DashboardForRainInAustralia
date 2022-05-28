from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架


# plots From Data
plotsFromDataContent = [
    html.Div(
    fac.AntdImage(
        src='/assets/imgs/dashboard.gif',
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
