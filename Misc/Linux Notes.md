


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


# CentOS Linux下VNC Server远程桌面配置详解

* Step(CentOS 6.5)
    * `# yum groupinstall "X Window System"`
    * `# yum install tigervnc-server tigervnc`
    