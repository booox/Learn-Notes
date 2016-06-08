


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
    * `chmod u+x somefile` : grantly only the owner of that file execution permissions
    * `chmod +x somefile` is the same as `chmod a+x somefile`

* chown �ı��ļ�ӵ���ߺ�Ⱥ��
    * �ı��ļ�ӵ����Ϊmail�û���Ⱥ��Ϊmail��
        `$ sudo chown mail:mail filename`
    * �ı�ָ��Ŀ¼����Ŀ¼�����ļ�
        `$ sudo chown -R mail:mail foldername/`
    
* �޸�ϵͳ���� 
    `$ echo $PATH`

    * `$ env | grep LANG` check environment
    * �޸�ϵͳ���� Change $PATH
        `# vi /etc/profile`
        `export PATH=$PATH:/opt/miniconda2/bin`
        `# source /etc/profile`
        `# echo $PATH` ,ȷ��conda�Ѿ���ӽ�ȥ


* find����
    * From: [LINUX �²���ָ���ļ�](http://www.centrue.me/2011/09/01/linux-find/)
    * �� `find` ��`-exec`�������ʹ��ʱ��
        * ���� `{}`������ `find`���ҵ����ļ���
        * ���� `\;` ����ʾ�������.
            * `find . -type f -exec ls -l {} \;` : �ڵ�ǰĿ¼�£��ݹ���Ŀ¼�����������ļ�����`ls`����
            * `find . -user root -exec sudo chown test:test {} \;` : 
                * �ڵ�ǰĿ¼�£��ݹ���Ŀ¼�����������û�Ϊ`root`���ļ���Ŀ¼��
                * ���޸������û����û���Ϊ`test`
    * �����Ʋ���
        * `find . -name readme.txt` : ����  ������Ϊreadme.txt���ļ� ���ݹ���Ŀ¼��
        * `find . -name \*.txt` : �������� ������.txt��β���ļ����ݹ���Ŀ¼��
        * `find . -name "*.txt"` : ͬ��
        * `find . -iname \*.txt` : �������� ������.txt��β���ļ����Ҳ����ִ�Сд���ݹ���Ŀ¼��
    * �����Ͳ���
        * `find . -type d` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)������Ŀ¼
        * `find . -type f` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)�������ļ�
        * `find . -type l` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)�����з�������
    * ��ʱ�����
        * `find` ����������ѡ�����ڰ�ʱ����ң���λΪ **Сʱ** :
            * `mtime` : �ϴ��޸�ʱ��
            * `atime` : �ϴζ�ȡ�����ʱ��
            * `ctime` : �ϴ��ļ�״̬�仯��ʱ��
        * `find . -mtime -1` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)������1Сʱ���޸ĵ��ļ���Ŀ¼
        * `find . -mtime +1` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)�����г���1Сʱ���޸ĵ��ļ���Ŀ¼
        * `find . -mtime 1` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)������ǡ����1Сʱ���޸ĵ��ļ���Ŀ¼
        * �Է���Ϊ��λ
            * `find . -mmin -10` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)������10�������޸ĵ��ļ���Ŀ¼ 
            * `find . -mmin +20` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)������20������1Сʱ���޸ĵ��ļ���Ŀ¼
        
    * ���ض����ļ��Ƚ�
        * ��������ص�ѡ�
            * `-newer ` : ָ����������޸ĵ��ļ�
            * `-anewer` : ָ�������ȡ�����ļ�
            * `-cnewer` : ָ״̬��������仯���ļ�
        * `find . -newer a.txt` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)�������޸�ʱ����a.txt֮��(�����ļ�����)���ļ���Ŀ¼
    * ��Ȩ�޺������߲���
        * `find . -user sky` : ��������userΪsky���ļ���Ŀ¼���ݹ���Ŀ¼��
        * `find . -group  sky` : ��������group Ϊsky���ļ���Ŀ¼���ݹ���Ŀ¼��
        * `find . -perm -ug=x` : ��������user��groupȨ��Ϊx���ļ���Ŀ¼���ݹ���Ŀ¼��
        * `find . -perm -u=rwx` : ��������userȨ��Ϊrwx���ļ���Ŀ¼���ݹ���Ŀ¼��
        * `find . -perm 777` : ��������Ȩ��Ϊ777���ļ���Ŀ¼���ݹ���Ŀ¼��
    * ���ļ���С����
        * `find . -size -100c` : �������� �ļ���СС��100�ֽ� ���ݹ���Ŀ¼��
        * `find . -size +100k` : �������� �ļ���С����100k ���ݹ���Ŀ¼��
        * `find . -size 0` : �������� �ļ���СΪ0 ���ݹ���Ŀ¼��
        * `find . -size -100c` : �������� �ļ���СС��100�ֽ� ���ݹ���Ŀ¼��
    * ���ҿ��ļ��Ϳ�Ŀ¼
        * `find . -empty` : �������� �ļ���СΪ0���ļ��Ϳ��ļ��У��ݹ���Ŀ¼��
        * `find . -empty -type f` : �������� �ļ���СΪ0���ļ����ݹ���Ŀ¼��
        * `find . -empty -type d` : �������� ��Ŀ¼���ݹ���Ŀ¼��
    * ���Ʋ��ҵ���Ϊ
        * `find . -maxdepth 3 -name "*.txt"` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)��������Ϊ*.txt���ļ���Ŀ¼��Ȳ�����3��
        * `find . -mindepth 3 -name "*.txt"` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)��������Ϊ*.txt���ļ���Ŀ¼��Ȳ�����3��
    * find��������������
        * `find . -name "*.jar" -ls` : ���ҵ�ǰĿ¼��(�ݹ���Ŀ¼)������*.jar�ļ���ʹ��ls -l�г���ϸ��Ϣ
        

