


# Linux Commands

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
    