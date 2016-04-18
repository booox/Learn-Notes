




# to-do

- [x] 运行 JupyterHub Docker ，外部访问
- [x] 本地用户登录测试成功
- [x] 批量添加用户
- [x] 添加共享文件夹
- [] 安装Python 2 Kernel
- [] 用户下载指定文件
- [] 设置 jupyterhub_config.py
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
        
## Test with local user
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
                
## 批量添加用户
    
* Ref : [Docker container with a PyData stack and JupyterHub server](https://github.com/twiecki/pydata_docker_jupyterhub)

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
            ln -s /opt/shared_nbs /home/$username

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
    
    
## 添加共享文件夹

* 创建共享文件夹
    `# mkdir /opt/shared_nbs`
* 创建到用户的链接
    `# ln -s /opt/shared_nbs /home/user_name`
    
    
## 添加对 Python2的支持
* JupyterHub的Docker 镜像提供的Notebooks只有 *python3* 
* 熟悉 [conda](http://conda.pydata.org/docs/using/index.html) 用法
* 参考 [Python 3 and 2 in IPython/Jupyter Notebook](http://stackoverflow.com/questions/29648412/anaconda-python-3-and-2-in-ipython-jupyter-notebook?rq=1)
    * 创建并激活 *python2* 虚拟环境
    ```
        # conda create -p /opt/python2 python=2.7
            -- 这里也可以用 *--name* 选项来指定名称
        # source activate python2
        # conda install jupyter
        # jupyter kernelspec install-self
        # source deactive
    ```
    * 上述命令执行完之后会自动生成 */usr/local/share/jupyter/kernels/python2/kernel.json* ，修改为：
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
         "env":{"PYTHONHOME":"/opt/python2/bin/python"}
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
    * 
    
    
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
