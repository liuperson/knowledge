**hexo**

```
#安装 npm install hexo -g 
#升级 npm update hexo -g
#初始化 npm init
```

**新建文章**

```
#新建 hexo n "文章名字" =hexo new "文章名字"
#发布 hexo p =hexo publish
#生成 hexo g =hexo generate
#启动服务预览 hexo s =hexo server
#部署 hexo d =hexo deploy
```

**监视文章变动**

```
#使用hexo生成静态文件 hexo generate
#监视文件变动 hexo generate --watch
```

**部署**

```
hexo generate --deploy
hexo deploy --generate
```

**服务器**

```
#监视文件变动和自动更新 hexo server
#静态模式 hexo server -s
#更改端口 hexo server -p 5000
#自定义ip地址 hexo server -i 192.168.1.1
#清除缓存 hexo clean
#生成静态网页 hexo g
#开始部署 hexo d
```

**草稿**

```
hexo publish [layout] <title>
```

**推送**

```
#写 hexo n
#生成 hexo g
#部署合并 hexo d -g
```

**报错分析**

```
ERROR Deployer not found:git
解决：
	npm install hexo-deployer-git --save
	
RSS不显示
解决：
	安装插件npm install hexo-generate-feed --save
开启RSS
	hexo/_config.yml
	添加代码 rss:atom.xml 
开启评论
```