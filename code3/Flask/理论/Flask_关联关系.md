### 2. 关联关系

#### 2.1 一对多建立模型

学生模型：

```
class Student(db.Model):

    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True)
    s_age = db.Column(db.Integer, default=18)
    s_g = db.Column(db.Integer, db.ForeignKey('grade.g_id'), nullable=True)

    __tablename__ = 'student'

```

班级模型：

```
class Grade(db.Model):

    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), unique=True)
    g_desc = db.Column(db.String(100), nullable=True)
    g_time = db.Column(db.Date, default=datetime.now)
    students = db.relationship('Student', backref='stu', lazy=True)

    __tablename__ = 'grade'

```

官网解释有如下几个lazy的参数：

lazy 决定了 SQLAlchemy 什么时候从数据库中加载数据:，有如下四个值:

**select**/True: (which is the default) means that SQLAlchemy will load the data as necessary in one go using a standard select statement.

**joined**/False: tells SQLAlchemy to load the relationship in the same query as the parent using a JOIN statement.

**subquery**: works like ‘joined’ but instead SQLAlchemy will use a subquery.

**dynamic**: is special and useful if you have many items. Instead of loading the items SQLAlchemy will return another query object which you can further refine before loading the items. This is usually what you want if you expect more than a handful of items for this relationship

```
select就是访问到属性的时候，就会全部加载该属性的数据。

joined则是在对关联的两个表进行join操作，从而获取到所有相关的对象。

dynamic则不一样，在访问属性的时候，并没有在内存中加载数据，而是返回一个query对象, 需要执行相应方法才可以获取对象，

```

#### 2.2

1. 通过班级查询学生信息

   ```
    @grade.route('/selectstubygrade/<int:id>/')
    
    def select_stu_by_grade(id):
        grade = Grade.query.get(id)
    	# 通过班级对象.定义的relationship变量去获取学生的信息
        stus = grade.students
    
        return render_template('grade_student.html',
                               stus=stus,
                               grade=grade
                               )

   ```

2. 通过学生信息查询班级信息

   ```
    @stu.route('/selectgradebystu/<int:id>/')

    def select_grade_by_stu(id):

        stu = Student.query.get(id)
    	# 通过学生对象.定义的backref参数去获取班级的信息
        grade = stu.stu
    
        return render_template('student_grade.html',
                               grade=grade,
                               stu=stu)

   ```

注意：表的外键由db.ForeignKey指定，传入的参数是表的字段。db.relations它声明的属性不作为表字段，第一个参数是关联类的名字，backref是一个反向身份的代理,相当于在Student类中添加了stu的属性。例如，有Grade实例dept和Student实例stu。dept.students.count()将会返回学院学生人数;stu.stu.first()将会返回学生的学院信息的Grade类实例。一般来讲db.relationship()会放在一这一边。

### 3. 数据库迁移

在django中继承了makemigrations，可以通过migrate操作去更新数据库，修改我们定义的models，然后在将模型映射到数据库中。

在flask中也有migrate操作，它能跟踪模型的变化，并将变化映射到数据库中

#### 2.1 安装migrate

```
pip install flask-migrate

```

#### 2.2 配置使用migrate

##### 2.2.1 初始化，使用app和db进行migrate对象的初始化

```
from flask_migrate import Migrate

#绑定app和数据库
Migrate(app=app, db=db)

```

##### 2.2.2 安装了flask-script的话，可以在Manager()对象上添加迁移指令

```
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

manage = Manager(app=app)

manage.add_command('db', MigrateCommand)

```

操作：

```
python manage.py db init  初始化出migrations的文件，只调用一次

python manage.py db migrate  生成迁移文件

python manage.py db upgrade 执行迁移文件中的升级

python manage.py db downgrade 执行迁移文件中的降级

python manage.py db --help 帮助文档
```