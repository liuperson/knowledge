SSH
通过SSH远程连接服务器---> ssh root@120.77.222.217，SSH(Secure Shell Protocol)安全的壳程序协议，目前而言，公司基本上采用文字接口的加密传输技术。

Unix - BSD - FreeBSD - Macintosh - macOS - iOS
Unix - Minix - Linux - Android

1991年 Linus Torvalds ---> Linux

Shell - 人机对话的交互式环境

shell是C语言编写的程序，用户使用linux的桥梁，既是命令语言，又是程序语言。

bash - bourne again shell

w / who / last - 获取登录信息

ps - processes - 查看进程快照



adduser - 创建用户

passwd - 修改密码

userdel - 删除用户

su - switch user - 切换用户

sudo - super user do - 以超级管理员身份执行



history - 查看历史命令

shutdown / init 0 - 关机

reboot / init 6 - 重启



cat - concatenate - 连接多个文件并显示到标准输出

Cat sohu.html

Head -10 sohu.html

Tail -2 sohu.html

Cat -n sohu.html|more

Less sohu.html

 

cd - change directory - 改变所在目录

pwd - print current working directory - 打印当前工作目录

ls - list directory contents - 列出文件夹内容

 

mkdir - make directory - 创建文件夹（目录）

rmdir / rm - remove directory - 删除空文件夹（空目录）

cp - copy - 拷贝文件

mv - move - 剪切文件

head / tail - 查看文件前面/后面部分

less / more - 分屏查看文件

 

echo - 回声

date - 查看系统时间日期

cal - calendar - 查看日历

 

**SSH课堂**

 通过ssh远程连接服务器---->ssh root@120.78.82.233

苹果系统是自带的，windows是自己用xshell或者是putty,就是说连接的方式有很多种。

 

登录进来，进入的是交互式的环境，将来服务器也不会有带图形化的界面，用计算机，先要有操作系统，才可以进行硬件的操作。

 

创建用户，删除用户

重启，关机。

一般是使用ps  -ef查看所有的进程，如果是要杀死则是kill<pid>,强制kill -9<pid>

history 查看历史，!命令编号

history --help 查看有哪些说明 或者man history

-d 删除

man-查看手册

操作文件和文件夹的命令

打印当前目录pwd

切换工作目录cd

 

查看文件夹下面的内容ls

参数的话，ls-l 长格式查看

drwxr  directory read  write x执行 root超级管理员

修改权限change model x-r 可执行可读不可写

mkdir bar 2次引用，ll和ls效果是一样的

 

删除 rm -rf abc

alias rmd="rm -rf" 自定义命令，这个叫做是命令的别名，这样的话可以给长命令起一个简短的名字 ，注意rmd /很危险。

如果是想取消 unalias rmd,这样就取消了别名。

 

linux系统中以. 开头的，都是文件，

-a  查看所有(包括以点开头的隐藏文件和文件夹)

-R  递归查看

windows里面命令是不区分大小写的，但是linux是要区分的。basic和sql不区分大小写。uml也是语音。

 

--help 想要查看

less 或者是more 

ls --help | more    |叫做是管道，通过管道将进程之间的数据连接起来，还有进程间通信的方式，套接字。前面的输出就是后面的输入。

 

创建文件夹midir -p 创建父文件夹

rmdir -r 递归删除

rmdir -f 强制删除

rmdir -i 交互式删除

 

echo-回声

\>输出重定项

\>>追加输出重定项

2>错误输出重定项

 

<输入重定项

|管道（进程间通信）-把前一个进程的输出当成是后一个进程的输入

后面我们学习的很多命令之间都是要用管道的，将很多联系起来。

举列子

who 和wc联系起来，2行，10单词，110字符

wc 就是统计的作用，word count-统计行、单词、字节数量。

linux里面小工具很多，比如说uniq-unique-去重

 

linux里面的命令，无副作用，就是不会改变原来的文件。

diff hello.txt hello2.txt  用来比较两个文件，文件如果相同，则无结果。

 

linux系统里面安装软件

-使用包管理工具进行安装yum/rpm  

r红帽子pcackbage method    yellow dog model 黄狗更新器

先来试一下黄狗,黄狗装的不一定是最新的版本，如果要新的需要自己来下。

-y可以一直选择yes

装python，用源代码来构建

 

压缩文件

-gz---gzip/gunzip解压 gun遵循开源协议

-xz---xz-z/xz-d解压

上面的3个工具，在里面都是有的。

WinARA，这个工具是归档和解归档。

tar-归档文件(把一个文件合并成一个文件)

解归档-把多个文件拆分成多个文件

 

Python解释器的Java实现-Jython

Python解释器的C#实现-lronPython

Python解释器的Python实现-PyPy

Python解释器的C实现-Cython

 

linux一般是自带C语音的编译器

如果没有gcc，执行命令 yum -y install gcc，自己下载就行了。

python的源代码，底层有很多的依赖库，把python需要的依赖库弄好，后面好编译

直接实现语音

yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

 

这种就叫做是源代码构建安装，编译源代码来进行安装

构建工具，构建文件是Makefile, make&&make install 短路运算，三目算法

直接敲python

既然是有软连接，那么就有硬链接

在没有复制文件数据的情况下，进行了备份，如果没有连接到它

 

 

 

 