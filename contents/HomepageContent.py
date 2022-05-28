from cgitb import strong
from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
from dash import dcc

# Homepage content
# the first bug: 不小心在列表后面加了逗号，导致回调函数以为传的参数是嵌套列表
HomepageContent = [
        # 澳洲风情Divider
        fac.AntdDivider([
            fac.AntdIcon(icon='fc-image-file',style={'fontSize':'2.5rem'}),
            fac.AntdText('澳洲风情',strong=True,style={'fontSize':'2.5rem'})]
        ),
        
        # 走马灯
        fac.AntdCarousel(
            [   
                # 使用Div包裹antdImage，可以调整图片的位置。div一般不设置背景图片
                html.Div(
                    fac.AntdImage(
                        src='/assets/imgs/AustraliaPic{}.jpeg'.format(i+1),
                        preview=False,
                        # control pic size
                        style={
                            'height': '600px',
                            'width': 'auto',
                        }
                    ),
                    style={
                        # 'color': 'white',
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

        # 项目介绍Divider
        fac.AntdDivider([
            fac.AntdIcon(icon='fc-idea',style={'fontSize':'2.5rem'}),
            fac.AntdText('研究背景',strong=True,style={'fontSize':'2.5rem'})]
        ),

        # 项目
        html.Div(
            html.Div([
                fac.AntdParagraph(
                    "　　天气的变化极大地影响着我们每个人的日常生活与工作，所以对来日天气进行预报具有非常重要的意义。\
                    但是，气候气象条件多元与复杂，给精准的天气预报带来了很大的难度。因此，建立精准的短期降雨预测模型一直都是一个气象科学的研究热点。",
                    strong=True
                    ),
                fac.AntdParagraph(['　　',
                    # 图片也可以当图标用
                    fac.AntdImage(src='https://img.icons8.com/color/48/000000/tornado.png',style={'width':'24px'},preview=False),
                    fac.AntdText('自然灾害方面: 降水预测 → 洪涝灾害的防治',)],
                    strong=True
                    ),
                
            ],
            style={
                # 这里的宽度比例是与后面团队介绍板块的比例60%是一致的
                # control internal div size
                # use internal div to typesetting
                'width': '60%',
                'background-color':'white',
            }
            ),
            style={
                # control external div size
                # use external div to divide the page
                'width': '100%',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        )

    ]