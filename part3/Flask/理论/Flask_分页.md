[TOC]

#### 1.函数

在这里，是先要获取学生信息的数据，然后将数据进行整理，并且传递给页面，让页面来进行解析，然后将数据展示出来。

```
def stu_page():
    page = int(request.args.get('page', 1))
    
     
    # # 1. offset+limit
    # stus = Student.query.offset((page - 1) * 2).limit(2)
    # # 2. 切片
    # stus = Student.query.all()[(page - 1) * 2:page * 2]
    # # 3. sql
    # sql = 'select * from Student limit %s,%s' % ((page - 1) * 2, 2)
    # stus = db.session.execute(sql)
    
    
    # 4. paginate()方法
    paginate = Student.query.paginate(page, 2)
    stus = paginate.items
    return render_template('stus.html', stus=stus, paginate=paginate)
```

#### 2.数据解析

在获取到后端传递的数据后，在前端设置分页的a标签，然后进行分页的具体操作

```
<table>
        <thead>
            <th>ID</th>
            <th>姓名</th>
            <th>年龄</th>
        </thead>
        <tbody>
            {% for stu in stus %}
                <tr>
                    <td>{{ stu.id }}</td>
                    <td>{{ stu.s_name }}</td>
                    <td>{{ stu.s_age }}</td>
                </tr>
            {% endfor %}
        </tbody>
</table>
	<br>
    <p>当前{{ paginate.page }}页，共有{{ paginate.pages }}页</p>
    {% if paginate.has_prev %}
        <a href="{{ url_for('user.stu_page') }}?page={{ paginate.prev_num }}">上一页</a>
    {% endif %}

    {% for i in paginate.iter_pages() %}
        <a href="{{ url_for('user.stu_page') }}?page={{ i }}">{{ i }}</a>
    {% endfor %}

    {% if paginate.has_next %}
        <a href="{{ url_for('user.stu_page') }}?page={{ paginate.next_num }}">下一页</a>
    {% endif %}    
```

