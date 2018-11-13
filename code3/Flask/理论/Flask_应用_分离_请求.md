1)flask最小应用

```
from flask import Flask

app=Flask(__name__)

@app.route('/hello')
def hello():
	return '你好，双十一'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080,debug=True)

1.导入Flask模块，类的实例应用在WSGI应用
2.创建类的实例，第一个参数是应用模块或者包的名称，如果使用的是单一模块，那应该使用__name__，因为模块的名称将会因其作为单独应用启动或者是模块导入而不同，这是必须的，因为这样才能让flask知道到哪里去找模板、静态文件等等。
3.接下来就是用装饰器route()告诉flask什么样的路由url可以触发我们定义的函数，这个函数的名字也会在生成url时被特定的函数采用，函数返回我们想要的内容并且显示出来
4.最后，用run()函数来让应用运行在本地服务器上，实例运行，app.run(定义主机端口等信息)
```

2)安装

```
req.txt
	flask
	flask-script

在flaskenv中执行  pip install -r req.txt
```

3)使用flask_script的Manager模块

```
from flask-script import Manager

manage=Manager(app)

manage.run()

在flaskenv中执行 python firstflask.py -p 8080 -h 0.0.0.0 -d

在这里，p代表port,h代表host,d代表debug
先导入manager ,使用manage来管理类app,然后运行函数，这样做肯定是不方便的

设置 runserver -p 8080 -d 
```

4)路由匹配规则

```
# 路由匹配规则 <选择器:参数名>
选择器有int: 表示接受的参数为int类型
没有定义选择器: 表示接受的参数为string类型（默认）
选择器string: 表示接受的参数一定为string类型
选择器 uuid/path/float
```

5)蓝图、分离

```
1.修改firstflask.py为manage.py
2.增加views.py文件
3.在req.txt增加flask-blueprint,使用蓝图来管理路由

from flask import Blueprint

# 第一步：在views.py里面app_blueprint=Blueprint('app',__name__)
# 第二步，在manage.py里注册蓝图 app.register_blueprint(blueprint=app_blueprint,url_prefix='/app')

#这里就不再使用@app.route(),改为@app_blueprint.route('/hello')

先是引入蓝图，然后生成蓝图对象，使用蓝图对象管理路由，不同模块生成不同的对象，然后注册路由，用户模块，加前缀，每个模块对应不同的前缀，url_prefix,现在访问地址的时候，就看注册路由，自动匹配路由地址，执行视图函数
```

6)跳转

```
@app_blueprint.route('/redirect/')
def redirect_url():
	#引入redirect,url_for
	#Flask写法：redirect(url_for('蓝图名称.跳转函数名'))
	return redirect(url_for('app.hello',id=10))
```

7)请求

```
程序如何来接收请求和响应，接收以后如何进行数据的解析，增删改查
@app_blueprint.route('/hello',methods=['GET','POST'])
def hello():
	if request.method == 'GET':
		return '你好GET'
	if request.method == 'POST':
		return '你好POST'

request请求
获取get:request.args
获取post:request.form
上传文件:request.files
请求路径:request.path
请求方式：request.method
```

8)响应

```
响应，可以在其中设置cookie,cookie的增删改查
@app_blueprint.route('/make_response/',methods=['GET'])
def make_my_response():
	res=make_response('<h2>天气好</h2>',200)
	return res
	
res.set_cookie()
res.delete_cookie()
在浏览器里面做缓存，或者是在cookie里操作数据
```

9)异常抛出捕获

```
@app_blueprint.route('/abort_a/',methods=['GET','POST'])
def abort_a():
    try:
        a=request.form.get('a')
        b=request.form.get('b')
        c=a/int(b)
        return '%s/%s=%s' % (a, b, c)
    except Exception as e:
        abort(500)

@app_blueprint.errorhandler(500)
def error_handler(error):
    # TODO:返回定制的错误页面
    return 'Excption is %s'% error
```
