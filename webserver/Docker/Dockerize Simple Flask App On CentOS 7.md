# Dockerize Simple Flask App in CentOS 7

## 所需软件
* Docker
* Python 2.7
* CentOS 7 x64


## 安装Docker

* 添加docker的repo
    * `$ sudo  /etc/yum.repo.d/docker.repo`
    * 添加以下内容：
    ```
        [dockerrepo]
        name=Docker Repository
        baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
        enabled=1
        gpgcheck=1
        gpgkey=https://yum.dockerproject.org/gpg    
    ```
* 安装Docker包
    * `$ sudo yum install docker-engine`
    
* 启动Docke服务
    * `$ sudo service docker start`
    
* 验证Docke是否正确安装
    * `$ sudo docker run hello-world`
    
## 创建文件夹、Flask应用及Dockfile

* 文件夹结构如下：
    ```
        |-flaska
          |-app/
            |-app.py
            |-Dockfile
            |-requirements.txt
    ```

* 创建文件夹
    * `$ mkdir flaska` 
    * `$ mkdir flaska/app` 
* 创建Flask脚本 
    * *app/app.py*
    ```
        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def hello_world():
            return 'Flask Dockerized'

        if __name__ == '__main__':
            app.run(debug=True,host='0.0.0.0')    
    ```
* 创建Flask所需插件列表： 
    * *app/requirements.txt* 
    ```
        Flask=0.10.1
    ```
    * 当出现版本不兼容时，可以将版本号去掉，直接写： `Flask`
    
* 创建Dockerfile文件
    * 该文件描述了需要哪些软件，以及将怎样将这些软件“烧录”成为镜像文件。
    * *app/Dockerfile*
    ```
        FROM centos:latest
        COPY . /app
        WORKDIR /app
        RUN yum -y install epel-release
        RUN yum repolist
        RUN yum -y install python-pip
        RUN pip install -r requirements.txt
        ENTRYPOINT ["python"]
        CMD ["app.py"]    
    ```
    
    * `FROM centos:latest` : 基于最新的CentOS镜像来制作镜像文件
    * `COPY . /app` : 
    * `WORKDIR /app` : 
    * `RUN yum -y install epel-release` : 
    * `RUN yum repolist` : 
    * `RUN yum -y install python-pip` : 
    * `RUN pip install -r requirements.txt` : 
    * `ENTRYPOINT ["python"]` : 
    * `CMD ["app.py"]` : 
    
    * 
    
## 制作镜像、运行测试

* 制作Docker镜像
    * 从 *app* 文件夹中运行如下命令：
        `$ docker build -t flaska:latest .`
        * 不要忽略了最后面的 *.* ，表示当前文件夹
        * *-t* 标签，命令为 *flaska* 的标签
        
* 运行Docker容器
    * 同样从 *app* 中运行：
        `$ docker run -d -p 5000:5000 flaska`
        * *-d* ：在后台运行
        
* 测试
    * CentOS本地浏览器中打开 *http://127.0.0.1:5000*
    * 其他机器浏览器中打开 *http://A.B.C.D:5000*
    
    
## 错误及解决

* `docker: Error response from daemon: Container command not found or does not exist..`
    * 运行：`docker run -d -p 5000:5000 flaska`
    * 试着运行：`docker run -i -t flaska`
        * 提示：`exec: "PATHON" : executable file not found in $PATH`
        * 由此可以看出在$PATH中没有 *python* ，这很奇怪，同样安装的两台centos vm，一样的操作，两种结果
        * 解决：修改 *Dockerfile* 文件最后两句为：
            ```
                # ENTRYPOINT ["python"]
                CMD ["python", "app.py"]    
            ```
        
 
 
 
 
 
 
 
 
 