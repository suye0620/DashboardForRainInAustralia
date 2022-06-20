# DashboardForRainInAustralia

## About this app

This project is for the class presentation(Big Data Cases Analysis,ZUEL,2022-Spring).

Developer: Ye.S

## How to run this app

(The following instructions apply to Posix/bash. Windows users should check
[here](https://docs.python.org/3/library/venv.html).)

First, clone this repository and open a terminal, such as Powershell.

Create and activate a new virtual environment (recommended, and our Python version in this project: **3.7.12**) by running
the following:

```powershell
python -m venv myvenv
.\myvenv\Scripts\activate
```

Install the requirements:

```powershell
pip install -r requirements.txt
```
Run the app:

```powershell
python app.py
```
Open a browser at http://127.0.0.1:8050 (or other ports)

If you add some new packages to the project, please remember use pip to generate the 'requirements.txt' again.
```powershell
pip freeze > requirements.txt
```

## Some tips on develop Dashboard
1. The folder 'callbacks' is a supplement of 'views', we just withdraw some callbacks functions from 'views', to make the file appear simple and explict

## TO DO
1. 开发响应式的数据呈现表格，为后面使用这些数据进行图表绘制做准备
2. 标签分布表格做起，绘制变量分布等图表，根据时间安排篇幅
3. 完成第二部分模型介绍页面的开发

## Screenshots
1. 使用`Link()`进行页面更新

## LightGBM
  在介绍LightGBM之前，我们有必要先介绍一下同样基于GBDT模型的梯度提升决策树模型XGBoost。XGBoost集成了多棵分类回归树（CART）以弥补单棵 CART 预测精度的不足的问题，是GBDT的改进boosting算法，具有速度快、精度高、能处理大规模数据等优点。然而，由于XGBoost使用Pre-sorted algorithm寻找数据分割点，在计算时占用大量内存，严重影响缓存优化。
  LightGBM在XGBoost的基础上有所提高，它使用Histogram algorithm寻找最佳数据分割点，占用的内存更低，数据分割的复杂度更低。Histogram algorithm寻找最优的分割点的流程如图？所示。
  
![图 2](images/f94da291ffa1a9be34a46b25ae892e47fceeb94d9a01acbab1d0759864c44285.png)  


## 用于二分类的人工神经网络
  人工神经网络,是一种以网络拓扑知识为基础模拟人脑的结构及功能形成一种有效运算模型, 主要包含输入层、隐藏层、输出层三部分。神经网络是由大量节点相互连接构成,每个节点代表一种特定输出函数,每两个节点间的连接都代表通过该连接信号的加权值, 即权重。每层节点对输入信息的加权求和并进行非线性变换后输出,其输出值作为下一层的输入值,以此类推直到最后分类节点。在我们的研究中，我们仅需使用结构较为简单的前馈神经网络，将最后一个输出层调整为类别输出即可。

![图 1](images/ca242b32d9242be0e75b97bc8ff0e0cc5e2f93f2c5f54a69dd522aced3776eda.png)  
