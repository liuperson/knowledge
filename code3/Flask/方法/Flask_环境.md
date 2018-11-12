day01: 

1）flask环境:
	1. 创建虚拟环境 flaskenv6
		virtualenv --no-site-packages -p xxxx flaskenv6
	2. 安装flask
		pip install flask

2）最小应用，创建hello.py文件:

	from flask import Flask
	app = Flask(__name__)
	
	@app.route('/')
	def hello():
		return 'hello'
	
	if __name__ == '__main__':
		app.run(host，port，debug)

3）默认启动命令: python hello.py 
   默认id和端口: 127.0.0.1:5000

4) 使用flask_script的Manager模块

	from flask import Flask
	from flask_script import Manager
	app = Flask(__name__)
	
	@app.route('/')
	def hello():
		return 'hello'
	
	manege = Manager(app)
	
	if __name__ == '__main__':
		manage.run()
	
	启动命令: python helLo.py runserver -h IP -p PORT -d

5) 分离出视图层，业务逻辑。从hello.py中分离出路由和视图函数。
​	
	使用蓝图管理路由，蓝图的好处就是模块化管理应用

	from flask import Blueprint
	# 第一步，获取蓝图对象
	blue = Blueprint('yyy', __name__)
	# 管理路由
	@blue.route('/')
	def xxx():
		pass
	
	# 第二步，注册蓝图
	app.register_blueprint(blueprint=blue, url_prefix='xxx')

6) 跳转
	url_for('蓝图别名.跳转的函数名')
	redirect(url_for('yyy.xxx'))

7) 请求与响应
	# request请求
	获取get传参: request.args
	获取post传参：request.form
	获取上传文件: request.files
	获取路径: request.path
	请求方式: request.method
	
	# 响应response，是后端产生返回给前端（浏览器）
	make_response(响应内容，响应状态码（默认为200）)
	响应绑定cookie，set_cookie/delete_cookie

8）异常抛出与捕获
​	
	抛出：abort(状态码)
	捕获: @blue.errorhandler(状态码)

9）路由规则
	# 路由匹配规则 <选择器:参数名>
	选择器有int: 表示接受的参数为int类型
	没有定义选择器: 表示接受的参数为string类型（默认）
	选择器string: 表示接受的参数一定为string类型
	选择器 uuid/path/float