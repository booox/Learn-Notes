# 在CentOS7上搭建 Flask + Gunicorn + Supervisor + Nginx的环境

# 准备工作

## 为了搭建上述环境，需要准备两样
    * *pip* : 方便安装Python包
    * *virtualenv* : 在相对隔离的python环境中进行测试
    
### 安装pip
 
* 下面提供两种方法用来在 *CentOS7* 上安装 *pip*

* 方法 1，
    * Step 1: 先添加 *yum* 的EPEL源:
        `$ sudo yum install epel-release`
        * Ubuntu:
            `$ sudo apt-get update`
            `$ sudo apt-get install python-pip`
        
        * 安装好之后，可以查看已安装的源
        `$ sudo yum repolist`
    * Step 2: 安装pip
        `$ sudo yum -y install python-pip`

* 方法 2:
    * 使用curl下载 *get-pip.py* 来安装
    ```
        $ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
        $ python get-pip.py
    
    ```
* Verify the Installation
    ```
        pip -V
        pip --help
        
    ```
    
### 安装virtualenv
* *pip* 装好之后就可以装 *virtualenv* 了
    `$ sudo pip install virtualenv`
    
    * 其他系统安装方式
        * Ubuntu
            `$ sudo apt-get install python-virtualenv`
        * Mac OS X
            `$ sudo easy_install virtualenv`
        * Windows
            * 同样可以先安装 *pip* 然后再安装: `pip install virtualenv`
            * 或者用 *easy_install*
                * 下载 :  https://bitbucket.org/pypa/setuptools
                * 运行:
                    ```
                    $ python ez_setup.py
                    $ easy_install virtualenv                    
                    ```
* 装好之后就可以查看 *virtualenv* 版本了:
    `$ virtualenv --version`
* Install *virtualenv*

# 完成配置

## 启动Virtualenv虚拟环境 

* 这些操作全部在python的虚拟环境中进行

    ```
        $ mkdir /home/myusername/myproject
        $ cd /home/myusername/myproject
        $ virtualenv venv
        $ source venv/bin/activate
        (venv) $     
    ```
    
## 安装flask及简单程序

* 安装flask
    `(venv) $ pip install flask`
    
* 建立flask程序
    * *myapp.py* 还在是 *myproject* 文件夹中
    ```
        (venv) $ vi myapp.py
        
        from flask import Flask
        
        app = Flask(__name__)
        
        @app.route('/')
        def index():
            return 'hello world'
            
        if __name__ == '__main__':            
            app.run(debug=True, host='0.0.0.0')        
    ```
    
    * *host='0.0.0.0'* 表示flask程序可以被外部IP所访问，而不是仅仅是内部IP （ *127.0.0.1* ）访问
    
* 运行flask程序
    `(venv) $ python myapp.py`
    `* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)`
    
    * 本地访问： *http://127.0.0.1:5000* 默认端口为 *5000*
    * 外部访问： *http://A.B.C.D:5000* 默认端口为 *5000*
    
* 退出flask程序
    `Ctrl + C`
    

## 用Gunicorn来管理Flask

* 前面使用的是flask自带的web服务器，而这在性能和并发请求的数量都无法满足生产的需求。
* 从而我们使用 [Gunicorn](http://gunicorn.org/) 来替代Flask服务器

* 安装Gunicorn
    `(venv) $ pip install gunicorn`
    
* Gunicorn用法
    ```
        (venv) $ gunicorun --help
        usage: gunicorn [OPTIONS] [APP_MODULE]   
    
    ```
    * 用 gunicorn 来启动Flask
        `(venv) $ gunicorn -w4 -b0.0.0.0:5008 myapp:app`
    
    
## 使用 Supervisor 来管理系统进程
* [Supervisor](http://supervisord.org/)
* Supervisor 是一个进程管理软件，它可以帮助我们监控类Unix系统上的多个进程。
* 也就是说：当你需要同时跑多个进程，并当这些进程挂掉之后，能自动重启进程，就可以用 *Supervisor* 来处理。

   
* 安装 Supervisor 
    `(venv) $ pip install supervisor`
    
    * 如果能输出配置文件，则安装成功
        `(venv) $ echo_supervisord_conf`
        
* supervisor 组成
    * *supervisord* : 服务端
        * 负责按预设的要求启动子程序员
        * 响应来自客户端的命令
        * 重启崩溃或退出子进程
        * 配置文件为 */etc/supervisord.conf*
        
    * *supervisorctl* : 命令行的客户端
        * 提供了类shell的界面来实现由 *supervisord* 提供的功能
        * 通过 *supervisorctl* ，用户可以连接到不同的 *supervisord* 进程
        * 得到 *supervisord* 运行的子进程列表
        * 获取子进程状态
        * 停止或启动子进程
        * 通常情况下 *supervisorctl* 使用与服务端相同的配置文件，但其它包含 *[supervisorctl]* 块的任意配置文件也可以起作用。
        
    * *Web-Server* : 一个实现 *supervisorctl* 功能的Web用户界面
  
    * */etc/supervisord.conf* : 配置文件
        * 如果修改了配置文件，可能需要 *reload* 来生效。
    
* 创建配置文件
    `(venv) $ echo_supervisord_conf > /etc/supervisord.conf`
    
* 修改配置文件
    * 在 */etc/supervisord.conf* 末尾添加以下内容
        ```
            (venv) $ vi /etc/supervisord.conf
            
            [program:myapp]
            command=/home/myusername/myproject/venv/bin/gunicorn -w4 -b0.0.0.0:8000 myapp:app 
            directory=/home/myusername/myproject
            startsecs=0 
            stopwaitsecs=0
            autostart=false
            autorestart=false 
            stdout_logfile=/home/myusername/myproject/log/gunicorn.log    
            stderr_logfile=/home/myusername/myproject/log/gunicorn.err
        ```
        
* 启动Supervisor (Gunicorn-Flask)
    `(venv) $ supervisorctl -c /etc/supervisord.conf start myapp`
    or
    `(venv) $ supervisorctl -c /etc/supervisord.conf start all` 
    
    * 用这个方法未能成功：
        `(venv) $ supervisord -c /etc/supervisord.conf`
            
    * 其它 *supervisorctl* 命令
        `(venv) $ supervisorctl -c /etc/supervisord.conf status` 
        `(venv) $ supervisorctl -c /etc/supervisord.conf reload` 
        `(venv) $ supervisorctl -c /etc/supervisord.conf stop [all] | [app_name]` 

* 浏览器访问检测
    `http://127.0.0.1:8000` 端口为 *supervisord.conf* 中所设。
    
* 先停止 *supervisor*
    `(venv) $ supervisorctl -c /etc/supervisord.conf stop [all] | [app_name]` 
    
    
## 安装配置 Nginx

* 在CentOS7上安装 nginx ，这个是直接安装到系统中的，不用在虚拟环境中
    * 先安装 *epel-release* 源
        `$ sudo yum -y install epel-release`
    * 安装 *nginx*
        `$ sudo yum -y install nginx`
    
* 再次修改 *supervisord.conf* 文件，让 Supervisor 来管理 Nginx
    * */etc/supervisord.conf* 在末尾添加
        ```
            [program:nginx]
            command=/usr/sbin/nginx 
            startsecs=0 
            stopwaitsecs=0
            autostart=false
            autorestart=false 
            stdout_logfile=/home/myusername/myproject/log/nginx.log    
            stderr_logfile=/home/myusername/myproject/log/nginx.err        
        ```
        
* 配置完成后，用 *root* 启动 *supervisor*
    
    
    