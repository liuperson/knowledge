1.外层函数嵌入内层函数

2.外层函数返回内层函数

3.内层函数调外层函数的参数



```
from flask import session,redirect,url_for

def is_login(func):

    def check():

        try:
            user_id=session['user_id']
        except Exception as e:
            return redirect('/app/login')
            
        return func()

    return check
    
    #如果session中设置有user_id，其实就是是否第一次登陆
```