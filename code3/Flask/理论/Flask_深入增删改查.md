### 数据库增删改查

定义模型，并定义初始化的函数：

```
class Student(db.Model):

    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16), unique=True)
    s_age = db.Column(db.Integer, default=1)

    __tablename__ = "student"

    def __init__(self, name, age):
        self.s_name = name
        self.s_age = age
```

#### 1.1 增--批量增加

第一种方式：

```
@blue.route('/createstus/')
def create_users():
    stus = []
    for i in range(5):
		# 实例化Student的对象
        s = Student()
		# 对象的属性赋值
        s.s_name = '张三%s' % random.randrange(10000)
        s.s_age = '%d' % random.randrange(100)
        stus.append(s)
	# 添加需要创建的数据
    db.session.add_all(stus)
	# 提交事务到数据库
    db.session.commit()

    return '创建成功'

```

注：在创建单条数据的时候使用db.session.add()，在创建多条数据的时候使用db.session.add_all()

第二种方式：

```
@blue.route('/createstus/')
def create_users():
    stus = []
    for i in range(5):
		# 使用类的初始化去创建Student对象
        s = Student('张三%s' % random.randrange(10000),
                    '%d' % random.randrange(100))
        stus.append(s)

    db.session.add_all(stus)
    db.session.commit()

    return '创建成功'

```

#### 1.2 查--使用运算符

获取查询集

```
filter(类名.属性名.运算符(‘xxx’))

filter(类名.属性 数学运算符  值)

```

运算符：

```
contains： 包含
startswith：以什么开始
endswith：以什么结束
in_：在范围内
like：模糊
__gt__: 大于
__ge__：大于等于
__lt__：小于
__le__：小于等于

```

筛选：

```
offset()

limit()

order_by()

get()

first()

paginate()

```

逻辑运算：

```
与
	and_
	filter(and_(条件),条件…)

或
	or_
	filter(or_(条件),条件…)

非
	not_
	filter(not_(条件),条件…)

```

例子1：

1. 查询学生的id为3，4，5，6，16的的学生信息，使用**in_逻辑运算**

   ```
    @blue.route('/getstubyids/')
    def get_stu_by_ids():

    	students = Student.query.filter(Student.s_id.in_([3,4,5,6,16]))
    	return render_template('StudentList.html', students=students)

   ```

2. 查询学生的年龄小于18岁的学生的信息

   ```
    Student.query.filter(Student.s_age < 18)

   ```

3. 查询学生的年龄小于18岁的学生的信息，**__lt__小于**

   ```
    students = Student.query.filter(Student.s_age.__lt__(15))

   ```

4. 查询学生的年龄小于等于18岁的学生的信息，**__le__小于等于**

   ```
    students = Student.query.filter(Student.s_age.__le__(15))

   ```

5. 查询学生的姓名以什么开始或者以什么结尾的学生的信息**startswith和endswith**

   ```
    students = Student.query.filter(Student.s_name.startswith('张'))
    students = Student.query.filter(Student.s_name.endswith('2'))

   ```

6. 查询id=4的学生的信息

   ```
    Student.query.get(4)
    获取的结果是学生的对象

   ```

7. 模糊搜索like

   ```
    %：代表一个或者多个
    _：代表一个
    
    Student.query.filter(Student.s_name.like('%张%')) 

   ```

8. 分页，查询第二页的数据4条

   ```
    第一个参数是那一页，第二个参数是一页的条数，第三个参数是是否输出错误信息
    students = Student.query.paginate(2, 4, False).items

   ```

例子2：

跳过offset几个信息，截取limit结果的几个值

```
# 按照id降序排列
stus = Student.query.order_by('-s_id')

# 按照id升序排列
stus = Student.query.order_by('s_id')
stus = Student.query.order_by(asc('s_id'))
stus = Student.query.order_by('s_id asc')

# 按照id降序获取三个
stus = Student.query.order_by('-s_id').limit(3)
stus = Student.query.order_by('s_id desc').limit(3)

from sqlalchemy import desc
stus = Student.query.order_by(desc('s_id')).limit(3)

# 获取年龄最大的一个
stus = Student.query.order_by('-s_age').first()

# 跳过3个数据，查询5个信息
stus = Student.query.order_by('-s_age').offset(3).limit(5)

# 跳过3个数据
stus = Student.query.order_by('-s_age').offset(3)

# 获取id等于24的学生
stus = Student.query.filter(Student.s_id==24)
stus = Student.query.get(24)

```

例子3：

1. 查询

   from sqlalchemy import and_, or_, not_

   **查询多个条件**

   stus = Student.query.filter(Student.s_age==18, Student.s_name=='雅典娜')

   **and_ 并且条件**

   stus = Student.query.filter(and_(Student.s_age==18, Student.s_name=='雅典娜'))

   **or_ 或者条件**

   stus = Student.query.filter(or_(Student.s_age==18, Student.s_name=='火神'))

   **not_ 非**

   stus = Student.query.filter(not_(Student.s_age==18), Student.s_name=='火神')

   查询姓名不包含'可爱‘，并且年龄不等于12的学生

   stus = Student.query.filter(not_(Student.s_name.contains('可爱')), not_(Student.s_age == 12))

例子4：

**分页：**

[![图](https://github.com/coco369/knowledge/raw/master/flask/images/flask_sqlalchemy_paginate.png)](https://github.com/coco369/knowledge/blob/master/flask/images/flask_sqlalchemy_paginate.png)

后端数据处理：

```
# 方法一：手动实现分页，使用offset和limit
page = int(request.args.get('page', 1))
stus = Student.query.offset((page-1)*5).limit(5)

# 方法二： 使用切片[:]
s_page = (page - 1)*5
e_page = page * 5
stus = Student.query.all()[s_page: e_page]

# 方法三：使用paginate
# 查询第几页的数据	
page = int(request.args.get('page', 1))

# 每一页的条数多少，默认为10条
per_page = int(request.args.get('per_page', 10))

# 查询当前第几个的多少条数据
paginate = Student.query.order_by('-s_id').paginate(page, per_page, error_out=False)

stus = paginate.items

```

前端数据展示：

```
<h2>学生信息</h2>
{% for stu in stus %}
    id：{{ stu.s_id }}
    姓名：{{ stu.s_name }}
    年龄：{{ stu.s_age }}
    <br>
{% endfor %}
<br>
总页数: {{ paginate.pages }}
<br>
一共{{ paginate.total }}条数据
<br>
当前页数：{{ paginate.page }}
<br>
{% if paginate.has_prev %}
    <a href="/stupage/?page={{ paginate.prev_num }}">上一页</a>：{{ paginate.prev_num }}
{% endif %}

{% if paginate.has_next %}
    <a href="/stupage/?page={{ paginate.next_num }}">下一页</a>：{{ paginate.next_num }}
{% endif %}
<br>

<br>
页码：{% for i in  paginate.iter_pages() %}
        <a href="/stupage/?page={{ i }}">{{ i }}</a>
    {% endfor %}
```