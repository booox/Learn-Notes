# cSphere Docker 实训课程

# cSphere Docker Training

From : [cSphere Docker Training](http://csphere.cn/training)
Other Links:
    [http://edu.51cto.com/](http://edu.51cto.com/) viid
    [cyzhang: git.oschina.net](https://git.oschina.net/dockerf)
    
* From [cSphere Docker 实训代码](https://github.com/nicescale/docker-training)
* Video: [cSphere Docker 培训视频](http://csphere.cn/training/lesson/0)    


# 第一讲 Docker 实战之入门以及 Dockerfile
    
## 由Dockerfile构建镜像及运行
* `git clone`
    ```
        mkdir docker
        cd docker
        git clone https://github.com/nicescale/docker-training.git
        cd docker-training/first/centos7
    ```
* Dockerfile 文件指令
    * `ENV` : 设置系统环境变量
        * `ENV TERM xterm`
    * `ADD` : 复制文件到container中
        * 与`COPY`不同，可解压、链接
        
    * `RUN` : 复制文件到container中
    * `EXPOSE` : 打开端口
    * `VOLUME` : 增加一个或多个数据卷(目录在容器内部)
        * 在`docker run` 命令后，可以通过 `-v`参数来创建数据卷
    * `ENTRYPOINT` : 
        * 在container每次启动时，需要执行的命令。
        * 如果有多条，则最后一条生效
    * `CMD` : 
    * `ONBUILD` : 
        * 对利用该Dockerfile构建的镜像（如A镜像）不会产生任何实质性作用。
        * 当我们编写一个新的Dockerfile文件来基于前面镜像（A镜像）来构建一个新的镜像（B镜像）时，
            * 构建A镜像的Dockerfile文件中 `ONBUILD` 指令会被执行。
            * 在构建B镜像的过程中，首先会执行 `ONBUILD`指令指定的指令，然后才会执行其它指令。
            
            * ref: [Dockerfile 指令 ONBUILD介绍](http://www.cnblogs.com/51kata/p/5265107.html)
            ```
                xxx@ubuntu:~/myimage$ docker build -t imageb .
                Sending build context to Docker daemon 15.87 kB
                Step 1 : FROM imagea
                # Executing 1 build trigger...
                Step 1 : RUN mkdir mydir
                 ---> Running in e16c35c94b03
                 ---> 4b393d1610a6
                Removing intermediate container e16c35c94b03
            ```
            * 注意这一句：`# Executing 1 build trigger...`
            * 在`FROM`之后，检测到基础镜像里有 `ONBUILD`指令，马上执行触发器（`ONBUILD`指令指定的指令）
            
    
* 创建一个镜像
    * `$ docker build -t ihub/centos:7.1 . `
        * 注意最后有个点，表示当前文件夹为 Dockerfile 所在位置
        * 完整的名字示例：
            `registry_url/namespace/csphere/centos:7.1`
            `registry_url/namespace/csphere/centos:latest`
    
* 其它命令
    * `docker images`
    * `docker ps -a`
    
* 生成一个Docker容器
    * 查看run命令的帮助：`docker help run`
    * `docker run -it `
        * `-it ` : 交互式
        * `-d ` : 后台运行
        * `-p 22` : 容器里端口为22，宿主机找一个随机可用的端口号与22映射
        * `-P 2222:22` : 容器为22, 宿主机为2222
        * `--name` : 给容器命名，方便后面操作
        * `-e` : 在创建容器时向容器内传递一些参数，可以有多个
        * `--rm` : 在容器退出时，将容器删除
        
* 基础镜像 - 中间件镜像 - 应用镜像

## 构建中间件镜像

### 构建php-fpm中间件镜像

* `cd php-fpm`

* `vi php-fpm/Dockerfile`
    * 由基础镜像开始：`FROM ihub/centos:7.1`
    
* 构建`php-fpm`中间件镜像
    * `docker build -t ihub/php-fpm:5.4 .`
    
    * Error: `Error: fakesystemd conflicts with systemd-219-19.el7_2.9.x86_64`
        * ref: [Fixing CentOS 7 systemd conflicts with docker](https://seven.centos.org/2015/12/fixing-centos-7-systemd-conflicts-with-docker/)
        * 在用`yum install`之前添加下面语句：
            * `RUN yum clean all && yum swap -y fakesystemd systemd`
* 创建一个容器
    * `docker run -d -p 8080:80 --name website ihub/php-fpm:5.4`
    
* 测试访问web
    * `ip:8080/info.php`
    
* 进入container里
    * `docker exec -it website /bin/bash`
    
    * 查看 `supervisor`运行的进程
        `supervisorctl` (回车)
        
### 构建mysql中间件镜像

* `cd mysql`

* `vi mysql/Dockerfile`
    * 由基础镜像开始：`FROM ihub/centos:7.1`
    
* 构建`mysql`中间件镜像
    * `docker build -t ihub/mysql:5.5 .`

* 查看 images
    * `docker images`
    
* 运行 mysql 容器
    `docker run -d -p 3306:3306 --name dbserver ihub/mysql:5.5`
    
* `docker ps -a`

* 登陆到 dbserver 的容器里
    `docker exec -it dbserver /bin/bash`
    `mysql`
    `MariaDB [(none)]> show databases;`
    `exit`
    
## 删除docker 容器、镜像
    
* 删除镜像: `docker rmi images-name`
* 删除停止容器:  `docker rm container-name`
* 强制删除容器:  `docker rm -f container-name`

## 运行一个挂载数据卷的容器

* `docker run -d -p 3306:3306 -v host_dir:conatiner_dir`
    * `docker run -d -p 3306:3306 --name dbserver -v host_dir:conatiner_dir ihub/mysql`
    
* 创建好容器之后，建立一些数据，然后将container 删除，查看数据是否还在？
    * 
        ```
            docker exec -it dbserver /bin/bash
            MariaDB [(none)]> show databases;
            MariaDB [(none)]> create database mydb;
            MariaDB [(none)]> show databases;
        ```
    * 挂载的数据卷宿主机与容器之间是同步的，此时到宿主机的挂载点查看是否有 `mydb` 文件夹
        `ll host_dir`
        
    * 把容器删除
        ```
            docker stop dbserver
            docker rm dbserver
        ```
    * 查看宿主机的挂载点中的 `mydb` 是否还在
        * 可以发现文件还在: `ll host_dir`
    
* 再次创建一个新的容器 `newdb`， 将宿主机中包含 `mydb`数据的文件夹再次挂载回来，看是否可用？
    * 创建新容器 `newdb` ，挂载原数据文件
        `docker run -d -p 3306:3306 --name newdb -v /home/lunn/docker-projects/vfs/dir/mydata:/var/lib/mysql ihub/mysql:5.5 `
        
    * 查看容器状态
        `docker ps`  (只显示UP的容器)
    * 进入容器中的 mysql，查看 `mydb`是否还在
        ```
            $ docker exec -it newdb /bin/bash
            # mysql
            MariaDB [(none)]> show databases;
        ```
    * 可以发现数据还在，非常方便 

## 利用 中间件镜像生成 应用镜像

* `cd wordpress`

* `vi wordpress/Dockerfile`

    * `FROM ihub/php-fpm:5.4` : 由基础镜像开始
    
        * 在构建 `ihub/php-fpm:5.4`的Dockerfile文件中有这样两句：
            ```
                ONBUILD ADD . /app
                ONBUILD RUN chown -R nginx:nginx /app
            ```
            * 这两句在构建 `wordpress` 的镜像时会被执行
            
        * 但在具体的应用服务器里将 `Dockerfile`也包括在里面显然没有必要，则可以排除掉。
            * 可以通过 `.dockerignore` 来进行文件的排除
                ```
                    vi .dockerignore
                    Dockerfile
                ```
                * 在执行 `ADD . /app` 时，`Dockerfile`会被排除掉。
    * `ADD init.sh /init.sh` : 添加 `init.sh`到系统根目录
    
        * `init.sh` 第一行： `set -e` ，表明如果后面语句执行过程中发生错误则停止往下执行
        
        * 其它主要是添加了 wordpress 运行的一些设置
            * `WORDPRESS_DB_HOST`
            * `WORDPRESS_DB_PASSWORD`
            * `.htaccess`
        
        * 最一行 `exec "$@"`
            * 在 `Dockerfile`中有这样一行：
                `ENTRYPOINT ["/init.sh", "/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]`
            * 这表示先执行完 `init.sh` ，然后接着执行后面的命令
                * 也即利用`supervisord`启动`mysql`和`php-fpm`：
                    `"/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"`
        
    
* 构建`wordpress`应用镜像
    * `docker build -t ihub/wordpress:4.2 .`

    * 这个过程会非常快，这也给以后重启服务、更新版本或快速部署带来了可能
    
* `docker images`

## 创建应用容器，连接 *mysql* 和 `php-fpm`

* 创建应用容器时，想让 `wordpress` 使用 前面已创建的 `mysql`和`php-fpm`容器
    * 可以通过 `docker run -e` 这个参数
        * 查看`mysql`容器的IP
            * `docker exec -it dbserver bash`
            * `ip addr` (CentOS 7)
            * 假设为： `172.17.0.4`
* `-e` 这个参数可以写多次
    * `docker run -d -p 80:80 --name wordpress -e WORDPRESS_DB_HOST=172.17.0.4 -e WORDPRESS_DB_USER=admin -e WORDPRESS_DB_PASSWORD=dbpass ihub/wordpress:4.2`

* 浏览器中访问宿主机的IP（端口默认为80）
    可以看到 `wordpress`不需要数据库的配置直接进入语言选择的页面
    
# ENTRYPOINT 与 CMD 区别

## ENTRYPOINT
* 在 Dockerfile 中 ENTRYPOINT 只有最后一行生效，会被执行。
* 运行一个 ENTRYPOINT 就像运行一个程序一样
    * 大概有两种写法：
        * 列表方法（推荐）：
            `ENTRYPOINT ["executable", "param1", "param2"]`
            
        * shell 格式:
            `ENTRYPOINT command param1 param2`
            
            
## CMD

### CMD用法

* 第一种用法：运行一个可执行的文件并提供运行的参数(推荐)
    * `CMD ["executable", "param1", "param2"]`
    
* 第二种用法：为 ENTRYPOINT 指定参数 （默认用法 ）
    * `CMD ["param1", "param2"]`
    
* 第三种用法：以 `/bin/sh -c`的方法执行的命令 （Shell 格式）
    * `CMD command param1 param2`
    
    * eg:
        `CMD ["/bin/echo", "This is test CMD"]`
        `docker run -it -rm csphere/cmd:0.1 /bin/bash`
        
### 测试 ENTRYPOINT and CMD 实例

#### CMD
* 创建一个 Dockerfile
    ```
        vi Dockerfile
        FROM centos:7
        
        CMD ["/bin/echo", "This is a CMD test."]
    ```
* 创建一个镜像
    `docker -t ihub/cmd:0.1 .`
    
* 启动一个容器
    ```
        docker run -it --rm ihub/cmd:0.1
        This is a CMD test.  (这是执行后回显出来的)
    ```
* 可以用其它命令来替换CMD中的命令
    * 如可以用 `/bin/bash` 来替换上述 `/bin/echo`
        `docker run -it ihub/cmd:0.1 /bin/bash`
        * 执行上述命令后，会进入到 container 当中
        
        
#### ENTRYPOINT
* 创建一个 Dockerfile
    ```
        vi Dockerfile
        FROM centos:7
        
        ENTRYPOINT ["/bin/echo", "This is a ENTRYPOINT test."]
    ```
* 创建一个镜像
    `docker -t ihub/ent:0.1 .`
    
* 启动一个容器
    ```
        docker run -it --rm ihub/ent:0.1
        This is a ENTRYPOINT test.  (这是执行后回显出来的)
    ```
* ENTRYPOINT 中的命令不可以用其它命令来替换
    * 如可以用 `/bin/bash` 来替换上述 `/bin/echo`
        `docker run -it ihub/ent:0.1 /bin/bash`
        `This is a ENTRYPOINT test.  /bin/bash`
    * 它会将后面跟着的 `bin/bash` 当作 `/bin/echo`的参数
    
* 如果想要替换 ENTRYPOINT 当中的命令，可以使用`--entrypoint=` 参数
    * ``
        
        dfdf
        
# 第二讲 Docker 实战之 Registry以及持续集成

部署一个企业内部的 Registry 服务

## 启动企业的 registry 服务

* `pull` 下 registry
    `docker pull registry:2`

* 运行 docker registry
    `docker run -d -p 5000:5000 --restart=always --name registry -v "$(pwd)/data:/var/lib/registry" registry:2`
    * `-v "$(pwd)/data:/var/lib/registry"` : 添加数据卷
        * `$(pwd)/data` :　宿主机当前目录下的 data 目录
        * `/var/lib/registry` : 容器内部目录
        

* 启动好 registry 服务之后，可以将本地的 docker 镜像上传到企业的 registry 仓库中

* 命名规则：
    `registry_url/namespace/image_name/version(tag)`
    `registry_url/ihub/wordpress:4.2`
    
* 打 tag
    * 按完整的命名规则，给本地镜像打上 tag 
    `docker tag ihub/mysql:5.5 registry_url/ihub/mysql:5.5`
* 查看 registry 是否启动
    `docker ps -a`
    
    
    
## 利用 docker-compose 控制多个容器

### docker-compose 配置文件

* 文件为： `docker-compose.yml, docker-compose.yaml`

```
mysql:
   image: csphere/mysql:5.5
   ports: 
     - "3306:3306"
   volumes:
     - /var/lib/docker/vfs/dir/dataxc:/var/lib/mysql
   hostname: mydb.server.com

tomcat:
   image: csphere/tomcat:7.0.55
   ports:
      - "8080:8080"
   links:
      - mysql:db
   environment:
      - TOMCAT_USER=admin
      - TOMCAT_PASS=admin
   hostname: tomcat.server.com    

```

### 启动、停止文件

* 在包含 `docker-compose.yml` 的文件内执行

* `docker-compose up` : 启动
* `docker-compose stop` : 停止
* `docker-compose ps` : 查看


## 利用 git 仓库自动构建

