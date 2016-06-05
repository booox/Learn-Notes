

## 安装 Node.js 和 npm (CentOS 7)
    
* [How To Install Node.js on a CentOS 7 server](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-a-centos-7-server)    
* [npm Documentation](https://docs.npmjs.com/)

* 安装
    `$ sudo yum install nodejs npm`
    如果报错，可能需要安装 *EPEL-repo*
        `$ sudo yum install epel-release`
        
* 测试安装：
    ```
        $ node -v
        v0.10.42
        
        $ npm -v
        1.3.6
    ```
* 更新npm
    ```
        $ sudo npm install npm -g
        
        $ npm -v
        3.9.5
    ```
    
## 使用npm安装软件

* [npm使用教程（未完)](http://www.cnblogs.com/stephenykk/p/4505834.html)

* There are two ways to install npm packages: locally or globally. 
* locally:
    `npm install <package_name>`
    
* globally:
    `npm install -g gitbook`
    
## 安装gitbook
    `npm install -g gitbook`
    `npm install -g gitbook-cli` (安装gitbook命令行)
