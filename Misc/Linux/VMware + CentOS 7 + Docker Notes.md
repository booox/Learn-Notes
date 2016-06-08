VMware + CentOS 7 + Docker Notes

# 在VMware 10中安装CentOS 7

## 安装CentOS 7
* 需要软件:
    * CentOS-7-x86_64-Minimal-1511.iso
    * VMware 10
    
1. BIOS中设置虚拟化显示技术
2. 安装CentOS 7


# 安装Docker

    * [Installation on CentOS](https://docs.docker.com/engine/installation/linux/centos/)
1. 确认核心及操作系统位数
    * Docker 需要64位操作系统
    * CentOS的核心至少要3.10以上的
        ```
            $ uname -r
            3.10.0-229.el7.x86_64        
        ```
2. 用Yum安装Docker
    * 更新 `yum` ，确保yum为最新的。
        `$ sudo yum update`
    * 添加`docker.repo`仓库
        ```
            $ sudo tee /etc/yum.repos.d/docker.repo <<-'EOF'
            [dockerrepo]
            name=Docker Repository
            baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
            enabled=1
            gpgcheck=1
            gpgkey=https://yum.dockerproject.org/gpg
            EOF        
        ```
    * 安装Docker
        * `$ sudo yum install docker-engine`

    `$ sudo yum install docker-engin`
    
3. 启动Docker服务
    * 启动服务
        `$ sudo systemctl start docker.service`
    * 查看docker 状态
        `$ sudo systemctl  status docker.service`
    * 停止docker
        `$ sudo systemctl  stop docker.service`
    * 重启docker
        `$ sudo systemctl  restart docker.service`
        
4. 设置Docker开机启动
    * 开机启动
        `$ sudo systemctl  enable docker.service`
    * 关闭自启动
        `$ sudo systemctl  disable docker.service`
    * 显示已启动服务
        `$ sudo systemctl  list-units --type=service | grep docker`
    
5. 运行测试命令
    `$ sudo docker run hello-world`
    
4. 创建Docker用户组
    * 运行Docker命令需要root权限
    * 为了避免在普通用户下每次运行docker命令时都要输入 `sudo`，可以创建一个Docker用户组。
    
    * 创建Docker用户组
        `$ sudo groupadd docker`
    * 添加用户到docker组
        `$ sudo usermod -aG docker your_username`
    * 登出后再登入
    * 验证运行
        `$ docker run hello-world`


