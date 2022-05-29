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

        # 研究背景
        html.Div(
            html.Div([

                # importance
                fac.AntdParagraph(
                    "　　天气的变化极大地影响着我们每个人的日常生活与工作，所以对来日天气进行预报具有非常重要的意义。如: ",
                    strong=True
                    ),
                fac.AntdParagraph(['　　',
                    # 图片也可以当图标用
                    fac.AntdImage(src='https://img.icons8.com/color/48/000000/tornado.png',style={'width':'24px'},preview=False),
                    fac.AntdText('自然灾害方面: 降水预测 → 洪涝灾害的防治',)],
                    strong=True
                    ),
                fac.AntdParagraph(['　　',
                    # 图片也可以当图标用
                    fac.AntdImage(src='https://img.icons8.com/color/48/000000/get-in.png',style={'width':'24px'},preview=False),
                    fac.AntdText('日常生活方面: 天气预报 → 安排出行',)],
                    strong=True
                    ),
                fac.AntdParagraph(['　　',
                    # 图片也可以当图标用
                    fac.AntdImage(src='https://img.icons8.com/color/48/000000/rocket--v1.png',style={'width':'24px'},preview=False),
                    fac.AntdText('航空航天方面: 雨雪概率 → 制定航班飞行计划',)],
                    strong=True
                    ),
                fac.AntdParagraph(['　　',
                    # 图片也可以当图标用
                    fac.AntdImage(src='https://img.icons8.com/color/48/000000/carbohydrates.png',style={'width':'24px'},preview=False),
                    fac.AntdText('农业生产方面: 地表径流 → 作物成长、农业',)],
                    strong=True
                    ),
                fac.AntdParagraph(
                    "　　但是，气候气象条件多元与复杂，给精准的天气预报带来了很大的难度。因此，建立精准的短期降雨预测模型一直都是一个气象科学的研究热点。\
                    当前，对于大气降雨的预测的主要的方法有物理测绘方法、传统统计方法、机器学习方法、深度学习方法。",
                    strong=True
                    ),
                # html.Br(),

                # related work
                html.Div(
                    # fill the external 60% div
                    fac.AntdImage(src='/assets/imgs/relatedWorks.png',style = {'width':'100%'},preview=False),
                    style={
                        # control Image div size
                        'height': '500px',
                        # 'width': '100%',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center'
                    }
                ),

                fac.AntdParagraph(
                    "　　本项目中我们将尝试使用机器学习方法进行短期降水预测，下面我们简单介绍一下实验中使用的数据。",
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
        ),
                

        # 数据来源Divider
        fac.AntdDivider([
            fac.AntdIcon(icon='fc-accept-database',style={'fontSize':'2.5rem'}),
            fac.AntdText('数据来源',strong=True,style={'fontSize':'2.5rem'})]
        ),

        html.Div(
            html.Div([
                # target
                fac.AntdParagraph(['　　',
                    # 图片也可以当图标用
                    fac.AntdImage(src='https://img.icons8.com/color/48/000000/goal--v1.png',style={'width':'24px'},preview=False),
                    fac.AntdText('任务目标',)],
                    strong=True
                    ),
                fac.AntdParagraph('　　通过对目标变量 RainTomorrow 训练分类模型来预测次日降雨',
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
        ),
    ]