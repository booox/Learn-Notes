Supervisor

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
