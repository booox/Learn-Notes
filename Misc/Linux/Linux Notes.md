


# Linux Commands

## vim
* install
    * `# yum -y install vim-enhanced`
* set alias
    * `# vi ~/.bashrc`
    * add this line: `# alias vi=vim`
    
* vim with color, line number etc.
    
* display line number in vi (not vim)
    ```
        $ vi ~/.vimrc
        set nu
        set tabstop=4
    ```
* enable vim display color
    * 
* config file
    * ` $ vi ~/.vimrc`
    
* Multi Files
    * You have opened a file, and now you want to open another file(s)
        `:sp file1` (on the vim command status)
        * change view windows
            Double `ctrl + w `
            
    * open multi files at the same time
        `$ vi file1 file2 file3`
        * *:n* next file
        * *:N* previous file
        
* date time
    * `date -R`
    
    * CentOS 同步网络时间
        `# yum -y install ntpdate`
        `# ntpdate asia.pool.ntp.org`
        
    
## other

* tree
    * Install: `sudo yum install tree`
    * `tree -d`
    * `tree -L n`
    * `tree -f`
    
    
* chmod 改变权限有两种方法
    * 符号类型改变文件权限:
        chmod (ugoa) (+-=) (rwx) (file|path)
    * `chmod u+x somefile` : grantly only the owner of that file execution permissions
    * `chmod +x somefile` is the same as `chmod a+x somefile`

* chown 改变文件拥有者和群组
    * 改变文件拥有者为mail用户，群组为mail组
        `$ sudo chown mail:mail filename`
    * 改变指定目录及子目录所有文件
        `$ sudo chown -R mail:mail foldername/`
    
* 修改系统变量 
    `$ echo $PATH`

    * `$ env | grep LANG` check environment
    * 修改系统变量 Change $PATH
        `# vi /etc/profile`
        `export PATH=$PATH:/opt/miniconda2/bin`
        `# source /etc/profile`
        `# echo $PATH` ,确认conda已经添加进去


