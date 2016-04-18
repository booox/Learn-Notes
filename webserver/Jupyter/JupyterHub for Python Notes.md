




# to-do

- [x] 运行 JupyterHub Docker ，外部访问
- [x] 本地用户登录测试成功
- [] 安装Python 2 Kernel
- [] 设置 jupyterhub_config.py
- [] 批量添加用户
- [] 用户下载指定文件


## Run JupyterHub Docker

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
                
## Bulk add user
    
* Ref : [Docker container with a PyData stack and JupyterHub server](https://github.com/twiecki/pydata_docker_jupyterhub)

* *add_user.sh* & *users*

        
    