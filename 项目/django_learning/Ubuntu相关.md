# ubuntu环境配置

## 网络配置
桥接无线网卡，**ip=192.168.0.50**

##远程登录
`$sudo apt-get install openssh-server #安装SSH服务`
`$sudo /etc/init.d/ssh start                   #开启服务`

参考自[百度经验](http://jingyan.baidu.com/article/11c17a2c382a15f446e39d24.html?st=2&net_type=&bd_page_type=1&os=0&rst=&word=) 

##安装pip


###为多版本python安装pip
####为默认版本安装pip
`$sudo apt-get install python-pip`
####为另一版本安装pip
从官网下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)

官网链接：<https://pip.pypa.io/en/latest/>

`$python3.5 get-pip.py`
####创建pip3.5
参考/usr/bin/pip

  	1 #!/usr/bin/python                                                           
  	2 # GENERATED BY DEBIAN
  	3 
 	4 import sys
 	5 
	6 # Run the main entry point, similarly to how setuptools does it, but because
  	7 # we didn't install the actual entry point from setup.py, don't use the
  	8 # pkg_resources API.
  	9 from pip import main
 	10 if __name__ == '__main__':
 	11     sys.exit(main())
	~    
将第一行`python`换成`python3.5`
另存为/usr/bin/pip3.5即可
需要时即使用`$pip3.5 install`

参考自<http://blog.csdn.net/junbujianwpl/article/details/51598506>

##安装及远程访问mysql
参考自<http://www.cnblogs.com/iscodercn/p/5488633.html>
<http://www.linuxidc.com/Linux/2014-09/106811.htm>

桌面使用Navicat Premium 登录查看mysql

`$/etc/init.d/mysql start` # 启动mysql 

##武装vim
###python IDE
<http://blog.csdn.net/zoe116/article/details/51163420>
<http://blog.csdn.net/nickyzhi/article/details/38429785>

**用法待续**
###仅补全
[Pydiction](http://www.vim.org/scripts/script.php?script_id=850)

按下`TAB`进行补全

###删除行首空格
尚不确认是否由于所使用终端引起

`%s/^\s*//`

参考自<http://tanqisen.github.io/blog/2013/01/13/vim-search-replace-regex/>

