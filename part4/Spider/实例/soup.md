[TOC]


```
xpath

Xml Path Language Xml 路径语言
```

```
安装lxml库(支持htnl和xml解析，支持xpath解析方式)
pip install lxml -i https://pypi.douban.com/simple
```

```
pip install beautifulsoup4

Python 标准库 BeautifulSoup(html, “html.parser”) 速度⼀般，容错能⼒好
lxml HTML解析器 BeautifulSoup(html, “lxml”) 速度快，容错好
lxml xml解析器 BeautifulSoup(markup, “xml”) 速度快，唯⼀⽀持xml
html5lib BeautifulSoup(markup, “html5lib”) 容错性⾼，速度慢
```


#####1.soup
```
from bs4 import BeautifulSoup

def parse_html(html):
	soup=BeautifulSoup(html,'lxml')
	#soup的节点都是bs4.element.Tag类型，可以继续进行选择
	print(soup.head.title.string)
	
	#让页面整齐输出
	print(soup.prettify())
	#打印文字内容
	print(soup.title.string)
	#打印标签
	print(soup.head)
	#打印第一个某标签
	print(soup.p)
	#打印标签名字
	print(soup.p.name)
	#取图片的src
	print(soup.img.attrs["src"])
	#取图片的src
	print(soup.img["src"])
	print(soup.img.attrs)
	
	#嵌套选择
	'<ul><li>aaa<li></ul><ul><li>bbb</li>mmm<li>ccc</li></ul>'
	#其中的mmm取不到
	
	#关联选择
	有些元素没有特征定位，可以先选择有办法定位的，然后以这个节点为		准选择它的⼦节点、⽗节点、兄弟节点等
    <p class="p1"></p>
    <p></p>
    <p></p>
    
	print(soup.p.contents) # 取p节点下⾯所有⼦节点列表
    print(soup.p.descendants) #取p节点所有⼦孙节点
    print(soup.a.parent) # 取⽗节点
    print(soup.a.parents) # 取所有祖先节点
    print(soup.a.next_sibling) # 同级下⼀节点
    print(soup.a.previous_sibling) # 同级上⼀节点
    print(soup.a.next_siblings) # 同级所有后⾯节点
    print(soup.a.previous_siblings) # 同级所有前⾯节点
    print(list(soup.a.parents)[0].attrs['class'])
	
	#方法选择器
	#根据属性和文本进行查找
	'<ul><li>aaa<li></ul><ul><li>bbb</li>mmm<li>ccc</li></ul>'
	print(soup.find_all(name="ul"))
    for ul in soup.find_all(name="ul"):
     	print(ul.find_all(name="li"))
     	for li in ul.find_all(name="li"):
     		print(li.string)
    soup.find_all(attrs={"id": "list-1"})
	
	#css选择器
	<p id="p1" class="panel"><p class=""><p><p>
	soup.select('.panel .panel_heading')
	soup.select('ul li')
	soup.select('#id1 .element')
	
```
​	