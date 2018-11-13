[TOC]

#### 1.jinja2

```
Flask中使用jinja2模板引擎

jinja2是由Flask作者开发，模仿Django的模板引擎

优点：

速度快，被广泛使用

HTML设计和后端python分离

非常灵活，快速和安全

提供了控制，继承等高级功能
```



####1.static的引入方式

```
{% block css %}
<!--引入static中的css-->
<!--第一种-->
<link href="/static/css/style.css"rel="stylesheet">

<!--第二种-->
<!--<link href="{{ url_for('static', filename='css/style.css') }}">-->
{% endblock %}
```
#### 3.super继承方式

```
{% block css %}
    {{ super() }}
{% endblock %}
```

#### 4.loop循环

```
{% for i in content %}
        <!--第一次循环-->
        <!--没有ifequeal-->        
        <h5>
        编号：{{ loop.index }}
        {% if loop.index == 1 %}
           <span style="color: red">内容：{{ i }}</span>
        {% else %}
            内容：{{ i }}
        {% endif %}
        
        是否循环第一次：{{ loop.first }}
        是否循环最后一次：{{ loop.last }}
        </h5>       
{% endfor %}

loop.first
loop.last
loop.index
loop.revindex
```
#### 5.functions函数

```
<!--声明函数-->
{% macro hello() %}
    <p>你好妹子</p>
{% endmacro %}


{% macro say(name) %}
    <p>你好,{{ name }}</p>
{% endmacro %}

单独的py文件，其他html只需要引入就好
引入方法：
	{% from 'functions.html' import hello %}
    {{ hello() }}
```

#### 6.过滤器

```
定义函数
@blue.route('/temp/')
def temp():
    content=['Python','Flask','Django','Tornado','Sanic','Twisted']
    content_h2='<h2>我是h2标题</h2>'
    content_h22='    <h2>我是h2标题</h2>    '
    return render_template('temp.html',title='模板语法',
                           content=content,
                           content_h2=content_h2,
                           content_h22=content_h22)
{{ 变量|过滤器|过滤器... }}
capitalize 单词首字母大写
lower 单词变为小写
upper 单词变为大写
title
trim 去掉字符串的前后的空格
reverse 单词反转
format
striptags 渲染之前，将值中标签去掉
safe 讲样式渲染到页面中
default
last 最后一个字母
first
length
sum
sort
```

#### 7.sql模型

```
pip install sqlalchemy
pip install pymysql
模型定义配置，模型迁移，模型关联关系
```