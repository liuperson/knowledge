[TOC]
#### auth+login_require+middleware

```
django封装好的注册登录注销函数
login_required装饰器
中间件
```

##### 1.url

```
from django.conf.urls import url
from user import views

urlpatterns=[
    # 注册，使用django自带的User模型
    url(r'register/',views.register,name='register'),
    # 登录
    url(r'^login/',views.login,name='login'),
    # 主页
    url(r'^index/',views.index,name='index'),
    # 注销
    url(r'^logout',views.logout,name='logout'),
]
```

##### 2.templates

```
#注册模块
{% block content %}
    {{ errors }}
    <form action=""method="post">
        姓名：<input type="text"name="username">
        密码: <input type="text"name="password">
        确认密码：<input type="text"name="password2">
        <input type="submit"value="提交">
    </form>
    {% if errors.username %}
        姓名错误：{{ errors.username }}
    {% endif %}
{% endblock %}

#登录模块
{% block content %}
    {{ errors }}
    <form action=""method="post">
        姓名：<input type="text"name="username">
        密码: <input type="text"name="password">
        <input type="submit"value="提交">
    </form>
{% endblock %}

#首页
{% extends 'base.html' %}
{% block content %}
   welcome to shouye
    <a href="{% url 'user:logout' %}">注销</a>
{% endblock %}
```

##### 3.注册登录注销

```
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from user.forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method =='GET':
        return  render(request,'register.html')
    if request.method =='POST':
        data=request.POST
        form =UserRegisterForm(data)

        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return render(request,'register.html',{'errors':form.errors})

def login(request):
    if request.method == 'GET':
        return  render(request,'login.html')
    if request.method == 'POST':
        data=request.POST
        form =UserLoginForm(data)
        if form.is_valid():
            # 使用随机标识符
            # 现在使用django自带的auth
            user=auth.authenticate(username=form.cleaned_data.get('username'),
                              password=form.cleaned_data.get('password'))
            if user:
                # 验证成功，进行登录
                # 向request.user属性赋值，赋值为登录系统的用户对象
                # 1.向页面的cookie中设置session值
                # 2.向django_session表中设置值
                # 在这里自动设置了标识符,session_key 和session_value 存了这两个值,自动检验
                auth.login(request,user)
                return HttpResponseRedirect(reverse('user:index'))
            else:
                return render(request,'login.html',{'msg':'密码错误'})
        else:
            return render(request,'login.html',{'errors':form.errors})

@login_required
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    if request.method == 'POST':
        pass
        
@login_required
def logout(request):
    if request.method== 'GET':
        return HttpResponseRedirect(reverse('user:login'))
```

#####4.forms

```
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username=forms.CharField(max_length=10,min_length=2,required=True,
                         error_messages={
                             'required': '姓名必填',
                             'min_length': '最短2字符',
                             'max_length': '最长10字符'
                         })
    password = forms.CharField(max_length=30, required=True,
                         error_messages={
                             'required': '注册密码必填',
                             'max_length':'不超过10字符',
                         })
    password2 = forms.CharField(max_length=30, required=True,
                          error_messages={
                              'required': '确认密码必填',
                              'max_length': '不超过10字符',
                          })

    def clean(self):
        user=User.objects.filter(username=self.cleaned_data.get('username')).first()
        if user:
            raise forms.ValidationError({'username':'账号已经注册，请去登录'})
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError({'password':'密码不一致'})
        return self.cleaned_data

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '姓名必填',
                                   'min_length': '最短2字符',
                                   'max_length': '最长10字符'
                               })
    password = forms.CharField(max_length=30, required=True,
                               error_messages={
                                   'required': '注册密码必填',
                                   'max_length': '不超过10字符',
                               })
    def clean(self):
        user=User.objects.filter(username=self.cleaned_data.get('username'))
        if not user:
            raise forms.ValidationError({'username':'该账号没有注册，请去注册'})
        return self.cleaned_data
```



##### 5.middleware

```
定义：
	1.轻量级，底层插件，可以插入django的请求和响应（面向切面对象）
	2.中间件的本质就是python类
	注意：中间件是帮助我们在视图函数执行之前和执行之后做一些额外操作，它本质上就是一个自定义类，类中定义了几个方法，Django框架会在请求的特定的时间去执行这些方法。

思考：
    1.什么是中间件？
    2.在settings.py中有很多的中间件，主要是用来做什么功能的呢？
    3.他们处理请求的url的过程在那些阶段呢？
    4.一般用来做那些数据的处理呢？
```




```
from django.utils.deprecation import MiddlewareMixin

# 周五代码中间件改为装饰器
class TestMiddleware(MiddlewareMixin):

    def process_request(self,request):

        print('process_request1')
        # 继续执行视图函数
        return None
        #装饰器里面的代码写在这里，面向切面编程


    def process_response(self,request,response):
        print('process_response1')
        # 返回响应
        return response


class TestMiddleware2(MiddlewareMixin):

    def process_request(self, request):
        print('process_request2')
        # 继续执行视图函数
        return None
        # 装饰器里面的代码写在这里，面向切面编程

    def process_response(self, request, response):
        print('process_response2')
        # 返回响应
        return response
    运行结果：
    process_request1
    process_request2
    process_response2
    process_response1
```


```
在项目中，setting.py中可以查到已经定义好的中间件，并加入我们自定义的
MIDDLEWARE = [
    'utils.middleware.TestMiddlware1',  # 加载中间件TestMiddlware1
    'utils.middleware.TestMiddlware2',  # 加载中间件TestMiddlware2
]
```



```
1. process_request(self, request)
	执行时机在django接收到request之后, 但仍未解析出url以确定运行哪个视图函数view之前

2. process_view(self, request, view_func, view_args, view_kwargs)
	执行时机在django执行完request预处理函数并确定待执行的view之后, 但在视图函数view之前
	request: HttpRequest对象
	view_fun: 是django将要调用的视图函数, 是真实的函数对象本身
	view_args: 将传入view的位置参数列表, 不包括request参数
	view_kwargs: 将传入view的字典参数

3. process_response(self, request, response)
	该方法必须返回HttpResponse对象, 可以是原来的, 也可以是修改后的

	调用时机在django执行完view函数并生成response之后, 该中间件能修改response的内容, 常见用途比如压缩内容
	request是request对象
	response是从view中返回的response对象

4. process_exception(self, request, exception)
	默认不主动调用，该方法只有在request处理过程中出了问题并且view函数抛出了一个未捕获的异常才会被调用, 可以用来发送错误通知, 将相关信息输出到日志文件, 或者甚至尝试从错误中自动恢复
	参数包括request对象, 还有view函数抛出的异常对象exception
	必须返回None或HttpResponse对象

5. process_template_response(self, request, response)
	默认不主动调用，在视图执行render()返回后进行调用，必须返回None或HttpResponse对象
	
以上方法的返回值可以是None或者一个HttpResponse对象，如果是None,则机选按照django定义的规则向后继续执行，如果是HttpResponse对象，则直接将该对象返回给用户。
```

