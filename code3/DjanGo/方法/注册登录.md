[TOC]

#### 1.三种注册登录


```
思路:
	1.django自带auth模块，实现注册登录注销
	登录：auth.login()
		request.user赋值，赋值为登录系统的用户，在页面中直接解析{{user}},{{user.username}}
	退出：auth.logout()
		request.user匿名用户anymouseUser
	验证：login_required()
	
	2.自己实现,令牌token
	登录：
		1.设置cookie，cookie中保存令牌token
		2.删除服务器中token和用户的关联关系(存在mangodb中是比较好的)
	登录校验：
		登录cookie中的token 值，是否能从服务端对应的用户信息
		1.装饰器
		2.中间件 process_request process_response
	3.cookie+seesion（会话上下文，会话保持）
		cookie:肯定是存在客户端的
		session:存放在服务端
	登录：
		request.session[key]=value
	退出:
		删除session中的kye
	校验：
		获取session中的key值，如果获取得到,表示登录，如果获取不到，表示没登录
		
```

#### 3.cookie+session（会话保持，会话上下文）

1.建立模型，模型建立后迁移进数据库

```
#1.建立模型需要model,当然也是可以使用系统自带的User,这里是自建。
#2.姓名 密码 出生年月 性别 电话 邮箱 一共六组数据，姓名和密码必填

from django.db import models 

class User(models.Model)：
	"""用户表"""
	username=models.CharField(max_length=4,unique=True,verbose_name="姓名")
	password = models.CharField(max_length=10, verbose_name="密码")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    GENDER = (
        	("male", "男"),
        	("female", "女")
        	)
    gender = models.CharField(max_length=6, choices=GENDER, default="female",verbose_name="性	别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        db_table = 'f_user'
```

2. forms表单，验证的是数据的完整性


```
#先是引入forms和系统的User
#验证的作用是很必要的
from django import forms
from user.models import User

class UserFormRegister(forms.Form):
	username=forms.CharField(max_length=4,required=True,
							error_message={
                              'required':'姓名必填'
							})
	password=forms.CharField(required=True,min_length=5,
                        error_messages={
                           'required': '密码必填'                
                        })
    password2=forms.CharField(required=True,min_length=5,
                        error_messages={
                           'required': '密码必填'
                        })
    email=forms.CharField(required=True,min_length=5,
                        error_messages={
                           'required': '邮箱必填'
                        })
       
     #clean
     def clean(self):
     	#先获取用户，是否存在
        user=User.objects.filter(username=self.clean_data.get('username'))
        if user:
        	raise forms.ValidationError({'username':'此账号已经注册'})
        if self.clean_data['password'] != self.clean_data['password2']
        	raise forms.ValidationError({'password':'密码前后不一致'})
        return self.clean_data
    
```

3.views 将数据保存至数据库，跳转至登录

```
#有模型，也验证数据的完整性后，接下来就是提交数据，将数据保存在数据库中，然后跳转到登录页面
from user.forms import UserFormRegister
from user.models import User

def register(request):
	if request.method == 'GET':
		return render(request,'register.html')
	if request.method == 'POST':
		# 获取提交的数据，数据里面有模型定义的六种
		data=request.POST
		# 将数据交给表单来验证
		form=UserFormRegister(data)
		# 系统自带的检测方法
		if form.is_valid():
			# 可以开始保存数据
			User.objects.create(username=self.clean_data.get('username'),
								password=make_password(self.clean_data.get('password'))
								)
			return HttpResponseRedirect(reverse('user:login'))
		else:
			return render(request,'register.html',{'error':form.error})
		
def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	if request.method == 'POST':
		username=request.POSt.get('username')
		password=request.POST.get('password')
		if not all([username,password]):
			msg='请填写完整'
			return render(request,'login.html',{'msg':msg})
		user=User.objects.filter(username=username).first()
		if not check_password(password,user.password):
			msg='密码不一致'
			return render(request,'login.html',{'msg':msg})
		
		#到这里，通过提交的姓名和密码和模型里的用户名和密码来进行比对，说明是可以登录的。
		#既然是可以登录，接下来将用户的id放在session中
		request.session['user_id']=user.id				
		retuen HttpResponseRedirect(reverse('goods:index'))		
			
```

4.request.session中存有数据，写中间件，验证

```
#1.先在setting.py里面设置utils.middleware.UserAuthMiddleware
#2.在utils里面新建middleware
from django.utils.deprecation import MiddlewareMixin

class UserAuthMiddleware(MiddlewareMixin):
	def process_request(self,request):
		
		# 既然在登录的views里面已经存有user_id
		user_id=request.session.get('user_id')
		# 如果登录
		if user_id:
			# 将拿到的user_id和数据库中众多user进行比对
			user=User.objects.filter(pk=user_id).first()
			
			# 所以对象就不只是user_id
			request.user=user
			return None
		# 返回登录界面，不过这样的做法，只要拿不到session就无法登录，也就		是说用户如果不登录，无法访问其他界面
		return render(request,'login.html') 
		
```







































