# 如何使用Git的submodule

* [How to use Git submodules](http://blog.joncairns.com/2011/10/how-to-use-git-submodules/)
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
        /home/user/git-study/git-submodule    
    ```
    
## 添加一个submodule

### 添加子模块
* 示例项目是可以打印出 “Hello World” 的 *php* 程序。
    * 我们需要增强它的能力，假设我们这里需要一个程序叫 *Flask* (只是文件较小方便实验) 。
    * *Flask* 在 [nginx-gunicorn-flask](https://github.com/booox/nginx-gunicorn-flask.git)
    
* 可以使用 `git submodule add` 来添加一个子模块
    `$ git submodule add (repository) (directory)`
    * 如添加 *Flask* 作为一个子模块，并放到名字为 *flask* 的目录中
        `$ git submodule add https://github.com/booox/nginx-gunicorn-flask.git flask`
        
    * 执行成功之后，就会将 *flask* 注册为一个子模块
    * 并将文件克隆到本地的 *flask* 文件夹里。
        
* 查看 *submodule* 状态
    ```
        $ git submodule status
        -ce3d6f12a64f0bf7719aa11293a476e1358ba477 flask
    ```
    * 这里可以告诉我们子模块已经被注册
    
* 查看父仓库有哪些变化
    `$ git status`
    * 添加了两个文件：
        * *.gitmodules* : 存储与子模块相关的信息
        * *flask* : 子模块
    * 当你在父仓库中时 *Git* 并不跟踪子模块中的文件，所以看起来子模块就是一个单独的文件。
    
  
### 提交改变
    `$ git commit -m 'Added Flask submodule'`
    
### 推送到Github
    `$ git push`
    * 这时可以在Github中看到一个指向 *Flask* 的链接
    

## 克隆一个包含子模块的仓库

* 让我们将刚刚创建好的仓库克隆到另一个不同的目录。移到我们当前目录的上一级。
    `$ pwd`
    `/home/user/git-study`
    `$ git clone ****/example.git submodule-clone-example `
    
    * 如果你移动到新克隆过来的仓库中的 *flask* 目录下，你会发现它是空的。
        ```
            $ cd submodule-clone-example
            $ pwd
            /home/user/git-study/submodule-clone-example
            $ ll flask
            Total 0
        ```
    * 如果此时你查看 *submodule* 状态：
        ```
            $ git submodule status
            -ce3d6f12a64f0bf7719aa11293a476e1358ba477 flask
        ```
        * 前面的 *-* 表明这个子模块还没有被下载。
    
    * 怎么会这样？难道 *git* 把它丢弃了，没把它克隆过来？
    
* 不是。默认情况下， `git clone` 不会把子模块和父仓库一直拉下来。
* 要把 *Flask* 子模块也拉下来，你需要以下两步：
    * 注册子模块，就是在 *.git/config* 上写入子模块相关信息：
        `$ cd submodule-clone-example`
        `$ cat .git/config`
        `$ git submodule init`
        `$ cat .git/config`
        * 可以对比两次 *config* 输出的不同
        
    * 将代码（文件）拉下来
        `$ git submodule update`
        * 到这里，我们才将子模块原封不动地拉下来了。
    * 这时再查 *submodule* 状态
        ```
            $ git submodule status
            ce3d6f12a64f0bf7719aa11293a476e1358ba477 flask
        ```
        * 前面的 *-* 没了。
        
## 更新子模块

* *Git* 的子模块其实就是在其它仓库里简单的 *Git* 仓库，没有什么神奇的。
* 因此，只要你在子模块的目录下，所有的 *Git* 动作像 *push* , *pull* , *reset* ， *log* ， *status*  等等都可以象往常一样照常使用。
* 如果你想确保子模块与远程仓库保持同步更新，只要在子模块的目录下运行 `git pull` 就可以了。
    ```
        $ cd flask
        $ git pull    
    ```
    
* 如果有错误提示你没有在任何分支上，运行 *checkout* 来修复它。
    `$ git checkout master`
    
* 如果当你在执行 *pull* 操作时，你的子模块有了一些更新，那么你的父仓库就会告诉你有一些改变需要 *commit* 。
    * 子模块指向一个特定的 *commit* ，如果这个 *commit* 更改了，那么父仓库就会注册这个更改。
    * 如果你的子模块需要切换到某一特定的 *commit* ，你可以通过 `git reset` 来实现。
        `$ git reset --hard (commit hash)`
        * 例如：如果想让 *Flask* 版本为最新的 *tag* (目前为 *2.1.2* )
            ```
                $ cd flask
                $ git reset --hard 144d0de
                HEAD is now at 144d0de Release 2.1.2            
            ```
            * 接着你就可以返回父目录，并提交它 ( *commit* ) 。
            ```
                $ cd ..
                $ git commit -am 'Set flask version to 2.1.2'
            ```
            
    * 这时如果 *push* 到远程仓库，那么子模块也就会和那个特定的 *commit* 联系起来了。

## 包含子模块的子模块

* 子模块的一个重要功能就是他们能够包含子模块。
    * 例如，我们前面用过的 *Flask* 仓库就包含几个子模块，包括 *flask-common* 和 *dbal* 。
    
* 回到前面的 *example* 仓库，目前， *Flask* 被注册为子模块，但它的子模块没有一个被拉下来( *pull* )。
    * 在 *flask* 目录中，查看子模块的状态
        ```
            jcairns$ git submodule status
            -3762cec59aaecf1e55ed92b2b0b3e7f2d602d09a lib/vendor/Symfony/Component/Console
            -c3e1d03effe339de6940f69a4d0278ea34665702 lib/vendor/Symfony/Component/Yaml
            -ef431a14852d7e8f2d0ea789487509ab266e5ce2 lib/vendor/flask-common
            -f91395b6f469b5076f52fefd64574c443b076485 lib/vendor/flask-dbal
        
        ``` 
        
        * 可以看到在 *flask* 中有四个子模块
        * 而在输出的每一行开头的 *-* 表明这个子模块还没有被下载。
        * 我们可以运行 `git init` 再接 `git update`来将所有的仓库（包括子模块？）克隆到正确的地方。

* 但如果要将我们的仓库 ( 例如这里的 *example* ) 克隆到其它的机器，我们是否需要在每一个子模块里执行 *init* 和 *update* 命令？
    * 答案是否定的。而我们也是幸运的，我们只需要在运行 `git clone` 时添加一个 *--recursive* 选项就可以了。
        `$ git clone --recursive (repository)`
        
## 移除子模块
    
* 要移除了模块，你得修改 *.gitmodules* 文件（在你项目的根目录下，不是子模块文件夹内）
        
* 打开 *gitmodules* 文件，大概是这样子的：
    ```
        [submodule "flask"]
        path = flask
        url = git://github.com/flask/flask2.git
    ```
    * 如果有多个子模块，就会有多个类似的节点。
    
* 要移除子模块，只要将对应的这三行删除就搞定了。
    * 如果只有一个子模块，你就可以直接税将 *gitmodules* 文件删除。
    
* 当你下一次 *commit* 时，你就会要求 *commit* 你的改变到 *.gitconfig* 。
    * 这样做之后，就会从远程仓库将子模块移除掉，如果再从远程仓库克隆，就不会再看到子模块了。
    
* 但是，现在子模块仍然呆在你的本地仓库里。如果你运行 `git submodule status` 你就会得到一个警告：
    ```
        $ git submodule status
        No submodule mapping found in .gitmodules for path 'flask'
    ```
    
* 这因为子模块除了被 *.gitmodules* 文件索引之外，还被 *.git/config* 文件记录着。
    ```
        [core]
            repositoryformatversion = 0
            filemode = true
           bare = false
           logallrefupdates = true
        [remote "origin"]
            fetch = +refs/heads/*:refs/remotes/origin/*
            url = git@github.com:joonty/example.git
        [branch "master"]
            remote = origin
            merge = refs/heads/master
        [submodule "flask"]
            url = git://github.com/flask/flask2.git
    ```
    * 在文件的末尾我们看到与子模块相关的信息。
    * 将最后两行删除，就将子模块从本地仓库移除了。（你可能需要 *sudo* ，即管理员权限。）

* 最后，我们还需要将子模块从 *git-cache* 中移除。
    `$ git rm --cached <path/to/submodule>`
    `$ git rm --cached flask`
    
    * 注意：在子模块目录名称的后面没有 */* 。
    * 到这里，我们才将子模块彻底移除了。
    * 别忘记 *commit* 和 *push* 到远程仓库中。 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    