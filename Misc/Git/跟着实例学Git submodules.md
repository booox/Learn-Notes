# 如何使用Git的submodule

## 准备工作

* 首先你要有一个 [Github](https://github.com) 的账号
* 接着你可以创建一个仓库 *repository* ，或者直接 *fork* 我简单的示例项目
    * 示例项目 : [https://github.com/booox/example.git](https://github.com/booox/example.git)
    
* 创建工作目录
    ```
        $ mkdir git-study
        /home/user/git-study        
    ```
    
* 将示例克隆下来
    `$ git clone https://github.com/booox/example.git git-submodule `
    * 这样就将示例项目克隆到 *git-submodule* 文件夹当中了
    ```
        $ cd git-submodule
        $ pwd
        $ /home/user/git-study/git-submodule    
    ```
    
## 添加一个submodule

* 示例项目是可以打印出 “Hello World” 的 *php* 程序。我们需要增强它的能力，这里我们准备使用 PHP *Doctrine* 。
    * *Doctrine2* 在 [doctrin2 in github](https://github.com/doctrine/doctrine2)
    
* 可以使用 `git submodule add` 来添加一个子模块
    `$ git submodule add (repository) (directory)`
    