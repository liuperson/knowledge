[TOC]

#### 1.Flask模型

```
Flask默认并没有提供任何数据库操作的API

我们可以选择任何适合自己项目的数据库来使用

Flask中可以自己的选择数据，用原生语句实现功能，也可以选择ORM（SQLAlchemy，MongoEngine）

SQLAlchemy是一个很强大的关系型数据库框架，支持多种数据库后台。SQLAlchemy提供了高层ORM，也提供了使用数据库原生SQL的低层功能。

ORM：

将对对象的操作转换为原生SQL
优点
	易用性，可以有效减少重复SQL
	性能损耗少
	设计灵活，可以轻松实现复杂查询
	移植性好
```

针对于Flask的支持，官网地址

```
pip install flask-sqlalchemy
```

安装驱动

```
pip install pymysql
```



#### 2.模型定义

```
使用SQLALchemy的对象去创建字段
其中__tablename__指定创建的数据库的名称
```

```
from flask_sqlalchemy import SQLAlchemy

# 这是对象，不是他自己
db=SQLAlchemy()

# 第一步：声明模型
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),unique=10,nullable=False)
    password=db.Column(db.String(100),nullable=True)
    gender=db.Column(db.Boolean,default=1)

    __tablename__ = 'day02_user'

# 其中：
Integer表示创建的s_id字段的类型为整形，
primary_key表示是否为主键
String表示该字段为字符串
unique表示该字段唯一
default表示默认值
autoincrement表示是否自增

# 第一种 如何将gender更新进去，flaskmigrate
# 第二种 写sql
```

#### 3.配置参数

```
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:1q2w3e4r5t@localhost:3306/flask6"
```

####4.新建数据库

####5.初始化sqlalchemy

```
第一种：
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
db = SQLAlchemy(app)
db.init_app(app)
manage=Manager(app)

if __name__ == '__main__':
    manage.run()
    
第二种：
from App.models import db

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app
```

#### 6.创建数据表

```
@blue.route('/create_db/')
def create_db():
    # 第一次迁移
    db.create_all()
    return '创建模型成功'


@blue.route('/drop_db/')
def drop_db():
    db.drop_all()
    return '删除模型成功'
```
####7.执行查看数据库