* find命令
    * From: [LINUX 下查找指定文件](http://www.centrue.me/2011/09/01/linux-find/)
    * 当 `find` 与`-exec`命令配合使用时：
        * 可用 `{}`来代表 `find`查找到的文件名
        * 并用 `\;` 来表示命令结束.
            * `find . -type f -exec ls -l {} \;` : 在当前目录下（递归子目录）查找所有文件，并`ls`出来
            * `find . -user root -exec sudo chown test:test {} \;` : 
                * 在当前目录下（递归子目录）查找所有用户为`root`的文件或目录，
                * 并修改所属用户和用户组为`test`
    * 按名称查找
        * `find . -name readme.txt` : 查找  所有名为readme.txt的文件 （递归子目录）
        * `find . -name \*.txt` : 查找所有 名称以.txt结尾的文件（递归子目录）
        * `find . -name "*.txt"` : 同上
        * `find . -iname \*.txt` : 查找所有 名称以.txt结尾的文件，且不区分大小写（递归子目录）
    * 按类型查找
        * `find . -type d` : 查找当前目录下(递归子目录)的所有目录
        * `find . -type f` : 查找当前目录下(递归子目录)的所有文件
        * `find . -type l` : 查找当前目录下(递归子目录)的所有符号链接
    * 按时间查找
        * `find` 命令有三个选项用于按时间查找，单位为 **小时** :
            * `mtime` : 上次修改时间
            * `atime` : 上次读取或访问时间
            * `ctime` : 上次文件状态变化的时间
        * `find . -mtime -1` : 查找当前目录下(递归子目录)的所有1小时内修改的文件和目录
        * `find . -mtime +1` : 查找当前目录下(递归子目录)的所有超过1小时内修改的文件和目录
        * `find . -mtime 1` : 查找当前目录下(递归子目录)的所有恰好在1小时内修改的文件和目录
        * 以分钟为单位
            * `find . -mmin -10` : 查找当前目录下(递归子目录)的所有10分钟内修改的文件和目录 
            * `find . -mmin +20` : 查找当前目录下(递归子目录)的所有20分钟外1小时内修改的文件和目录
        
    * 与特定的文件比较
        * 有三个相关的选项：
            * `-newer ` : 指内容最近被修改的文件
            * `-anewer` : 指最近被读取过的文件
            * `-cnewer` : 指状态最近发生变化的文件
        * `find . -newer a.txt` : 查找当前目录下(递归子目录)的所有修改时间在a.txt之后(所以文件更新)的文件和目录
    * 按权限和所有者查找
        * `find . -user sky` : 查找所有user为sky的文件和目录（递归子目录）
        * `find . -group  sky` : 查找所有group 为sky的文件和目录（递归子目录）
        * `find . -perm -ug=x` : 查找所有user和group权限为x的文件和目录（递归子目录）
        * `find . -perm -u=rwx` : 查找所有user权限为rwx的文件和目录（递归子目录）
        * `find . -perm 777` : 查找所有权限为777的文件和目录（递归子目录）
    * 按文件大小查找
        * `find . -size -100c` : 查找所有 文件大小小于100字节 （递归子目录）
        * `find . -size +100k` : 查找所有 文件大小大于100k （递归子目录）
        * `find . -size 0` : 查找所有 文件大小为0 （递归子目录）
        * `find . -size -100c` : 查找所有 文件大小小于100字节 （递归子目录）
    * 查找空文件和空目录
        * `find . -empty` : 查找所有 文件大小为0的文件和空文件夹（递归子目录）
        * `find . -empty -type f` : 查找所有 文件大小为0的文件（递归子目录）
        * `find . -empty -type d` : 查找所有 空目录（递归子目录）
    * 控制查找的行为
        * `find . -maxdepth 3 -name "*.txt"` : 查找当前目录下(递归子目录)的所有名为*.txt的文件，目录深度不超过3层
        * `find . -mindepth 3 -name "*.txt"` : 查找当前目录下(递归子目录)的所有名为*.txt的文件，目录深度不低于3层
    * find和其他命令的组合
        * `find . -name "*.jar" -ls` : 查找当前目录下(递归子目录)的所有*.jar文件并使用ls -l列出详细信息
        

* add user to sudoer
    ```
        $ su -
        # visudo    
        # username ALL=(ALL)   ALL
            (在root  ALL=(ALL)   ALL后面添加上面一行)
    
    ```
* CentOS Install pip
    * Way 1:
        * Step1: Add the EPEL Repository
            `rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm`
            * *Pip* is part of Extra Packages for Enterprise Linux (EPEL).
            * which is a community repository of non-standard packages for the RHEL distribution.
        * Step2: install pip
            ```
                yum -y update
                yum -y install python-pip
            
            ```
    * Way 2:
        * We can also use curl and python to download and install Pip.
        ```
            curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
            python get-pip.py
        
        ```
    * Verify the Installation
        ```
            pip -V
            pip --help
            
        ```
    * `pip` 使用国内源
        * 使用`-i`参数指定源
            `sudo pip install --trusted-host pypi.douban.com -i http://pypi.douban.com/simple/ flask`
        * 修改配置文件，不用每次输入大段文本
            ```
                sudo mkdir ~/.pip
                vi ~/.pip/pip.conf
                
                [global]
                index-url = http://pypi.douban.com/simple
                index-url = http://mirrors.aliyun.com/pypi/simple/
                
                [install]
                trusted-host=mirrors.aliyun.com
                trusted-host=pypi.douban.com
            
            ```
    
 
* look log
    ```
        # tail -f /var/log/messages
        # tail -f /var/log/secure
    ```
* Linux bind port
    * `<1024` : for *root*
    
* *touch*
    `$ touch newfile_name` , create a empty file
  
* Linux *history* command:
    * 
        ```
            $ history 10 : list 10 history cmds
            
            $ !10 : run No.10 history cmd
            $ ! !    : run the last cmd
            $ !rpm     : run the last cmd begin with 'rpm'
            
            $ history |more
            $ history -c : clear shell history
        ```
        
* *unset* : 删除变量或函数
    ```
        $ dog=Doggie
        $ echo $dog
        $ unset dog
        $ echo $dog
    
    ```
    
* *useradd* : 创建用户同时创建用户主目录
    `# useradd -m user_name`
    
* List All Linux Commands, 显示当前用户所有可用命令
    * *compgen* 
    * list all the commands available to you
        `$ compgen -c`
    * To list all the bash shell aliases available to you,
        `$ compgen -a`
    * Other
        `$ compgen -b`  , bash built-ins
        `$ compgen -k`  , bash keywords
        `$ compgen -A function`
        
        
    
# CentOS Linux下VNC Server远程桌面配置详解

* Step(CentOS 6.5)
    * `# yum groupinstall "X Window System"`
    * `# yum install tigervnc-server tigervnc`
    

# iptables
* To check the status of your firewall and all rules:
    `$ sudo iptables -L -n`
    `$ sudo iptables -L -v -n --line-numbers`
* to allow the Flask using iptables:
    `iptables -I INPUT -p tcp --dport 5000 -j ACCEPT`
* [IPTables](https://wiki.centos.org/zh/HowTos/Network/IPTables)
* network statistics
    * `netstat -tupln | grep ':5000'`
    
# yum

* Ref : [yum command: Update / Install Packages Under Redhat Enterprise / CentOS Linux Version 5.x](http://www.cyberciti.biz/faq/rhel-centos-fedora-linux-yum-command-howto/)

* List all installed packages
    * `# rpm -qa`
    * `# rpm -qa | grep httpd*`
    * `# yum list installed`
    * `# yum list installed httpd`
* Check for and update specified packages
    * `# yum update httpd`
* Search for packages by name
    * `# yum list httpd`
    * `# yum list perl*`
* Install the specified packages [ RPM(s) ]
    * `# yum install httpd`
* Remove / Uninstall the specified packages [ RPM(s) ]
    * `# yum remove httpd`
    ```
        # yum list update       =Display list of updated software
        # yum update            =Patch up system by applying all updates
        # yum list all
        
        # yum grouplist
        # yum groupinstall "Development Tools"  = Install all ‘Development Tools’ group packages
        # yum groupupdate "Development Tools"
        # yum groupremove "Development Tools"   
        
    ```

    
# Q & A

* Q: [How do I set a user environment variable? (permanently, not session)](http://unix.stackexchange.com/questions/21598/how-do-i-set-a-user-environment-variable-permanently-not-session) 
    *  如，要添加到 `/opt/miniconda2/bin` 到系统变量中
            `# vi /etc/profile`
            `export PATH=$PATH:/opt/miniconda2/bin`
            `# source /etc/profile`
            `# echo $PATH` ,确认conda已经添加进去
    
* ‘Ifconfig’ Command Not Found In CentOS 7 Minimal Installation – A Quick Tip To Fix It
    * In CentOS-7, there are some alternate command
        `ip add`
    
    * Here is the installation of `ifconfig`:
        * set network ONBOOT 
            ```
                # vi /etc/sysconfig/network-scripts/ifcfg-eth0
                    ONBOOT=yes
                # service network restart
            ```
        * install net-tools
            ```
                # yum install net-tools
                # ifconfig
            ```
    
* How do I install *semanage* command under RedHat Enterprise Linux?
    * *semanage* for SELinux manage
    ```
        # yum provides semanage
        or 
        # yum whatprovides semanage
        
            Loaded plugins: fastestmirror
            Loading mirror speeds from cached hostfile
             * base: mirrors.zju.edu.cn
             * extras: mirrors.zju.edu.cn
             * updates: mirrors.zju.edu.cn
            policycoreutils-python-2.2.5-20.el7.x86_64 : SELinux policy core python utilities
            Repo        : base
            Matched from:
            Filename    : /usr/sbin/semanage    
        
        # yum -y install policycoreutils-python
        # semanage
        $ man semanage
    ```
    * [RHEL 6: semanage SELinux Command Not Found](http://www.cyberciti.biz/faq/redhat-install-semanage-selinux-command-rpm/)
        
* `sshd[13798]: error: Bind to port 1234 on :: failed: Permission denied.`
    * This is SELinux in action. 
        * So we need to modify the SELinux configuration to allow sshd to listen on our new port 1234. 
    1. To display current port contexts, enter:
        ```
            # semanage port -l |grep ssh
            ssh_port_t                     tcp      22
        
        ```
    2. To add port 1255 to port contexts, enter:
        ```
            # semanage port -a -t ssh_port_t -p tcp 1255
        ```
    3. verify new settings
        ```
            # semanage port -l |grep ssh
            ssh_port_t                     tcp      1255,22
        ```
    4. reload or restart the OpenSSH server
        `# service sshd restart`
        
    * ref: [Change OpenSSH Port To 1255 ( SELinux Config )](http://www.cyberciti.biz/faq/centos-redhat-enterprise-linux6-change-sshd-port-number/)

        
    5. But I still not access ssh even the port is been listened.
    
* How To Install *EPEL* *Repo* on a CentOS and RHEL 7.x
    * Extra Packages for Enterprise Linux (or *EPEL* ) is a Fedora Special Interest Group 
        * that creates, maintains, and manages a high quality set of additional packages 
        * for Enterprise Linux, including, but not limited to, Red Hat Enterprise Linux (RHEL),CentOS and Scientific Linux (SL). 
    * Install Extra Packages for Enterprise Linux ( *EPEL* ) repository configuration (recommended)
        1. `$ sudo yum install epel-release `
        2. `$ sudo yum repolist` , Refresh repo
        
* Install *pip* Client To Install Python Packages 
    * Install *EPEL* repo
    * Install python-pip package
        `$ sudo yum -y install python-pip`
        
        
* `curl` text surf
    * `$ curl -I 127.0.0.1:5000` , return url header
    * `$ curl 127.0.0.1:5000` , return url web page
    
    
* Flask: `app.run(host='0.0.0.0', debug=True) `
    * when run the flask app, local host access work,  but in the remote host can't access
    * The reason is *firewall*
        `$ sudo systemctl stop firewalld`
        
        ```
            [修改机器名]
            # vi /etc/hostname

            [关SELinux]
            # vi /etc/selinux/config
            设置SELINUX=disabled

            [关防火墙]

            # systemctl stop firewalld
            # systemctl disable firewalld
            # systemctl status firewalld 看状态
        ```
* `supervisord -c supervisor.conf ` , can't work
    * Only used: `supervisorctl -c supervisor.conf start [all]|[appname]`
    * Other command:
        ```
            supervisord -c supervisor.conf                             通过配置文件启动supervisor
            supervisorctl -c supervisor.conf status                    察看supervisor的状态
            supervisorctl -c supervisor.conf reload                    重新载入 配置文件
            supervisorctl -c supervisor.conf start [all]|[appname]     启动指定/所有 supervisor管理的程序进程
            supervisorctl -c supervisor.conf stop [all]|[appname]      关闭指定/所有 supervisor管理的程序进程
        
        ```
   
* Install *nginx* on CentOS-7
    1. Install EPEL
        `$ sudo yum install epel-release`
    2. Install nginx
        `$ sudo yum install nginx`
        
    3. Starting Nginx
        `$ sudo systemctl start nginx`
    
    4. set Nginx as a service
        `$ sudo systemctl enable nginx.service`
        
* *lsof* : lists openfiles
    * 在Unix中，一切都是文件，包括网络套接口。
    
    * 显示与指定端口相关的网络信息，查阻止端口
        `# lsof -i :22`
        
    * 显示所有连接
        `# lsof -i`
        
* *Systemctl* Usage
    以docker服务为例
        ```
        chkconfig&service用法

            #自启动
            chkconfig docker on
            #关闭自启动
            chkconfig docker off
            #显示已启动服务
            chkconfig --list
            #检查服务状态
            service docker status
            #启动服务
            service docker start
            #暂停服务
            service docker stop
            #重启服务
            service docker restart
            
        systemctl用法

            #自启动
            systemctl enable docker.service
            #关闭自启动
            systemctl disable docker.service
            #显示已启动服务
            systemctl list-units --type=service
             
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
# Question and Aswer

* how to list all users
    * `$ cat /etc/passwd`
        * use pages:
            * `$ more /etc/passwd`
            * `$ less /etc/passwd`
    * whick users that can actually login anc execute
        * `$ cat /etc/passwd | grep -v nologin`
   
* Recommended console ftp clients : *curlftpfs*
    * ref : [](http://askubuntu.com/a/12824)
    * install *curlftpfs*
        `$ sudo apt-get install curlftpfs`
    * add yourself to group *fuse* :
        `$ sudo usermod -aG fuse <username>`
    * Log out, and log back in again, for changes to take effect
    * Make a directory for a mount point
        `$ mkdir ~/ftp`
    * mount the ftp server as a local filesystem
        `$ curlftpfs ftp.server.com ~/ftp -o user=<ftp_username>`
        * Enter the password when prompted
        
    * other : unmount it do:
        `$ fusermount -u ~/ftp`
        
    
        
    * Error
        * `usermod: group 'fuse' does not exist`
            * the error appear, when run :
                `$ curlftpfs ftp.server.com ~/ftp -o user=<ftp_username>`
            * when run the command with *root* :
                `# curlftpfs ftp.server.com ~/ftp -o user=<ftp_username>`
                * appear another error:
                    `fuse: failed to open /dev/fuse: Operation not permitted`
                * the *root* not permite to do this.
                
        * So here ,we know it's the permission problem
            * check the 'fuse' directory
                ```
                    $ ll /dev/fuse
                    c---------. 1 root root ... /dev/fuse
                
                ```               
            * if 
    
* account user password passwd
    * */etc/passwd* : user account
    * */etc/shadow* : password information and optional account aging information
    * */etc/group* : the groups
    * */etc/default/useradd* : this file contains a value for the default group, if none is pecified by the *useradd* command.
    * */etc/login.defs* : this file defines the site-specific configuration for the shadow password suite stored in */etc/shadow* file.
    
    * [Howto: Linux Add User to Group](http://www.cyberciti.biz/faq/howto-linux-add-user-to-group)
    * Add user
        * 
    
* module
    * confirm *fuse* module is loaded
        `lsmod | grep fuse`   , 
    * load the *fuse* module 
        `modprobe fuse`   , 
    * make sure the *fuse* module is loaded upon a reboot.
        `echo "modprobe fuse" >> /etc/rc.local`   
    
    
* copy directory
    `$ cp -r /tmp/a /root/a`
    
* chmod
    * To change all the directories to 755 (-rwxr-xr-x):
        `find /opt/lampp/htdocs -type d -exec chmod 755 {} \;`
    * To change all the files to 644 (-rw-r--r--):
        `find /opt/lampp/htdocs -type f -exec chmod 644 {} \;`
    * [change all the directories to 755](http://stackoverflow.com/questions/3740152/how-to-set-chmod-for-a-folder-and-all-of-its-subfolders-and-files-in-linux-ubunt?rq=1)
    
* `-bash: locate: command not found`
    * `$ sudo yum -y install mlocate`
    * `$ sudo updatedb`
    
        
# Links

-[] [Centos7系统配置上的变化（一）](http://www.cnblogs.com/panblack/p/Centos7-WhatsNew-01.html)


# Debug 

* `$ pgrep -fl supervisor`
    `3786 supervisord`
* `kill 3786`

* `tail -f /var/log/nginx/error.log`

* `ps aux | grep nginx`

## About SELinux

* check SELinux allowed to bind to the whic ports
    ```
        $ sudo semange port -l | grep http_port_t
        http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
    
    ```
* Add port you want to bind out to the list
    `$ sudo semanage port -a -t http_port_t -p tcp 8090`
    
* 查看当前文件夹内包含 *listen* 的所有文件
    `$ grep -R listen *`
    
    flask.conf:     listen  [::]:80 ipv6only=on default_server;

    
* There are no `/usr/local/bin` `no suc file or `


# Question & Answer

* 使用`apt-get install package-name`提示`Unable to locate package package-name`
    * `apt-get update`
    
* yum使用国内源，163源
    1. 首先备份/etc/yum.repos.d/CentOS-Base.repo
        * `mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
`
    2. 下载对应版本repo文件, 放入/etc/yum.repos.d/(操作前请做好相应备份)
        * [CentOS-7](http://mirrors.163.com/.help/CentOS7-Base-163.repo)
        * [CentOS 6](http://mirrors.163.com/.help/CentOS6-Base-163.repo)
    3. 生成缓存
        * `yum clean all`
        * `yum makcache`
        
* 使用`locate` 定位文件
    From: [FindingFiles](https://help.ubuntu.com/community/FindingFiles#locate)
    ```
        sudo apt-get install mlocate
        updatedb
        
    ```
    * 也可制订一个定时任务
        * 每天晚上在4:02am，对文件进行索引，但不包括`/mnt/data`和`/mnt/files`这两个文件夹。
        ```
            sudo crontab -e
            02 4 * * * /usr/bin/updatedb -e /mnt/data,/mnt/files
        ```
        
* 安装 `add-apt-repository`
    

   `apt-get install python-software-properties`
    