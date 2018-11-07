[TOC]

##### 1.xx

```
分布式爬虫
1.爬虫一定是在服务器上运行的，不能是自己的电脑
2.联合开发最主要工作是写接口
3.分开的，横向和纵向扩展，横向就加人，纵向就加机器性能，行业倾向是横向的扩展，纵向的话机器有限制
4.业务量的大小来决定服务器设备多少
5.队列，任务先进先出，可以放在那里先不做，有调度器，一般就有队列
但是scrapy,里面呢其实就是列表来实现的，区分不同的请求，实际上放相同的请求，其实就一个。
把所有信息转字符串，转成哈希值，通过哈希，判断是否一样的请求。
6.一台机器写多个scrapy,其实也可以
7.不同机器共享一个队列，就很容器取完。

```

```
爬取队列：使用redis有序集合
去重：使用redis保存request指纹，提供过滤了的
中断续爬：调度器从redis队列中取没有爬过的
单击爬虫，队列在内存，分布式在redis

```

```
scrapy 本身是没有分布式能力
pip install scrapy-redis -i 豆瓣镜像

redis-cli -h 138.138.138.138 -p 6379

ZRANGE comic:

```

```
settings参数
SCHEDULER='scrapy_redis.scheduler.Scheduler'
DUPEFITER_CLASS='scrapy_redis.dupefilter.RFPDupeFilter'
```
```
分布式的原理：schender，去共同一台机器上拿请求
```
```
from student left join course
student 就是左
from course right join student 
course 就是右

sql连接查询
4种
1.内连接inner join
	--两张表都有的记录才显示出来
2.左连接left join
	--左边的记录全部出来，右边没有匹配的记录，用空来代替
3.右连接right join
	--右边的记录全部出来，左边没有匹配的记录，用空来代替
4.全连接full join(mysql没有)
	--两边的记录都出来，互相没有匹配的用空来代替

```