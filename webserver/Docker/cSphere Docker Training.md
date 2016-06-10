# cSphere Docker ʵѵ�γ�

# cSphere Docker Training

From : [cSphere Docker Training](http://csphere.cn/training)
Other Links:
    [http://edu.51cto.com/](http://edu.51cto.com/) viid
    [cyzhang: git.oschina.net](https://git.oschina.net/dockerf)
    
* From [cSphere Docker ʵѵ����](https://github.com/nicescale/docker-training)
* Video: [cSphere Docker ��ѵ��Ƶ](http://csphere.cn/training/lesson/0)    


# ��һ�� Docker ʵս֮�����Լ� Dockerfile
    
## ��Dockerfile������������
* `git clone`
    ```
        mkdir docker
        cd docker
        git clone https://github.com/nicescale/docker-training.git
        cd docker-training/first/centos7
    ```
* Dockerfile �ļ�ָ��
    * `ENV` : ����ϵͳ��������
        * `ENV TERM xterm`
    * `ADD` : �����ļ���container��
        * ��`COPY`��ͬ���ɽ�ѹ������
        
    * `RUN` : �����ļ���container��
    * `EXPOSE` : �򿪶˿�
    * `VOLUME` : ����һ���������ݾ�(Ŀ¼�������ڲ�)
        * ��`docker run` ����󣬿���ͨ�� `-v`�������������ݾ�
    * `ENTRYPOINT` : 
        * ��containerÿ������ʱ����Ҫִ�е����
        * ����ж����������һ����Ч
    * `CMD` : 
    * `ONBUILD` : 
        * �����ø�Dockerfile�����ľ�����A���񣩲�������κ�ʵ�������á�
        * �����Ǳ�дһ���µ�Dockerfile�ļ�������ǰ�澵��A����������һ���µľ���B����ʱ��
            * ����A�����Dockerfile�ļ��� `ONBUILD` ָ��ᱻִ�С�
            * �ڹ���B����Ĺ����У����Ȼ�ִ�� `ONBUILD`ָ��ָ����ָ�Ȼ��Ż�ִ������ָ�
            
            * ref: [Dockerfile ָ�� ONBUILD����](http://www.cnblogs.com/51kata/p/5265107.html)
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
            * ע����һ�䣺`# Executing 1 build trigger...`
            * ��`FROM`֮�󣬼�⵽������������ `ONBUILD`ָ�����ִ�д�������`ONBUILD`ָ��ָ����ָ�
            
    
* ����һ������
    * `$ docker build -t ihub/centos:7.1 . `
        * ע������и��㣬��ʾ��ǰ�ļ���Ϊ Dockerfile ����λ��
        * ����������ʾ����
            `registry_url/namespace/csphere/centos:7.1`
            `registry_url/namespace/csphere/centos:latest`
    
* ��������
    * `docker images`
    * `docker ps -a`
    
* ����һ��Docker����
    * �鿴run����İ�����`docker help run`
    * `docker run -it `
        * `-it ` : ����ʽ
        * `-d ` : ��̨����
        * `-p 22` : ������˿�Ϊ22����������һ��������õĶ˿ں���22ӳ��
        * `-P 2222:22` : ����Ϊ22, ������Ϊ2222
        * `--name` : ����������������������
        * `-e` : �ڴ�������ʱ�������ڴ���һЩ�����������ж��
        * `--rm` : �������˳�ʱ��������ɾ��
        
* �������� - �м������ - Ӧ�þ���

## �����м������

### ����php-fpm�м������

* `cd php-fpm`

* `vi php-fpm/Dockerfile`
    * �ɻ�������ʼ��`FROM ihub/centos:7.1`
    
* ����`php-fpm`�м������
    * `docker build -t ihub/php-fpm:5.4 .`
    
    * Error: `Error: fakesystemd conflicts with systemd-219-19.el7_2.9.x86_64`
        * ref: [Fixing CentOS 7 systemd conflicts with docker](https://seven.centos.org/2015/12/fixing-centos-7-systemd-conflicts-with-docker/)
        * ����`yum install`֮ǰ���������䣺
            * `RUN yum clean all && yum swap -y fakesystemd systemd`
* ����һ������
    * `docker run -d -p 8080:80 --name website ihub/php-fpm:5.4`
    
* ���Է���web
    * `ip:8080/info.php`
    
* ����container��
    * `docker exec -it website /bin/bash`
    
    * �鿴 `supervisor`���еĽ���
        `supervisorctl` (�س�)
        
### ����mysql�м������

* `cd mysql`

* `vi mysql/Dockerfile`
    * �ɻ�������ʼ��`FROM ihub/centos:7.1`
    
* ����`mysql`�м������
    * `docker build -t ihub/mysql:5.5 .`

* �鿴 images
    * `docker images`
    
* ���� mysql ����
    `docker run -d -p 3306:3306 --name dbserver ihub/mysql:5.5`
    
* `docker ps -a`

* ��½�� dbserver ��������
    `docker exec -it dbserver /bin/bash`
    `mysql`
    `MariaDB [(none)]> show databases;`
    `exit`
    
## ɾ��docker ����������
    
* ɾ������: `docker rmi images-name`
* ɾ��ֹͣ����:  `docker rm container-name`
* ǿ��ɾ������:  `docker rm -f container-name`

## ����һ���������ݾ������

* `docker run -d -p 3306:3306 -v host_dir:conatiner_dir`
    * `docker run -d -p 3306:3306 --name dbserver -v host_dir:conatiner_dir ihub/mysql`
    
* ����������֮�󣬽���һЩ���ݣ�Ȼ��container ɾ�����鿴�����Ƿ��ڣ�
    * 
        ```
            docker exec -it dbserver /bin/bash
            MariaDB [(none)]> show databases;
            MariaDB [(none)]> create database mydb;
            MariaDB [(none)]> show databases;
        ```
    * ���ص����ݾ�������������֮����ͬ���ģ���ʱ���������Ĺ��ص�鿴�Ƿ��� `mydb` �ļ���
        `ll host_dir`
        
    * ������ɾ��
        ```
            docker stop dbserver
            docker rm dbserver
        ```
    * �鿴�������Ĺ��ص��е� `mydb` �Ƿ���
        * ���Է����ļ�����: `ll host_dir`
    
* �ٴδ���һ���µ����� `newdb`�� ���������а��� `mydb`���ݵ��ļ����ٴι��ػ��������Ƿ���ã�
    * ���������� `newdb` ������ԭ�����ļ�
        `docker run -d -p 3306:3306 --name newdb -v /home/lunn/docker-projects/vfs/dir/mydata:/var/lib/mysql ihub/mysql:5.5 `
        
    * �鿴����״̬
        `docker ps`  (ֻ��ʾUP������)
    * ���������е� mysql���鿴 `mydb`�Ƿ���
        ```
            $ docker exec -it newdb /bin/bash
            # mysql
            MariaDB [(none)]> show databases;
        ```
    * ���Է������ݻ��ڣ��ǳ����� 

## ���� �м���������� Ӧ�þ���

* `cd wordpress`

* `vi wordpress/Dockerfile`

    * `FROM ihub/php-fpm:5.4` : �ɻ�������ʼ
    
        * �ڹ��� `ihub/php-fpm:5.4`��Dockerfile�ļ������������䣺
            ```
                ONBUILD ADD . /app
                ONBUILD RUN chown -R nginx:nginx /app
            ```
            * �������ڹ��� `wordpress` �ľ���ʱ�ᱻִ��
            
        * ���ھ����Ӧ�÷������ｫ `Dockerfile`Ҳ������������Ȼû�б�Ҫ��������ų�����
            * ����ͨ�� `.dockerignore` �������ļ����ų�
                ```
                    vi .dockerignore
                    Dockerfile
                ```
                * ��ִ�� `ADD . /app` ʱ��`Dockerfile`�ᱻ�ų�����
    * `ADD init.sh /init.sh` : ��� `init.sh`��ϵͳ��Ŀ¼
    
        * `init.sh` ��һ�У� `set -e` ����������������ִ�й����з���������ֹͣ����ִ��
        
        * ������Ҫ������� wordpress ���е�һЩ����
            * `WORDPRESS_DB_HOST`
            * `WORDPRESS_DB_PASSWORD`
            * `.htaccess`
        
        * ��һ�� `exec "$@"`
            * �� `Dockerfile`��������һ�У�
                `ENTRYPOINT ["/init.sh", "/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]`
            * ���ʾ��ִ���� `init.sh` ��Ȼ�����ִ�к��������
                * Ҳ������`supervisord`����`mysql`��`php-fpm`��
                    `"/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"`
        
    
* ����`wordpress`Ӧ�þ���
    * `docker build -t ihub/wordpress:4.2 .`

    * ������̻�ǳ��죬��Ҳ���Ժ��������񡢸��°汾����ٲ�������˿���
    
* `docker images`

## ����Ӧ������������ *mysql* �� `php-fpm`

* ����Ӧ������ʱ������ `wordpress` ʹ�� ǰ���Ѵ����� `mysql`��`php-fpm`����
    * ����ͨ�� `docker run -e` �������
        * �鿴`mysql`������IP
            * `docker exec -it dbserver bash`
            * `ip addr` (CentOS 7)
            * ����Ϊ�� `172.17.0.4`
* `-e` �����������д���
    * `docker run -d -p 80:80 --name wordpress -e WORDPRESS_DB_HOST=172.17.0.4 -e WORDPRESS_DB_USER=admin -e WORDPRESS_DB_PASSWORD=dbpass ihub/wordpress:4.2`

* ������з�����������IP���˿�Ĭ��Ϊ80��
    ���Կ��� `wordpress`����Ҫ���ݿ������ֱ�ӽ�������ѡ���ҳ��
    
# ENTRYPOINT �� CMD ����

## ENTRYPOINT
* �� Dockerfile �� ENTRYPOINT ֻ�����һ����Ч���ᱻִ�С�
* ����һ�� ENTRYPOINT ��������һ������һ��
    * ���������д����
        * �б������Ƽ�����
            `ENTRYPOINT ["executable", "param1", "param2"]`
            
        * shell ��ʽ:
            `ENTRYPOINT command param1 param2`
            
            
## CMD

### CMD�÷�

* ��һ���÷�������һ����ִ�е��ļ����ṩ���еĲ���(�Ƽ�)
    * `CMD ["executable", "param1", "param2"]`
    
* �ڶ����÷���Ϊ ENTRYPOINT ָ������ ��Ĭ���÷� ��
    * `CMD ["param1", "param2"]`
    
* �������÷����� `/bin/sh -c`�ķ���ִ�е����� ��Shell ��ʽ��
    * `CMD command param1 param2`
    
    * eg:
        `CMD ["/bin/echo", "This is test CMD"]`
        `docker run -it -rm csphere/cmd:0.1 /bin/bash`
        
### ���� ENTRYPOINT and CMD ʵ��

#### CMD
* ����һ�� Dockerfile
    ```
        vi Dockerfile
        FROM centos:7
        
        CMD ["/bin/echo", "This is a CMD test."]
    ```
* ����һ������
    `docker -t ihub/cmd:0.1 .`
    
* ����һ������
    ```
        docker run -it --rm ihub/cmd:0.1
        This is a CMD test.  (����ִ�к���Գ�����)
    ```
* �����������������滻CMD�е�����
    * ������� `/bin/bash` ���滻���� `/bin/echo`
        `docker run -it ihub/cmd:0.1 /bin/bash`
        * ִ����������󣬻���뵽 container ����
        
        
#### ENTRYPOINT
* ����һ�� Dockerfile
    ```
        vi Dockerfile
        FROM centos:7
        
        ENTRYPOINT ["/bin/echo", "This is a ENTRYPOINT test."]
    ```
* ����һ������
    `docker -t ihub/ent:0.1 .`
    
* ����һ������
    ```
        docker run -it --rm ihub/ent:0.1
        This is a ENTRYPOINT test.  (����ִ�к���Գ�����)
    ```
* ENTRYPOINT �е���������������������滻
    * ������� `/bin/bash` ���滻���� `/bin/echo`
        `docker run -it ihub/ent:0.1 /bin/bash`
        `This is a ENTRYPOINT test.  /bin/bash`
    * ���Ὣ������ŵ� `bin/bash` ���� `/bin/echo`�Ĳ���
    
* �����Ҫ�滻 ENTRYPOINT ���е��������ʹ��`--entrypoint=` ����
    * ``
        
        dfdf
        
# �ڶ��� Docker ʵս֮ Registry�Լ���������

����һ����ҵ�ڲ��� Registry ����

## ������ҵ�� registry ����

* `pull` �� registry
    `docker pull registry:2`

* ���� docker registry
    `docker run -d -p 5000:5000 --restart=always --name registry -v "$(pwd)/data:/var/lib/registry" registry:2`
    * `-v "$(pwd)/data:/var/lib/registry"` : ������ݾ�
        * `$(pwd)/data` :����������ǰĿ¼�µ� data Ŀ¼
        * `/var/lib/registry` : �����ڲ�Ŀ¼
        

* ������ registry ����֮�󣬿��Խ����ص� docker �����ϴ�����ҵ�� registry �ֿ���

* ��������
    `registry_url/namespace/image_name/version(tag)`
    `registry_url/ihub/wordpress:4.2`
    
* �� tag
    * ���������������򣬸����ؾ������ tag 
    `docker tag ihub/mysql:5.5 registry_url/ihub/mysql:5.5`
* �鿴 registry �Ƿ�����
    `docker ps -a`
    
    
    
## ���� docker-compose ���ƶ������

### docker-compose �����ļ�

* �ļ�Ϊ�� `docker-compose.yml, docker-compose.yaml`

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

### ������ֹͣ�ļ�

* �ڰ��� `docker-compose.yml` ���ļ���ִ��

* `docker-compose up` : ����
* `docker-compose stop` : ֹͣ
* `docker-compose ps` : �鿴


## ���� git �ֿ��Զ�����

