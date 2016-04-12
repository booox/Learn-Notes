


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
    
    * CentOS ͬ������ʱ��
        `# yum -y install ntpdate`
        `# ntpdate asia.pool.ntp.org`
        
    
## other

* tree
    * Install: `sudo yum install tree`
    * `tree -d`
    * `tree -L n`
    * `tree -f`
    
    
* chmod �ı�Ȩ�������ַ���
    * �������͸ı��ļ�Ȩ��:
        chmod (ugoa) (+-=) (rwx) (file|path)
        
* `$ echo $PATH`

* `$ env | grep LANG` check environment

* add user to sudoer
    ```
        $ su -
        # visudo    
        # username ALL=(ALL)   ALL
            (��root  ALL=(ALL)   ALL������������һ��)
    
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
    
# CentOS Linux��VNC ServerԶ�������������

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
        # yum groupinstall "Development Tools"  = Install all ��Development Tools�� group packages
        # yum groupupdate "Development Tools"
        # yum groupremove "Development Tools"   
        
    ```

    
# Q & A

* Q: [How do I set a user environment variable? (permanently, not session)](http://unix.stackexchange.com/questions/21598/how-do-i-set-a-user-environment-variable-permanently-not-session) 
    * A: 
    
* ��Ifconfig�� Command Not Found In CentOS 7 Minimal Installation �C A Quick Tip To Fix It
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
            [�޸Ļ�����]
            # vi /etc/hostname

            [��SELinux]
            # vi /etc/selinux/config
            ����SELINUX=disabled

            [�ط���ǽ]

            # systemctl stop firewalld
            # systemctl disable firewalld
            # systemctl status firewalld ��״̬
        ```
* `supervisord -c supervisor.conf ` , can't work
    * Only used: `supervisorctl -c supervisor.conf start [all]|[appname]`
    * Other command:
        ```
            supervisord -c supervisor.conf                             ͨ�������ļ�����supervisor
            supervisorctl -c supervisor.conf status                    �쿴supervisor��״̬
            supervisorctl -c supervisor.conf reload                    �������� �����ļ�
            supervisorctl -c supervisor.conf start [all]|[appname]     ����ָ��/���� supervisor�����ĳ������
            supervisorctl -c supervisor.conf stop [all]|[appname]      �ر�ָ��/���� supervisor�����ĳ������
        
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
        
* *Systemctl* Usage
    ��docker����Ϊ��
        ```
        chkconfig&service�÷�

            #������
            chkconfig docker on
            #�ر�������
            chkconfig docker off
            #��ʾ����������
            chkconfig --list
            #������״̬
            service docker status
            #��������
            service docker start
            #��ͣ����
            service docker stop
            #��������
            service docker restart
            
        systemctl�÷�

            #������
            systemctl enable docker.service
            #�ر�������
            systemctl disable docker.service
            #��ʾ����������
            systemctl list-units --type=service
             
            #������״̬
            #������ϸ��Ϣ
            systemctl status docker.service
            #����ʾ�Ƿ� Active
            systemctl is-active docker.service
            #��������
            systemctl start docker.service
            #��ͣ����
            systemctl stop docker.service
            #��������
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

-[] [Centos7ϵͳ�����ϵı仯��һ��](http://www.cnblogs.com/panblack/p/Centos7-WhatsNew-01.html)


# Debug 

* `$ pgrep -fl supervisor`
    `3786 supervisord`
* `kill 3786`

* `tail -f /var/log/nginx/error.log`

* `ps aux | grep nginx`