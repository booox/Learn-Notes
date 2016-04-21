




# to-do

- [x] 运行 JupyterHub Docker ，外部访问
- [x] 本地用户登录测试成功
- [x] 批量添加用户
- [x] 添加共享文件夹
- [x] 安装Python 2 Kernel
- [x] 设置 jupyterhub_config.py
- [] 用nginx做反向代理
- [] JupyterHub 多线程支持？
- [] 中文界面
- [] 用户下载指定文件
- [] 上传文件
- [] 使用仅用于存储的容器
- [] 自动备份数据
- [] 使用GitHub账户登录（认证）


## Run JupyterHub Docker

### 下载 JupyterHub Docker

* [jupyter/jupyterhub](https://hub.docker.com/r/jupyter/jupyterhub/)

* 先不要后台运行，这样可以直接看到服务端详细的信息提示，对排错来说是非常方便的。
    * 非后台运行， *--no-ssl* 
    `$ docker run -p 8000:8000 --name jupyterhub jupyter/jupyterhub jupyterhub --no-ssl`
    * The last *jupyterhub* is the COMMAND
    * Now we can test it with websurf : `http://127.0.0.0:8000`
        * 这里可以看到一个登录界面
        
## Add local user
    * Spawn a root shell with `docker exec`
    ```
        $ docker exec -it jupyterhub bash
        root@dfj3434:/srv/jupyterhub#
    ```
    
    * Create system users in the container
    ```
        root@dfj3434:/srv/jupyterhub# useradd usr1
        root@dfj3434:/srv/jupyterhub# passwd usr1
    ```
        * 尝试用刚添加的用户登录时，提示如下错误：
        ```
            500 : Internal Server Error
            Spawner failed to start [status=1]
        ```
        * 仔细查看了服务端信息，发现提示如下错误
        ```
            File "/opt/conda/bin/jupyter/jupyterhub-singleuser", line 21, in <module>
                import notebook
            ImportError: No module named: 'notebook'
        
        ```
            * 应该是*JupyterHub* 的Docker镜像中没有安装 *Jupyter* 导致的，安装后错误提示不再出现。            
                `# pip install jupyter`
                
## login with PAM authentication
    * 出现新的错误：`PAM Authentication failed [PAM Error 3] Error in service module`
        * Fix:
            ```
                # vi /etc/pam.d/login
                #session required pam_loginuid.so #将此行注释掉
            ```
        *[PAM authentication errors](https://github.com/jupyter/jupyterhub/issues/323)
    * 后来才发现，用 *useradd* 创建用户时，默认是不会创建用户目录的
        * 要加上 *-m* 参数：`# useradd -m usr1` 
        
    * Done!
                
    
    
## 添加对 Python2的支持
* JupyterHub的Docker 镜像提供的Notebooks只有 *python3* 
* 熟悉 [conda](http://conda.pydata.org/docs/using/index.html) 用法
* 参考 [Python 3 and 2 in IPython/Jupyter Notebook](http://stackoverflow.com/questions/29648412/anaconda-python-3-and-2-in-ipython-jupyter-notebook?rq=1)
    * 安装了其他软件
    ```
        # apt-get update && apt-get install -y vim
        # alias vi=vim
    ```
    
    * 创建并激活 *python2* 虚拟环境
    ```
        # conda create -p /opt/python2 python=2.7
            -- 这里也可以用 *--name* 选项来指定名称
            如：# conda create -y --name python2 python=2.7
            默认会将环境生成在：/opt/conda/envs/python2
        # source activate /opt/python2
        # conda install -y jupyter
        # jupyter kernelspec install-self   # 这个有问题，用这个：ipython kernelspec install-self
        # source deactivate
    ```
    * 上述命令执行完之后会自动生成 */usr/local/share/jupyter/kernels/python2/kernel.json* ：
    ```
        {
         "display_name": "Python 2",
         "language": "python",
         "argv": [
          "/opt/python2/bin/python",
          "-m",
          "ipykernel",
          "-f",
          "{connection_file}"
         ],
        }
    ```
    * 这里就可以在 *New* 中看到 *Python-2* 了，但有个问题，
        * 当单击 *Python-2* 会新建一个 Notebook ，可是 *Web* 页面上马上提示 *Dead-kernel* ，并访问是否 *restart*
        * 而终端上提示：
            ```
                ImportError: No module named site
                KernelRestarter: restarting kernel
                restarted failed!
                Kernel deleted before session
            
            ```
        
    * 纠结了许久，终于尝试了一下
        ```
            # cd /opt
            # source activate python2
            # ipython kernelspec install-self
            # source deactivate
        ```
        * 这次可以了，分析原因可能是版本的不同导致的。
        
        
        
## 批量添加用户
    
* Ref : [Docker container with a PyData stack and JupyterHub server](https://github.com/twiecki/pydata_docker_jupyterhub)
* 添加共享文件夹

    * 创建共享文件夹
        `# mkdir /opt/shared_notebooks`
        * 创建到用户的链接，这个是在 *add_user.sh* 里自动实现
            `# ln -s /opt/shared_nbs /home/user_name`
    
* *add_user.sh* & *users*
    * *add_user.sh*
    ```bash
#!/bin/bash

if [ $# -lt 1 ]
  then
    echo "Usage : $0 userfile"
    exit
fi

if [ $(id -u) -eq 0 ]; then

while IFS=, read username password; do

    if egrep "^$username" /etc/passwd >/dev/null;  then
        echo "$username exists!"
    else
        password=$(perl -e 'print crypt($ARGV[0], "password")' $password)

        if  useradd -m -p "$password" "$username" >/dev/null; then
                echo "User '$username' has been added to system!"
        else
                echo "Failed to add  user '$username'!"
        fi
    fi
    ln -s /opt/shared_notebooks /home/$username

done <"$@"

else
      echo "Only root may add a user to the system"
      exit
fi
    
    ```
    * *users*
    ```
        usr1,ps1
        usr2,ps2
    ```
    * Run : `# bash /tmp/add_user.sh /tmp/users`

    * *del_user.sh*
```
#!/bin/bash

if [ $# -lt 1 ]
  then
    echo "Usage : $0 userfile"
    exitvi 
fi

if [ $(id -u) -eq 0 ]; then

while IFS=, read username password; do

    if egrep "^$username" /etc/passwd >/dev/null;  then
        
        password=$(perl -e 'print crypt($ARGV[0], "password")' $password)

        if  userdel -r "$username" >/dev/null; then
                echo "User '$username' has been deleted to system!"
        else
                echo "Failed to delete  user '$username'!"
        fi       
        
    else
        echo "$username doesn't exists!"
    fi

done <"$@"

else
      echo "Only root may delete a user to the system"
      exit
fi


```
    
    
## Ref    
### 添加数据容器

- [data persistence and permissions issue](https://github.com/twiecki/pydata_docker_jupyterhub/issues/2)

#### mount a folder from host:
`sudo docker run -d -p 8000:8000 -v /path/to/local/folder:/opt/shared_nb myhub`

#### use a data-only container
*  (seems to be the appropriate docker way, it allows backup facility etc.) 
`sudo docker run --name mydata mydata`
`sudo docker run -d -p 8000:8000 --volumes-from mydata myhub`

* using a simple Dockerfile for mydata, the so-called data-only container:
```

    FROM ubuntu
    RUN addgroup jupyter

    RUN mkdir /opt/shared_nbs
    RUN chgrp -R jupyter /opt/shared_nbs
    RUN chmod a+rwx /opt/shared_nbs
    RUN chmod g+s /opt/shared_nbs

    VOLUME /opt/shared_nbs
```

## 用nginx做反向代理

* [jupyterhub nginx reverse proxy](http://stackoverflow.com/questions/35419414/jupyterhub-nginx-reverse-proxy)
* [ (HTTP 403: Forbidden)](https://gitter.im/jupyter/jupyterhub/archives/2015/11/03)
* [jupyterhub-deploy-data301](https://github.com/booox/jupyterhub-deploy-data301)

* 学习一下 nginx 的配置代码用法


* 

    * `docker run -p 8000:8000 --name jhub1 jupyter/jupyterhub jupyterhub -f /srv/jupyterhub/jupyterhub_config.py --no-ssl`
    
    
## 设置 jupyterhub_config.py

* 生成 *jupyterhub_config.py* 
    ```
        # cd /srv/jupyterhub
        # jupyterhub --generate-config
        writing default config to: jupyterhub_config.py
    ```
    
    * 也可以通过 *-f* 来加载特定的配置文件夹
        `jupyterhub -f /path/to/jupyterhub_config.py`
        
    * 测试是否有效
    ```
        # vi  jupyterhub_config.py
        c.Authenticator.whitelist = {'mal', 'zoe', 'inara', 'kaylee'}
    ```
        * 如果只有括号里的可以访问，则说明配置文件在起作用。

        
## use check()

* [Start notebook by linking to myapp](http://nbviewer.jupyter.org/github/frankr6591/AppNotebooks/blob/master/nbExample1.ipynb)
* [import fails on jupyter-notebook](http://stackoverflow.com/questions/35850136/import-fails-on-jupyter-notebook)
* [Import python package from local directory into interpreter](http://stackoverflow.com/questions/1112618/import-python-package-from-local-directory-into-interpreter)

### nb extensions
* [Loading notebook extensions for all users on the hub](https://github.com/jupyterhub/jupyterhub/issues/305)





# 先运行Docker，带上log文件，然后进入bash后再运行jupyterhub

## 运行Docker

* 运行Docker bash:    `$ docker run -d -p 8000:8000 --name jhub jupyter/jupyterhub jupyterhub --no-ssl --log-file /var/log/jupyterhub.log`

* 进入Docker container: `$ docker exec -it juhb bash`

* 可查看 *jupyterhub.log*
    `# tail -f /var/log/jupyterhub.log`

* 生成 *jupyterhub* 配置文件夹：
    `# jupyterhub --generate-config`
    
* 安装必要软件 更新 *apt-get* 及安装
    `# pip install jupyter`
    `# apt-get update`
    `# apt-get -y install vim`
    
* 修改 *jupyterhub_config.py*
    * ref: [jupyterhub configuration](https://jupyterhub.readthedocs.org/en/latest/getting-started.html#configuring-authentication)
    ```
        # jupyterhub_config.py
        c = get_config()

        # put the log file in /var/log
        c.JupyterHub.log_file = '/var/log/jupyterhub.log'

        # specify users and admin
        c.Authenticator.whitelist = {'rgbkrk', 'minrk', 'jhamrick'}
        c.Authenticator.admin_users = {'jhamrick', 'rgbkrk'}

        # start single-user notebook servers in ~/assignments,
        # with ~/assignments/Welcome.ipynb as the default landing page
        # this config could also be put in
        # /etc/ipython/ipython_notebook_config.py
        c.Spawner.notebook_dir = '~/assignments'
        c.Spawner.args = ['--NotebookApp.default_url=/notebooks/Welcome.ipynb']
    
    ```
* 在container中添加共享文件夹
    ```
        # mkdir /opt/shared_notebooks
        # mkdir /opt/shared_notebooks/examples
        # mkdir /opt/shared_notebooks/dashboard
        # chmod a+rwx /opt/shared_notebooks
        # chmod a+rwx /opt/shared_notebooks/examples
        # chmod a+rwx /opt/shared_notebooks/dashboard
    ```
    
* 批量添加用户
    见上面
    
* 添加python2的支持
    * 照上面装，装好就出问题了
    
    
    
    
    
    
    
    
# Problem

* 运行Docker
    `docker run -d -p 8000:8000 --name jhub jupyter/jupyterhub jupyterhub --no-ssl --log-file /var/log/jupyterhub.log`
    


* `tail -f /var/log/jupyterhub.log`
    `JupyterHub log:100] 200 GET /hub/api/authorizations/cookie/jupyter-hub-token-lunn/[secret] (lunn@127.0.0.1)`
    
* `tail -f /var/log/nginx/error.log`
    `[warn] 3495#0: *897 an upstream response is buffered to a temporary file`
    
* 访问 8000端口正常，访问 8848 页面可以显示首页等，但不能创建notebook，提示 Not Found