

# Git Getting Started

## Download & Install

### In Windows
    [Git for Windows Setup](http://git-scm.com/download/win)
    
### In Linux
    * CentOS : `yum install git`
    * Ubuntu/Debian : `apt-get install git`

## First-Time Git Setup
* Git comes with a tool called `git config` that lets you get and set configuration variables that control all aspects of how Git looks and operates.
* These variables can be stored in three different places:
    * */etc/gitconfig* : for every user on the system and all their repositories.
        * `$ git config --system path/gitconfig` : specific the file
    * *~/.gitconfig* or *~/.config/git/config* : Specific to your user
        * `$ git config --global `
    * *.git/config* : config file in the Git directory of whatever repository you're currently using:
        * Specific to that single repository.
        
    
            
	
###  Your Identity
	$ git config --global user.name "John Doe"
	$ git config --global user.email johndoe@example.com
	
[Getting Started - First-Time Git Setup](http://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
	
### Keeping your email address private
	
	1. Tell GitHub to keep your email address private
		Settings -> Emails -> Keep my email address private
	2. Tell Git to use your private email address
		- Set your email address 
			`$ git config --global user.email "username@users.noreply.github.com"`
		- Confirm your email address
			`$ git config --global user.email username@users.noreply.github.com`
             
             
### Local to Remote Repository

1. create a repository named *esse* on *github.com* : 
    `https://github.com/username/esse.git`

2. create local directory and init
    ```
        $ mkdir esse
        $ cd esse
        $ git init
    
    ```
3. connect local and remote:
    `$ git remote add origin https://github.com/username/esse.git`
    * requirements
        * the local repo and remote repo both exist
        * the remote repo is empty
        * the first push after the connect remote repo, you need use this command
            `$ git push -u origin master`
	
### Remember the authen?




[Which remote URL should I use?](https://help.github.com/articles/which-remote-url-should-i-use/)
		
		
		
[Caching your GitHub password in Git](https://help.github.com/articles/caching-your-github-password-in-git/)
		
		
#### Linux

1. In terminal:
    `$ git config --global credential.helper cache`
    * This will cache your password for 15 minutes.
    
2. To change the cache timeout:
    `$ git config --global credential.helper 'cache --timeout=3600'`
    * Set the cache to timeout after 1 hour (setting is in seconds)

#### Windows		
		$ git config --global core.editor "'D:\bak\MyDropBox\Dropbox\software\notepad++\notepad++.exe' -multiInst -nosession"
		test
        
        
        - Using credential caching
            Windows:
                1. Download git-credential-winstore [git-credential-winstore](http://gitcredentialstore.codeplex.com/releases/view/106064)
                2. Run it. (Need .net Framework v4.0)
                    + ?? Could not find Git in your PATH.
                        1. go to the git-credential-winstore.exe folder
                        2. cmd run: git-credential-winstore -i "C:\Program Files (x86)\Git\bin\git.exe"
                            (CHANGE TO YOUR GIT DIRECTORY)
                3. Git Bash Run: $ git config --global credential.helper wincred
                4. You will be prompted for credentials the first time you access a repository(NO PROMPT ?)
                
        - Using the .netrc file
            Windows:
                1. Create a text file called _netrc in your home directory (e.g. c:\users\kannonboy\_netrc)(NO SPACES!)
                2. Add credentials to the file for the server or servers
                    machine stash1.mycompany.com
                    login myusername 
                    password mypassword
                    machine stash2.mycompany.com
                    login myotherusername
                    password myotherpassword
                    
        Ref: [Permanently authenticating with Git repositories](https://confluence.atlassian.com/bitbucketserver/permanently-authenticating-with-git-repositories-776639846.html)
                [Is there a way to skip password typing when using https:// github](http://stackoverflow.com/questions/5343068/is-there-a-way-to-skip-password-typing-when-using-https-github)
                
                
### Resume to ask you password everytime
    $ git config --unset credential.helper

	
## Your Editor
	
	On a x64 System:
	$ git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst -nosession"
	$ git config --global core.editor "'F:\bak\dropbox\Dropbox\software\notepad++\notepad++.exe' -multiInst -nosession"
		
## Checking Your Settings

	~~~
	$ git config --list
	user.name=John Doe
	user.email=johndoe@example.com
	color.status=auto
	color.branch=auto
	color.interactive=auto
	color.diff=auto
	...

	~~~

## Getting Help
	three ways to get the help page:
	+	$ git help config
	+	$ git config --help
	+	$ man git config

# Git Basics

## Getting a Git Repository
	There are two main approaches to get a Git project:
	- Takes an existing project or directory and import it into Git.
	- Clones an existing Git repository from another server.
	
### Initializing a Repository in an Existing Directory
	`$ git init`

### Cloning an Existing Repository
```
	$ git clone https://github.com/USER_NAME/REPOS_NAME (new_directory_name)
```
	
## Recording Changes to the Repository
### Recording Changes to the Repository
	The lifecycle of the status of your files.
![lifecycle](lifecycle.png)
	
	four states: 
		+ Untracked
		+ Unmodified
		+ Modified
		+ Staged
	
### Checking the Status of Your Files
	$ git status
	$ git status
	$ echo 'Readme test' >> README
	
### Tracking New Files
	$ git add README
	$ git status
	
### Staging Modified Files
	Let’s change a file that was already tracked. CONTRIBUTING.md
	$ git status
	$ git add CONTRIBUTING.md
	$ git status
	
### Short Status
	$ git status -s
	
### Ignoring Files
	* `$ cat .gitignore`
	`*.[oa]		// ignore any files ending in '.o' or '.a'.`
	`*~			// ignore all files that end with a tilde (~)`
	
    * The rules in *.gitignore* file only apply to untracked files.
    
	example:
    ```
		# no .a files
		*.a

		# but do track lib.a, even though you're ignoring .a files above
		!lib.a

		# only ignore the TODO file in the current directory, not subdir/TODO
		/TODO

		# ignore all files in the build/ directory
		build/

		# ignore doc/notes.txt, but not doc/server/arch.txt
		doc/*.txt

		# ignore all .pdf files in the doc/ directory
		doc/**/*.pdf
	```	
		
### Committing Your Changes
	`$ git commit`
	`$ git commit -m "Some comments"`
	
	
# Push your app to GitHub
## Create a new repository on your GitHub
	1. give it a name(example: git-test)
	2. choose the "public" repo option
	
## 	Create 'origin' pointing to GitHub repository
	The first time you should do this:
		`$ git remote add origin https://github.com/username/repo-name.git`
		
## Send your commits to your GitHub repository 'master' branch
	`$ git push -u origin master`

## Continue do some changes, JUST need this:
	`$ git add .`
	`$ git commit -m 'some commit message'`
	`$ git push origin master`
    
    
    
## Sub modules

### 带有submodule的git仓库的创建
* 正如 git 仓库有两种创建方式一样，带 submodule 的 git 仓库的创建也有两种。
#### 在现在工程中添加一个子工程
    ```
        $ git submodule add **.git local_name
        $ git status
        $ cd local_name
    
    ```

    


    
# Some Links
    - [try Git ](https://try.github.io/levels/1/challenges/1)
    - [Git real](http://gitreal.codeschool.com/levels/1)
    

DIFFERENT WAYS TO ADD

+ `$ git add <list of files>`      Add the list of files
+ `$ git add --all`                   Add all files   
+ `$ git add *.txt`                   Add all txt files in current directory
+ `$ git add docs/*.txt`          Add all txt files in docs directory
+ `$ git add docs/`               Add all files in docs directory
+ `$ git add "*.txt"`             Add all txt files in the whole project


# Links

## Submodule
- [Getting Git Right](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [git 子模块的使用简介](http://easior.is-programmer.com/posts/42541.html)
- [Git Submodule使用完整教程 - 咖啡兔 - HenryYan](http://www.kafeitu.me/git/2012/03/27/git-submodule.html)
- [How to use Git submodules](http://blog.joncairns.com/2011/10/how-to-use-git-submodules/)




# Q & A

* Q:  'Please, commit your changes or stash them before you can merge.'
    * A: You have three options
        * 1. One is to commit the change: 
                `git commit -m "Something"`
        * 2. The second is to stash it. stashing acts as a stack, where you can push changes, and you pop them in reverse order.
                To stash:   `git commit -m "Something"`
                Do the merge, and than pull the stash: `git stash pop`
        * 3. The third options is to discard the local changes:
                `git reset --hard`
    * Links: [You have three options](http://stackoverflow.com/a/15745424)

* git tag

* `git submodule "no submodule mapping found in "`
    * 

* 确认已经添加用户名、邮箱
    * `$ git config user.name` 如果不正确，则要添加用户名
        * `$ git config --global user.name "user-name"`
        * `$ git config --global user.email "user-name@users.noreply.github.com"`


* `403 Forbidden while accessing https://github.com/** fatal: HTTP request failed`
            
    * 为了能够通过 *https* 协议登录 *github* ，要设置你的安全验证为 *git-Remote-URI* :
        `$ git remote set-url origin https://user-name@github.com/user-name/repo-name.git`
        * 或，直接修改 *.git/config* 中的 *remote-origin* 的 *url* 的值如上。
        
    * 这样当你使用 `git push` 时会被提示输入密码。
        * 如果出现错误：`(gnome-ssh-askpass:10890): Gtk-WARNING **: cannot open display:`，执行：
            `$ unset SSH_ASKPASS`
    
    
* 如何删除已经 *push* 到 远端仓库里的文件？如何只删除 github仓库里的文件？如何将已经提交到远端仓库的文件 *ignore* ？
    * The rules in your .gitignore file only apply to untracked files. 
    * Since the files under that directory were already committed in your repository,
        * You have to *unstage* them, *create-a-commit* , and *push* that to *GitHub* : 
            * `$ git rm -r --cached some-directory`
            * `$ git commit -m 'Remove the now ignored directory "some-directory"'`
            * `$ git push origin master`
    
* 如果本地仓库是 *fork* 远程仓库的，要获取主仓库的更新，则用：
    `$ git fetch`
    
* 如何切换分支
    * 切换到主分支：`$ git checkout master`
    * 切换到上一分支：`$ git checkout -`
    * 切换到tag名字为*7a*的分支：`$ git checkout 7a`
* 如何创建新分支
    `$ git checkout -b branch_name`
    or
    `$ git branch branch_name`
* 如何合并分支
    * 将 branch_name 分支的内容合并到当前的分支里
        * 对分支进行自动合并： `$ git merge branch_name`
        * 如果合并出现冲突，则需自行对相关文件进行合并修订，完成后再用`git add`命令完成添加。
        
* 如何保持fork到本地的仓库与源仓库的同步：
    1. 首先添加主仓库地址到remote，名称为upstream
        `git remote add upstream https://github.com/source_username/source.git`
    2. 然后从upstream里fetch更新了的内容
        `git fetch upstream`
    3. 最后将fetch下来的内容merge到master分支里
        `git checkout master`
        `git merge upstream/master`
    
* 如何回退到某一版本
    * 下面这个操作：要将某一个文件回退到某一特定历史版本
    * 具体操作：
        1. 查看提交记录
            `$ git log file_path/file_name`
            * 输出结果类似：
            ```
                commit 3224924a9b84fac2...6104c7933b6
                Merge: 2ced040 c662279
                Date:   Wed May 18 23:24:51 2016 +0800

                    conflict

                commit 2ced040e626e62a...02409b73ee6
                Date:   Wed May 18 22:03:48 2016 +0800

                    add seaborn
            
            ```
            * `commit` : 后面跟的是commit_id
            * 缩进的那一行是使用 `git commit -m 'MESSAGE' 提交时写的那个MESSAGE`
        2. 恢复到指定版本
            * 例如回退到 "add seaborn" 这一版本，使用commit_id的前面几位
                * 6~8位就可以了，不用写全，git 会自动匹配
                `$ git reset 2ced040 file_path/file_name`
            * 此时文件还是在暂存区
        3. 