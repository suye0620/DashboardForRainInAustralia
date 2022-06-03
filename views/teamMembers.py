from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
from models.api import getMemberInfo

# team members content
# Although it is a part here, the root path need to keep pace with the app.py
df_membersInfo = getMemberInfo()
teamMembersContent=[
    # '关于我们'Divider
    fac.AntdDivider([
        fac.AntdIcon(icon='fc-conference-call',style={'fontSize':'2.5rem'}),
        fac.AntdText('关于我们',strong=True,style={'fontSize':'2.5rem'})]
    ),

    html.Div(
    fac.AntdCol([
        fac.AntdRow(
            # 卡片网格
            fac.AntdCard([
                # 头像
                fac.AntdAvatar(
                    mode='image',
                    size=100,
                    shape='square',
                    src='{}'.format(url),
                    # style={'margin-left':'1 rem','width':'16 rem'},
                ),
                # 描述
                fac.AntdParagraph('　　{}'.format(df_membersInfo.iloc[i,1]),
                    style={
                        # 'font-weight': 'bold',
                        # 固定文本宽度
                        'width':'70%',
                        # 'font-size': '1.5 rem',
                    }
                )
            ],
            title='{}'.format(df_membersInfo.iloc[i,0]),
            headStyle = {
                'font-weight': 'bold',
                'font-size': '2 rem',
                'justifyContent': 'center',
                'display': 'flex',
            },
            bodyStyle={
                'font-weight': 'bold',
                'font-size': '2 rem',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            hoverable=True,
            # 卡片样式
            style={
                # 卡片撑到row的宽
                'width': '100%',
                # 'justifyContent': 'center',
            }),

            # row 的参数
            # wrap换行
            wrap=True,

            style={
                # antdrow的宽度撑到col的列宽
                'width': '100%',
                
            }
            )
            for i,url in enumerate(['/assets/imgs/sy.png','/assets/imgs/chn.png',
            '/assets/imgs/wpy.png','/assets/imgs/wrz.png','/assets/imgs/lkn.png',
            ])
        ],
        style={
            # col的列宽占页面宽度的大小
            'width': '60%',
        }
    ), #col结束
    # 外层Div样式
    style={
        # 背景颜色与之前保持一致
        'background-color': '#f0f2f5',

        # control div size
        # 'height': '600px',
        'width': '100%',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'start'
    }
    )
]