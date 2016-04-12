# Supervisor


# Components

* 
    ```
        /usr/bin/echo_supervisord_conf
        /usr/bin/supervisorctl
        /usr/bin/supervisord
    ```
    
    
# Get started

* Installing via pip
    `$ sudo pip install supervisor` (use *root* )
    
* Creating a Configuration File
    * 如果有 *root* 权限，则将配置文件存放到 */etc* 中
        `$ sudo echo_supervisord_conf > /etc/supervisord.conf`
    * 如果没有 *root* 权限，则可以将 *supervisord.conf* 放到当前文件夹中
        `$ echo_supervisord_conf > supervisord.conf`
        
    * 接着就可以用 *supervisord* 加上 *-c* 跟着配置文件夹来启动 *supervisor* 了。
    
* Running supervisord
    `$ sudo supervisord -c /etc/supervisord.conf`
    
* Running supervisord automatically on startup
    * First Try this in CentOS 7 :`$ systemctl enable supervisord.service`
        * If worked : `Created symlink from /etc/systemd/system/multi-user.target.wants/supervisord.service to /usr/lib/systemd/system/supervisord.service.`
        
    * If not:
        * Copy the raw content: [centos-systemd-etcs](https://github.com/Supervisor/initscripts/blob/master/centos-systemd-etcs)
        ```
                # supervisord service for sysstemd (CentOS 7.0+)
                # by ET-CS (https://github.com/ET-CS)
                [Unit]
                Description=Supervisor daemon

                [Service]
                Type=forking
                ExecStart=/usr/bin/supervisord -c /etc/supervisord.conf
                ExecStop=/usr/bin/supervisorctl $OPTIONS shutdown
                ExecReload=/usr/bin/supervisorctl $OPTIONS reload
                KillMode=process
                Restart=on-failure
                RestartSec=42s

                [Install]
                WantedBy=multi-user.target
        
        ```
        
        * Edit the file : `$ sudo vi /etc/systemd/system/supervisord.service`
        

[按需讲解之Supervisor](http://www.cnblogs.com/yjf512/archive/2012/03/05/2380496.html)

* 我现在有一个进程需要每时每刻不断的跑，但是这个进程又有可能由于各种原因有可能中断。当进程中断的时候我希望能自动重新启动它，此时，我就需要使用到了Supervisor

* *supervisord* : 服务器端程序　启动supervisor就是运行这个命令
* *supervisorctl* : supervisorctl

* Install
    `$ pip install supervisor`
    
* check it work
    `$ echo_supervisord_conf`
    
* creat config file
    `$ echo_supervisord_conf > /etc/supervisord.conf`
    
* *supervisord.conf* 
    ```
        [program:redis]

        command = redis-server   //需要执行的命令

        autostart=true    //supervisor启动的时候是否随着同时启动

        autorestart=true   //当程序跑出exit的时候，这个program会自动重启

        startsecs=3  //程序重启时候停留在runing状态的秒数
    
    ```
    
* run
    * 
    ```
        supervisord    //启动supervisor

        supervisorctl   //打开命令行

        [root@vm14211 ~]# supervisorctl 
        redis                            RUNNING    pid 24068, uptime 3:41:55

        ctl中： help   //查看命令

        ctl中： status  //查看状态    
    
    ```
    
    
    
```
    [program:myapp]
    command=/home/rsj217/rsj217/myproject/venv/bin/gunicorn -w4 -b0.0.0.0:2170 myapp:app    ; supervisor启动命令
    directory=/home/rsj217/rsj217/myproject                                                 ; 项目的文件夹路径
    startsecs=0                                                                             ; 启动时间
    stopwaitsecs=0                                                                          ; 终止等待时间
    autostart=false                                                                         ; 是否自动启动
    autorestart=false                                                                       ; 是否自动重启
    stdout_logfile=/home/rsj217/rsj217/myproject/log/gunicorn.log                           ; log 日志
    stderr_logfile=/home/rsj217/rsj217/myproject/log/gunicorn.err                           ; 错误日志

```
    
    
    
    
    
    
    
# Question & Answer

* `unix:///tmp/supervisor.sock no such file` when run `supervisorctl -c supervisor.conf status`
    ```
        supervisord -c /etc/supervisord.conf
        supervisorctl -c /etc/supervisord.conf reload
        supervisorctl -c /etc/supervisord.conf restart foo
    
    ```
    * 启动时提示 `unix:///tmp/supervisor.sock no such file`
        * 先启动 *supervisord* ，再查看就可以看到进程跑起来了
        ```
            $ sudo venv
        ```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
