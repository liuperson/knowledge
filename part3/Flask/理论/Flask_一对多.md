[TOC]

#### 1.建立模型

```

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    s_name=db.Column(db.String(10),unique=10,nullable=False)
    s_age=db.Column(db.String(100),nullable=True)
    gender=db.Column(db.Boolean,default=1)
    grade_id=db.Column(db.Integer,db.ForeignKey('grade.id'),nullable=True)

    __tablename__ = 'stu'

    def save(self):
        db.session.add(self)
        db.session.commit()


class Grade(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    g_name=db.Column(db.String(10),unique=True,nullable=False)
    student=db.relationship('Student',backref='g')

    __tablename__ = 'grade'

```

#### 2.数据迁移

```
1.navicate中执行sql语句(推荐使用)
2.migrate

1.执行...
alter table stu add grade_id int;
alter table grade add foregin key (grade_id) references grade(id);
```

#### 3.添加数据

```
@blue.route('/create_grade/')
def create_grade():
    grades_names=['LOL','CF','CS','QQFEICHE']
    for name in grades_names:
        g=Grade()
        g.g_name=name
        db.session.add(g)
        db.session.commit()
    return '创建班级成功'
```

