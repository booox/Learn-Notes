
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
- []()
- [Nginx from ubuntu wiki](http://wiki.ubuntu.com.cn/Nginx)
- []()
 
 
 