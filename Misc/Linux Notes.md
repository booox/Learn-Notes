


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
    
## other

* tree
    * Install: `sudo yum install tree`
    * `tree -d`
    * `tree -L n`
    * `tree -f`
    
    
* chmod 改变权限有两种方法
    * 符号类型改变文件权限:
        chmod (ugoa) (+-=) (rwx) (file|path)
        
* `$ echo $PATH`

* `$ env | grep LANG` check environment

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
    * A: 
    
* ‘Ifconfig’ Command Not Found In CentOS 7 Minimal Installation – A Quick Tip To Fix It
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
    
    
    
# Links

-[] [Centos7系统配置上的变化（一）](http://www.cnblogs.com/panblack/p/Centos7-WhatsNew-01.html)