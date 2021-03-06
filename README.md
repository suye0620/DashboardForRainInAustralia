# DashboardForRainInAustralia

☞[click me to visit it](http://150.158.97.38:5000/)

## About this app

This project is for the class presentation(Big Data Cases Analysis,ZUEL,2022-Spring).

Developer: Ye.S

**project structure:**

**assets:** store some static files such as images, css style sheets and the ML model

**callbacks:** define some callback functions

**models:** data and some useful api

**views:** define the layout of all pages

**source_code_of_ML_models:** source code we used in model training

app.py: index page and startup file

server.py: define some details of the Dash app

paper.pdf: brief introduction of our project

tools.py: some small tools to process data

requirements.txt: list the packages and their versions we used in this project

## How to run this app

(The following instructions apply to Posix/bash. Windows users should check
[here](https://docs.python.org/3/library/venv.html).)

First, clone this repository and open a terminal, such as Powershell.

Create and activate a new virtual environment (recommended, and our developing Python version in this project: **3.7.12**) , and run
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

If you add some new packages to the project, please remember use pip to generate the 'requirements.txt' again (when you use the virtual environment).
```powershell
pip freeze > requirements.txt
```

## Some tips on develop Dashboard
1. The folder 'callbacks' is a supplement of 'views', we just withdraw some callbacks functions from 'views', to make the file appear simple and explict
2. [Documentation 1:（数据科学学习手札123）Python+Dash快速web应用开发](https://www.cnblogs.com/feffery/tag/Dash/)
3. [Documentation 2: feffery-antd-components official documentation](http://fac.feffery.tech/getting-started)