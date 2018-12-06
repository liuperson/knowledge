[TOC]



##### 1.urilllb

```
urllib是基于http的⾼层库，它有以下三个主要功能：
1. request处理客户端的请求
2. response处理服务端的响应
3. parse会解析url
4. 主要⽤来识别⽹站的robots.txt⽂件，⽤得较少
```

##### 2.response属性

```
import urllib.request
response=urllib.request.urlopen('http://www.baidu.com')

print(response.status)
print(response.getheaders())
print(response.getheaders("Server"))

html=response.read().decode('utf-8')
```
##### 3.设置超时

```
import urllib.request
response = urllib.request.urlopen("http://2018.sina.com.cn/", timeout=1) 
```

##### 4.请求头参数

```
from urllib import request, parse
url = "http://2018.sina.com.cn/"
headers = {
 "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
 "Host": "2018.sina.com.cn",
}
dict = {
 "name": "Question"
}
data = bytes(parse.urlencode(dict), encoding="utf8")
req = request.Request(url=url, data=data, headers=headers, method="GET")
response = request.urlopen(req)
print(response.read().decode("utf-8"))
```

##### 5.异常

```
from urllib import request, error
try:
 response = request.urlopen("https://cuiqingcai.com/index.htm")
except error.URLError as e:
 print(e.reason)
```

用的很少