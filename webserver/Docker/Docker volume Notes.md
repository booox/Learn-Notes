
# Links

* [Docker Tutorial Series](http://blog.flux7.com/blogs/docker/docker-tutorial-series-part-1-an-introduction)
* [五方面深入介绍了Docker Volume的工作原理](http://www.open-open.com/lib/view/open1420611970109.html)
* [Understanding Volumes in Docker](http://container-solutions.com/understanding-volumes-docker/)
* []()

# 数据卷

* From: [Docker volume使用](http://my.oschina.net/guol/blog/271225)
* **数据卷** :     是一个特别指定的目录
    * 该目录利用容器的UFS文件系统可以为容器提供一些稳定的特性或者数据共享。
    * 数据卷可以在多个容器之间共享。
    
## 创建数据卷

### 在 Dockerfile 文件中
    * `VOLUME ["/var/lib/mysql"]`
    * 增加了一个数据卷，指向宿主机的 `/var/lib/mysql`（？）
    
### 在 `docker run` 命令中
    
    * 通过 `-v` 参数可创建一个数据卷，也可以跟多个 `-v` 参数创建多个数据卷
    * 当创建好带有数据卷的容器后，还可以在其他容器中通过 `--volumes-from` 参数来挂载该数据卷
        * 而不管该容器是否运行
    
## 数据卷共享

* 启动一个Volume_Container容器，包含两个数据卷
    `docker run -v /var/volume1 -v /var/volume2 --name Volume_Container ubuntu14.04  linux_command`
    
* 创建App_Container容器，挂载Volume_Container容器中的数据卷
    `docker run -t -i -rm -volumes-from Volume_Container --name App_Container ubuntu14.04  linux_command`
    
* 或者再创建一个容器，挂载App_Container中从Volume_Container挂载的数据卷
    `docker run -t -i -rm -volumes-from App_Container --name LastApp_Container ubuntu14.04  linux_command`
    
* 即使你删除了刚开始的第一个数据卷容器或者中间层的数据卷容器，只要有其他容器使用数据卷，数据卷都不会被删除的。

## 挂载本地主机的目录为数据卷

* 格式： `[host-dir]:[container-dir]:[rw|ro]`

* `docker run -i -t -v /tmp:/mnt ubuntu/14.04:14.04 /bin/bash`
    * 宿主机目录 : `/tmp`
    * 容器目录 : `/mnt`
    
## 备份数据 卷的内容

* 不能使用docker export、save、cp等命令来备份数据卷的内容，因为数据卷是存在于镜像之外的
* 可以：创建一个新容器，挂载数据卷容器，同时挂载一个本地目录，然后把远程数据卷容器的数据卷通过备份命令备份到映射的本地目录里面。 
    * `docker run -rm --volumes-from DATA -v $(pwd):/backup busybox tar cvf /backup/backup.tar /data`