**基础条件：**

```
window10 专业版 64位
Git+nodejs+github
```

**相关步骤：**

```
1.安装node.js+GIt
2.Github账户注册
	Owner:liuperson
	Repository:liuperson.github.io
	
	public
	inintialize this repository with a readme
3.E盘新建文件夹blog
	E:\blog\ 
		npm install hexo -g #开始安装
		hexo -v #检查是否安装成功
		hexo init #初始化
		npm install #安装插件
		hexo g #首次体验
		hexo s #开启服务
			#如果没有见本地localhost
		hexo server -p 5000
	4. 右键 git Bash Here
	/E/blog
		$git config --global user.name "liuperson"
        $git config --global user.email "123@qq.com"
    cd ~/.ssh
    $ls
    $ssh-keygen -t rsa -C "123@qq.com"
    $eval "$(ssh-agent -s)" #添加密钥到ssh-agent
    $ssh-add ~/.ssh/id_rsa #添加生成的ssh key 到ssh-agent
    
    5.登录github,点击setting ，添加ssh
    	新建new ssh key ,将id_rsa.pub内容复制上去
    6.输入ssh -T git@github.com #测试是否成功
    	如果失败：
    		ssh-add -D #清除所有的key-pair
    		rm -r ~/.ssh #删除你在github中的publish-key
    		
    		重新生成密钥
    		ssh-keygen -t rsa -C "123@qq.com"
    		重新粘贴复制
    7.配置Deployment,找到_config.yum
    deploy:
    	type: git
    	repository: git@github.com:liuperson/liuperson.github.io.git		branch:master				
    		
    8.新建博客,在cmd执行 
    hexo new post "like"
    	npm install hexo-deployer-git --save
    hexo d -g
    9.http:liuperson.github.io进行访问
		
```

