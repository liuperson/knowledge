[TOC]

####1.flask介绍

Flask： 基于python实现的web开发的微框架

Flask：也是基于MVC设计模式

优点：

```
a)有非常齐全的官方文档，上手方便
b)有非常好的拓展机制和三房拓展环境，工作常见软件都有对应拓展
c)微框架的形式给开发者更大选择空间
```

####2.flask安装

##### 2.1环境

```
virtualenv --no-site-packages flaskenv
cd Scipts
activate 环境激活
```

##### 2.2安装

```
pip install flask
```

####3. flask实例

```
创建hello.py
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
	return 'hello,world'

if __name__ == __main__:
	app.run()
运行：python hello.py
```
##### 3.1初始化

```
from flask import flask
app = Flask(__name__)

Flask类构造函数唯一需要的参数就是应用程序的主要模块和包。
大多数应用程序而言：Python的__name__变量就是那个正确的、你需要传递的值。Flask使用这个参数来确定应用程序的根目录，这样以后可以相对这个路径来找到资源文件。
```

#####3.2路由

```
@app.route('/')
客户端例如web浏览器发送请求给web服务，进而将它们发送给Flask应用程序实例。应用程序实例需要知道对于各个URL请求需要运行哪些代码，所以它给Python函数建立了一个URLs映射。这些在URL和函数之间建立联系的操作被称之为路由。

在Flask应程序中定义路由的最便捷的方式是通过显示定义在应用程序实例之上的app.route装饰器，注册被装饰的函数来作为一个 路由。
```

##### 3.3视图函数

```
在上一个示例给应用程序的根URL注册gello_world()函数作为事件的处理程序。如果这个应用程序被部署在服务器上并绑定了 www.example.com 域名，然后在你的浏览器地址栏中输入 http://www.example.com 将触发gello_world()来运行服务。客户端接收到的这个函数的返回值被称为 响应 。如果客户端是web浏览器，响应则是显示给用户的文档。

类似于gello_world()的函数被称作视图函数 。
```

##### 3.4动态名称组件路由

```
你的Facebook个人信息页的URL是 http://www.facebook.com/ ，所以你的用户名是它的一部分。Flask在路由装饰器中使用特殊的语法支持这些类型的URLs。下面的示例定义了一个拥有动态名称组件的路由：

@app.route('/hello/<name>')

def gello_world(name):

	return 'Hello World %s' % name

用尖括号括起来的部分是动态的部分，所以任何URLs匹配到静态部分都将映射到这个路由。当视图函数被调用，Flask发送动态组件作为一个参数。在前面的示例的视图函数中，这个参数是用于生成一个个性的问候作为响应。

在路由中动态组件默认为字符串，但是可以定义为其他类型。例如，路由/user/int:id只匹配有一个整数在id动态段的URLs。Flask路由支持int、float

如下：
@app.route('/hello/<int:id>')

def gello_stu_id(id):

  return 'Hello World id: %s' % id
```

##### 3.5服务启动

```
if __name__ == '__main__':

	app.run()
注意： name == 'main'在此处使用是用于确保web服务已经启动当脚本被立即执行。当脚本被另一个脚本导入，它被看做父脚本将启动不同的服务，所以app.run()调用会被跳过。

一旦服务启动，它将进入循环等待请求并为之服务。这个循环持续到应用程序停止，例如通过按下Ctrl-C。

有几个选项参数可以给app.run()配置web服务的操作模式。在开发期间，可以很方便的开启debug模式，将激活 debugger 和 reloader 。这样做是通过传递debug为True来实现的。

run()中参数有如下：
debug 是否开启调试模式，开启后修改python的代码会自动重启

port 启动指定服务器的端口号

host主机，默认是127.0.0.1
```

#### 4.命令行参数启动

##### 4.1安装插件

```
pip install flask-script

```

调整代码 manager = Manager(app=‘自定义的flask对象’)

启动的地方 manager.run()

#### 4.2 启动命令

```
python hellow.py runserver -h 地址 -p 端口 -d -r

```

其中：-h表示地址。-p表示端口。-d表示debug模式。-r表示自动重启

#### 5. route规则

##### 5.1 规则

写法：converter:variable_name

converter类型：

```
string 字符串
int 整形
float 浮点型
path 接受路径，接收的时候是str，/也当做字符串的一个字符
uuid 只接受uuid字符串
any 可以同时指定多种路径，进行限定

```

例子：

```
@app.route('/helloint/<int:id>/')

@app.route('/getfloat/<float:price>/')

@app.route('/getstr/<string:name>/'，methods=['GET', 'POST'])

@app.route('/getpath/<path:url_path>/')

@app.route('/getbyuuid/<uuid:uu>/'，methods=['GET', 'POST'])

```

实现对应的视图函数：

```
@blue.route('/hello/<name>/')
def hello_man(name):
    print(type(name))
    return 'hello name:%s type:%s' % (name, type(name))

@blue.route('/helloint/<int:id>/')
def hello_int(id):
    print(id)
    print(type(id))
    return 'hello int: %s' % (id)

@blue.route('/index/')
def index():
    return render_template('hello.html')

@blue.route('/getfloat/<float:price>/')
def hello_float(price):

    return 'float: %s' % price

@blue.route('/getstr/<string:name>/')
def hello_name(name):

    return 'hello name: %s' % name

@blue.route('/getpath/<path:url_path>/')
def hello_path(url_path):

    return 'path: %s' % url_path

@blue.route('/getuuid/')
def gello_get_uuid():
    a = uuid.uuid4()
    return str(a)

@blue.route('/getbyuuid/<uuid:uu>/')
def hello_uuid(uu):

    return 'uu:%s' % uu

```

##### 5.2 methods请求方法

常用的请求类型有如下几种

```
GET : 获取
POST : 创建
PUT : 修改(全部属性都修改)
DELETE : 删除
PATCH : 修改(修改部分属性)

```

定义url的请求类型:

```
@blue.route('/getrequest/', methods=['GET', 'POST'])
```

