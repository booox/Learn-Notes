
JupyterHub Deploy



# Links

* a multi-user Jupyter Notebook environment, on a single host using Docker: [jupyterhub-deploy-docker](https://github.com/jupyterhub/jupyterhub-deploy-docker)
* deploy JupyterHub on AWS using Ubuntu Trusty: [Deploying JupyterHub on AWS](https://github.com/jupyterhub/jupyterhub/wiki/Deploying-JupyterHub-on-AWS)
* JupyterHub for teaching with nbgrader: [JupyterHub for Teaching](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/)
    * [jupyterhub-deploy-teaching](https://github.com/booox/jupyterhub-deploy-teaching)
* JupyterHub is running on the host, and users are in containers: [jupyterhub-demo](https://github.com/minrk/jupyterhub-demo)
* []()


# Create a Docker Machine

* Use Docker Machine to provision a new host, or to connect to an existing host. 

## Provision a new host



## Connect to an existing host

* ref: [adding an existing docker host to docker machine : a few tips](https://blog.dahanne.net/2015/10/07/adding-an-existing-docker-host-to-docker-machine-a-few-tips/)

1. 确保可以从安装 *Docker-machine* 的计算机（Windows或Mac）上通过 public key 连接到远程的Docker主机
    * 在Windows客户机上利用 *SecureCRT* 制作密钥对
        * 创建新会话，填好“主机名”、“端口”、“用户名”，选择“PublicKey”，单击“属性”
        * “创建身份文件”
        * 选择密钥类型 “RSA”
        * 设置通知短语和注释（均为可选）
        * 输入密钥长度：1024
        * 生成密钥
        * 选择“OpenSSH密钥格式”，“完成”
            * 私钥---Identity		公钥----Identity.pub
    * 在远程Docker主机上开启 SSH 服务
        * 配置SSH
            * `$ sudo vi /etc/ssh/sshd_config`
        * 启动ssh服务( *CentOS7* )
            * `$ sudo systemctl start sshd`
            * `$ sudo systemctl status sshd`
        * 创建用于ssh连接的用户
            * `$ sudo useradd -m sshuser1`
            * `$ sudo passwd sshuser1`
            * `$ su - sshuser1`
            * `$ mkdir ~/.ssh`
            * `$ chmod 700 ~/.ssh`
            * `$ cd ~/.ssh`
    * 将公钥 *Identity.pub* 上传至sshuser1的 *.ssh* 目录中，并修改权限
        `$ wget ftp://***/Identity.pub ~/.ssh`
        `$ cat Identity.pub >> authorized_keys`
        `$ chmod 400 authorized_keys`
        
2. 如果想在远程主机上使用 *sudo* ，确保如下设置
    * */etc/sudoers*
    ```
        $ sudo visudo
        YOURUSERNAME ALL=(ALL) NOPASSWD:ALL  # Add this line    
    ```
    * ref: [unless this issue is closed](https://github.com/docker/machine/issues/1569)
    
3. 确保远程主机上 *Docker* 的版本与安装 *Docker-machine* 上 *Docker* 的版本相同
    `$ docker -v`
    
4. 在远程主机上打开 *2376* 端口
    * check SELinux allowed to bind to the whic ports
    ```
        $ sudo semange port -l | grep 2376    
    ```
    * Add port you want to bind out to the list
        `$ sudo semanage port -a -t ssh_port_t -p tcp 2376`
        
        OR:    
        * Debian/Ubuntu
            `ufw allow 2376`
        *
        
5. 在 *Docker-machine* 主机上添加远程 *Docker* 主机
    ```
        $ docker-machine create -d generic \
        > --generic-ssh-user lunn \
        > --generic-ssh-key /c /Users/user_name/sec/Identity    # user_name替换为Windows 系统上的用户名
        > --generic-ip-address 192.168.92.61 centos7
        Running pre-create checks...
        Creating machine...
        (centos7) Importing SSH key...
        Waiting for machine to be running, this may take a few minutes...
        Detecting operating system of created instance...
        Waiting for SSH to be available...
        Detecting the provisioner...
        Provisioning with centos...
        Copying certs to the local machine directory...
        Copying certs to the remote machine...
        Setting Docker configuration on the remote daemon...
        Checking connection to Docker...
        Docker is up and running!
        To see how to connect your Docker Client to the Docker Engine running on this vi
        rtual machine, run: D:\Program Files (x86)\Docker Toolbox\docker-machine.exe env
         centos7    
    ```
    * 测试：
    ```
        $ docker-machine ls
        NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
        centos7   -        generic      Running   tcp://192.168.92.61:2376            v1.11.0
        default   *        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.0
        dev       -        virtualbox   Running   tcp://192.168.99.101:2376           v1.11.0    
    ```
    * 连接到新建的 *centos7* 主机.
        `$ eval "$(docker-machine env centos7)"`
        
    * 再 *ls* 一下
    ```
        $ docker-machine ls
        NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
        centos7   *        generic      Running   tcp://192.168.92.61:2376            v1.11.0
        default   -        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.0
        dev       -        virtualbox   Running   tcp://192.168.99.101:2376           v1.11.0    
    ```

# Activate Docker Machine

* 下面所有的 *docker* 命令都运行在叫做 *jupyterhub* 的远程主机上，因此 *jupyterhub* 要被激活

* 激活 *jupyterhub*
    `$ eval "$(docker-machin env jupyterhub)"`
    
* 查看环境变量
    ```
        
    
        $ env|grep DOCKER

        DOCKER_HOST=tcp://10.0.0.10:2376
        DOCKER_MACHINE_NAME=jupyterhub
        DOCKER_TLS_VERIFY=1
        DOCKER_CERT_PATH=/Users/jtyberg/.docker/machine/machines/jupyterhub
    ```
    
* 检查主机是否激活：
    `$ docker-machine active`

# 创建Docker网络

* 使用Docker网络的优点有：
    * 容器独立：只有在这个网络上的容器才能互相通信
    * 名字解析：允许我们通过名字来访问同一个网络上的容器
    
* 创建一个名字为 *jupyterhub-network* 的Docker网络
    `$ docker network create jupyterhub-network`
    * 下面我们会配置 JupyterHub 和 single-user Jupyter Notebook 容器来附着在这个网络上。
    
    












