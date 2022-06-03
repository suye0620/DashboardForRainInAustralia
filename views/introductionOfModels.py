from dash import html  # html用于构建Dash应用中最基础的html元素
import feffery_antd_components as fac  # 导入fac框架
from dash import dcc

# introduction Of Models
# 设计：1. 分类模型 2. 评价指标
# 分割标题：divider 小标题：text 文字：markdown
introductionOfModelsContent = html.Div(
    html.Div([
    dcc.Markdown('''
        # LightGBM
        在介绍LightGBM之前，我们有必要先介绍一下同样基于GBDT模型的梯度提升决策树模型XGBoost。XGBoost集成了多棵分类回归树（CART）以弥补单棵 CART 预测精度的不足的问题，是GBDT的改进boosting算法，具有速度快、精度高、能处理大规模数据等优点。然而，由于XGBoost使用Pre-sorted algorithm寻找数据分割点，在计算时占用大量内存，严重影响缓存优化。LightGBM在XGBoost的基础上有所提高，它使用Histogram algorithm寻找最佳数据分割点，占用的内存更低，数据分割的复杂度更低。Histogram algorithm寻找最优的分割点的流程如图所示。

        ### ![](/assets/imgs/AustraliaPic1.jpeg)

        ''',
        style={
            'font-weight':'bold',
            'font-size':'2 rem'
        },
        dangerously_allow_html=True,
        dedent=True)
    ],
    style={
        'width': '60%',
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
