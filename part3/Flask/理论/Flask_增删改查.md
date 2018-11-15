[TOC]

语法：

```
类名.query.xxx

```

获取查询集：

```
all()

filter(类名.属性名==xxx)

filter_by(属性名=xxx)

```

数据操作：

```
在事务中处理，数据插入

db.session.add(object)

db.session.add_all(list[object])

db.session.delete(object)

db.session.commit()

修改和删除基于查询
```

#### 1.添加学生

```
@blue.route('/createstu/')
def create_stu():

    s = Student()
    s.s_name = '小花%d' % random.randrange(100)
    s.s_age = '%d' % random.randrange(30)

    db.session.add(s)
    db.session.commit()

    return '添加成功'
提交事务，使用commit提交我们的添加数据的操作
```

#### 2.查询学生

将学生的全部信息获取到，并且返回给页面，在页面中使用for循环去解析即可

```
@blue.route("/getstudents/")
def get_students():
    students = Student.query.all()
    return render_template("StudentList.html", students=students)
```

####3.指定查询 

写法1：

```
students = Student.query.filter(Student.s_id==1)

```

写法2：

```
students = Student.query.filter_by(s_id=2)

```

注意：filter中可以接多个过滤条件

写法3：

```
sql = 'select * from student where s_id=1'
students = db.session.execute(sql)

```

####4.修改学生

写法1：

```
students = Student.query.filter_by(s_id=3).first()
students.s_name = '哈哈'
db.session.commit()

```

写法2：

```
Student.query.filter_by(s_id=3).update({'s_name':'娃哈哈'})

db.session.commit()

```

####5.删除学生

写法1：

```
students = Student.query.filter_by(s_id=2).first()
db.session.delete(students)
db.session.commit()

```

写法2：

```
students = Student.query.filter_by(s_id=1).all()
db.session.delete(students[0])
db.session.commit()
```

注意：filter_by后的结果是一个list的结果集

**重点注意：在增删改中如果不commit的话，数据库中的数据并不会更新，只会修改本地缓存中的数据，所以一定需要db.session.commit()**