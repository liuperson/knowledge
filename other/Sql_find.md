[TOC]

##### 1.普通查询

```
-- 查询数据(行，列)
-- select * from tb_student;

-- 投影
-- select stuname,gender from tb_student;

-- 别名
-- select stuname as 姓名,gender as 性别 from tb_student;
-- select stuname as 姓名,if(gender,'男','女') as 性别 from tb_student;

-- select stuname as 姓名,case gender when 1 then '男' when 0 then '女' else '未知' end as 性别 from tb_student;

--  对列进行运算
-- select concat(stuname,':',tel) as '信息' from tb_student;

-- 筛选
-- select * from tb_student where stuid=1001;
-- select * from tb_student where stuid<>1001;
-- select * from tb_student where stuid in (100,1002,1003);
-- select stuid,stuname,gender from tb_student where stuid>1001;
-- select stuid,stuname,gender from tb_student where gender=1;
-- select * from tb_student where stuid between 1002 and 1003;

-- select * from tb_student where stuid>1002 and gender=1;
-- select * from tb_student where stuid>1002 or gender=0;
-- select * from tb_student where addr is null;
-- select * from tb_student where addr is not null;
-- 注意：判断一个字段是否为null不能用=和<>;

-- 模糊查询(var/varchar)
-- %是一个通配符表示零个或者任意多个字符
-- select * from tb_student where stuname like '白%';
-- select * from tb_student where stuname like '%白%';
-- _也是一个通配符，它表示一个字符
-- select * from tb_student where stuname like '白_';
-- select * from tb_student where stuname like '白__';

-- 排序
-- select * from tb_student order by stuid desc;
-- select * from tb_student order by tel asc;
-- select * from tb_student order by gender asc,stuid desc;
-- select * from tb_student where gender=0 order by stuid desc;

-- 先筛选再排序

-- 限制分页
-- select * from tb_student limit 3;
-- select * from tb_student limit 3 offset 3;
-- select * from tb_student limit 5,5;
-- limit 构造的效果是分页,limit 限制的记录数量 offset 跳过的数量;
-- select * from tb_student where gender=1 order by stuid desc limit 0,3;

-- regexp -regular expression
-- select * from tb_student where stuname regexp '[白王]'

-- 时间查询
select now();
select year(now());
select month(now());
select hour(now());

```

##### 2.复杂查询

```



```