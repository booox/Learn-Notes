

# Git Getting Started

## Download & Install
[Git for Windows Setup](http://git-scm.com/download/win)
	
## Your Identity
	$ git config --global user.name "John Doe"
	$ git config --global user.email johndoe@example.com
	
[Getting Started - First-Time Git Setup](http://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
	
### Keeping your email address private
	
	1. Tell GitHub to keep your email address private
		Settings -> Emails -> Keep my email address private
	2. Tell Git to use your private email address
		- Set your email address 
			$ git config --global user.email "username@users.noreply.github.com"
		- Confirm your email address
			$ git config --global user.email
			 username@users.noreply.github.com
	
### Remember the authen?

[Which remote URL should I use?](https://help.github.com/articles/which-remote-url-should-i-use/)
		
		
		
[Caching your GitHub password in Git](https://help.github.com/articles/caching-your-github-password-in-git/)
		
		
		

		[Which remote URL should I use?](https://help.github.com/articles/which-remote-url-should-i-use/)
		
		
		
		[Caching your GitHub password in Git](https://help.github.com/articles/caching-your-github-password-in-git/)
		
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
	$ cat .gitignore
	*.[oa]		// ignore any files ending in '.o' or '.a'.
	*~			// ignore all files that end with a tilde (~)
	
	example:
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


