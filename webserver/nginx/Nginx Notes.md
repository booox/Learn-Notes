
# Folers and Files
    
* Site Files Directory
    `/usr/share/nginx/html`
* Nginx global configuration File
    `/etc/nginx/nginx.conf`
* sites and virtual sites configuration
    `/etc/nginx/conf.d/default.conf`
* nginx exec files
    `/usr/sbin/nginx`
* nginx log file
    `/var/log/nginx/access.log`
    `/var/log/nginx/error.log`

# Nginx on CentOS 7
* Install *nginx* on CentOS
    1. Install EPEL
        `$ sudo yum install epel-release`
    2. Install nginx
        `$ sudo yum install nginx`
        
    3. Starting Nginx
        `$ sudo systemctl start nginx`
    
    4. set Nginx as a service
        `$ sudo systemctl enable nginx`
        
    5. check Nginx status
        `$ sudo systemctl status nginx`
        
        ```
            nginx.service - nginx - high performance web server
            Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; vendor preset: disabled)
            Active: active (running) since Fri 2016-04-08 22:59:29 CST; 7h ago
            Docs: http://nginx.org/en/docs/
         Main PID: 7587 (nginx)
           CGroup: /system.slice/nginx.service
                   ├─7587 nginx: master process /usr/sbin/nginx -c /etc/nginx/nginx.conf
                   └─7588 nginx: worker process
        
        ```
        * Note : master process `/usr/sbin/nginx -c /etc/nginx/nginx.conf`
        
        
        
    ```
        systemctl用法

            #自启动
            systemctl enable docker.service
            #关闭自启动
            systemctl disable docker.service
            #显示已启动服务
            systemctl list-unit-files --type=service
             
            #检查服务状态
            #服务详细信息
            systemctl status docker.service
            #仅显示是否 Active
            systemctl is-active docker.service
            #启动服务
            systemctl start docker.service
            #暂停服务
            systemctl stop docker.service
            #重启服务
            systemctl restart docker.service
    ```
    
## shell command

* `$ sudo nginx -t` : test configuration and exit
 


## Creating a Virtual Server

* */etc/nginx/conf.d/* : default virtual server config

* We must setup at least one virtual server for Nginx, in order to process the HTTP request by Nginx.
    * When Nginx process the request,  it looks for the server *directive* which is placed in `http context` . 
    * You can add multiple server directives, to define multiple virtual servers.
    
* Example
    * */etc/nginx/conf.d/itzgeek.conf*
    ```
        $ cp /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/itzgeek.conf
        $ vi /etc/nginx/conf.d/itzgeek.conf
        
        server {
            listen       80;
            server_name  server.itzgeek.com;
            
            location / {
            root   /usr/share/nginx/html/itzgeek;
            index  index.html index.htm;
            }
        }
    
    ```
    * Create root directory
        `mkdir /usr/share/nginx/html/itzgeek`
    * Create Index.html page.
        `echo “This is ITzGeek Home” > /usr/share/nginx/html/itzgeek/index.html`
    * Test it.
 
# Links
 
- [Nginx配置及应用场景之基本配置](http://www.blogways.net/blog/2013/10/21/nginx-2.html)
- [Nginx配置及应用场景之高级配置](http://www.blogways.net/blog/2013/10/22/nginx-3.html)
- [nginx的启动流程和接客流程](http://www.cnblogs.com/wully/archive/2011/12/23/2299792.html)
- [Virtual Hosts on nginx (CSC309)](https://gist.github.com/soheilhy/8b94347ff8336d971ad0#step-9-optional----redirecting-based-on-host-name)
- [Nginx from ubuntu wiki](http://wiki.ubuntu.com.cn/Nginx)
- []()
 
 
## Supervisor with Nginx

* The ngix process must start in foreground (not as a daemon) to be controlled by supervisor. 


## Question and Answer

* `[emerg] 13420#0: bind() to 0.0.0.0:8000 failed (13: Permission denied)`
    * This will most likely be related to SELinux
        ```
            semanage port -l | grep http_port_t
            http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
        ```
        * SELinux in *enforcing* mode http is only allowed to bind to the listed ports.
    * Add the ports you want to bind on to the list
        `semanage port -a -t http_port_t -p tcp 8090`
        
* `nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)`
    * If I run:
        ```
            $ sudo lsof -i :80
            [root@localhost ~]# lsof -i :80
            COMMAND   PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
            nginx   15480 nginx    6u  IPv4  14939      0t0  TCP *:http (LISTEN)
            nginx   15954  root    6u  IPv6 936801      0t0  TCP *:http (LISTEN)
            
            reset and run again:
            [root@localhost ~]# lsof -i :80
            COMMAND PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
            nginx   683  root    6u  IPv4  15547      0t0  TCP *:http (LISTEN)
            nginx   683  root    7u  IPv6  15548      0t0  TCP *:http (LISTEN)
            nginx   685 nginx    6u  IPv4  15547      0t0  TCP *:http (LISTEN)
            nginx   685 nginx    7u  IPv6  15548      0t0  TCP *:http (LISTEN)
        ```
        * 这里有两个用户同时在运行nginx: *nginx* 和 *root*
        
    * Run `netstat -lntp |grep :80`
        ```
            [root@localhost ~]# netstat -lntp |grep :80
            tcp        0      0 0.0.0.0:8008            0.0.0.0:*               LISTEN      683/nginx: master p 
            tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      683/nginx: master p 
            tcp6       0      0 :::80                   :::*                    LISTEN      683/nginx: master p 
        
        ```
    
    
        * Run, `$ sudo fuser -k 80/tcp `
            `sudo: fuser: command not found`
* `"proxy_pass" cannot have URI part in location given by regular expression  `
    * 相关代码如下：
    ```
        location ~* /(user/[^/]*)/(api/kernels/[^/]+/channels|terminals/websocket)/? {
            proxy_pass http://localhost:8000/;

            proxy_set_header X-Real-IP $remote_addr;
        }
    
    ```
    * 原因是当 *location* 中使用了正则表达式之后，则 *proxy_pass* 不能以 */* 结尾，删除即可。
    
    
    
    