* add user to sudoer
    ```
        $ su -
        # visudo    
        # username ALL=(ALL)   ALL
            (��root  ALL=(ALL)   ALL�����������һ��)
    
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
    * `pip` ʹ�ù���Դ
        * ʹ��`-i`����ָ��Դ
            `sudo pip install --trusted-host pypi.douban.com -i http://pypi.douban.com/simple/ flask`
        * �޸������ļ�������ÿ���������ı�
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
        
* *unset* : ɾ����������
    ```
        $ dog=Doggie
        $ echo $dog
        $ unset dog
        $ echo $dog
    
    ```
    
* *useradd* : �����û�ͬʱ�����û���Ŀ¼
    `# useradd -m user_name`
    
* List All Linux Commands, ��ʾ��ǰ�û����п�������
    * *compgen* 
    * list all the commands available to you
        `$ compgen -c`
    * To list all the bash shell aliases available to you,
        `$ compgen -a`
    * Other
        `$ compgen -b`  , bash built-ins
        `$ compgen -k`  , bash keywords
        `$ compgen -A function`
        
        
    
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
    *  �磬Ҫ��ӵ� `/opt/miniconda2/bin` ��ϵͳ������
            `# vi /etc/profile`
            `export PATH=$PATH:/opt/miniconda2/bin`
            `# source /etc/profile`
            `# echo $PATH` ,ȷ��conda�Ѿ���ӽ�ȥ
    
* ��Ifconfig�� Command Not Found In CentOS 7 Minimal Installation �C A Quick Tip To Fix It
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
            supervisorctl -c supervisor.conf start [all]|[appname]     ����ָ��/���� supervisor����ĳ������
            supervisorctl -c supervisor.conf stop [all]|[appname]      �ر�ָ��/���� supervisor����ĳ������
        
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
    * ��Unix�У�һ�ж����ļ������������׽ӿڡ�
    
    * ��ʾ��ָ���˿���ص�������Ϣ������ֹ�˿�
        `# lsof -i :22`
        
    * ��ʾ��������
        `# lsof -i`
        
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

## About SELinux

* check SELinux allowed to bind to the whic ports
    ```
        $ sudo semange port -l | grep http_port_t
        http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
    
    ```
* Add port you want to bind out to the list
    `$ sudo semanage port -a -t http_port_t -p tcp 8090`
    
* �鿴��ǰ�ļ����ڰ��� *listen* �������ļ�
    `$ grep -R listen *`
    
    flask.conf:     listen  [::]:80 ipv6only=on default_server;

    
* There are no `/usr/local/bin` `no suc file or `


# Question & Answer

* ʹ��`apt-get install package-name`��ʾ`Unable to locate package package-name`
    * `apt-get update`
    
* yumʹ�ù���Դ��163Դ
    1. ���ȱ���/etc/yum.repos.d/CentOS-Base.repo
        * `mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
`
    2. ���ض�Ӧ�汾repo�ļ�, ����/etc/yum.repos.d/(����ǰ��������Ӧ����)
        * [CentOS-7](http://mirrors.163.com/.help/CentOS7-Base-163.repo)
        * [CentOS 6](http://mirrors.163.com/.help/CentOS6-Base-163.repo)
    3. ���ɻ���
        * `yum clean all`
        * `yum makcache`
        
* ʹ��`locate` ��λ�ļ�
    From: [FindingFiles](https://help.ubuntu.com/community/FindingFiles#locate)
    ```
        sudo apt-get install mlocate
        updatedb
        
    ```
    * Ҳ���ƶ�һ����ʱ����
        * ÿ��������4:02am�����ļ�������������������`/mnt/data`��`/mnt/files`�������ļ��С�
        ```
            sudo crontab -e
            02 4 * * * /usr/bin/updatedb -e /mnt/data,/mnt/files
        ```
        
* ��װ `add-apt-repository`
    

   `apt-get install python-software-properties`
    