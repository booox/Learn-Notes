

# Gitbook 简介

## GitBook Links

* [GitBook Github] (https://github.com/GitbookIO/gitbook)
* [GitBook Official Site](http://www.gitbook.io/)

## Gitbook说明

* GitBook 是一个现代发行工具链，它使写作及合作变得非常容易。
* GitBook 是一个命令行工具（也是 Node.js 库）
* 让你能够使用 GitHub/Git 和 Markdown 构建出美丽的编程书籍，可以包含互动的练习。
* GitBook 支持使用多种语言构建书籍。每种语言都应该是按照正常 GitBook 格式的子目录，
    * 另外要在版本库根目录下的 LANGS.md 文件。
* GitBook 可以方便的输出多种文档格式
   * Ref: [GitBook：使用Git+Markdown快速制作电子书](http://www.csdn.net/article/2014-04-09/2819217-gitbook-using-git-markdown-book)
    * 静态网站： GitBook默认输出该种格式，生成的静态站点可直接托管搭载Github Pages服务上
    * PDF: 需要安装gitbook-pdf依赖；
    * eBook：需要安装ebook-convert；
    * 单HTML网页：支持将内容输出为单页的HTML，不过一般用在将电子书格式转换为PDF或eBook的中间过程；
    * JSON：一般用于电子书的调试或元数据提取。

### Gitbook 优点

* Simple to update
* Version Control
* Markdown
* GitHub
* Our Analytics
* Editor
* Personalize branding
* Collaboration


# 安装及测试

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
    
## 安装gitbook及测试
    `npm install -g gitbook`
    `npm install -g gitbook-cli` (安装gitbook命令行)
    
* 测试安装：
    `gitbook -V`
    `gitbook --version`

    
# GitBook 使用

* GitBook 最重要有两个文件，指明目录结构
    * SUMMARY

## GitBook 命令集

* `$ gitbook init` : 将当前目录初始化为gitbook目录
* `$ gitbook serve` : 本地预览和监听（根据现有文档生成电子书的一个可以在本地浏览的在线网站）
* `$ gitbook --help` : 
* `$ gitbook serve ./The_book_Directory` : 可在浏览器中查看该书
* `$ gitbook versions:available` : 查看所有可用版本
* `$ gitbook versions:install version_number` : 安装某版本
* `$ gitbook versions:uninstall version_number` : 卸载某版本

## 创建一本书

1. 初始化目录
    `$ gitbook init`
2. 编辑 *SUMMARY.md* :
    `$ vi SUMMARY.md`
3. 根据 *SUMMARY.md* 目录结构生成对应的目录树
    `$ gitbook init`
4. 本地生成电子书
    `$ gitbook serve`
    
5. 封面 `cover.jpg`
    * 推荐尺寸： 1800*2360
    
    
## 使用插件

* 搜索 GitBook Plugins
    * [npmjs](https://www.npmjs.com/)