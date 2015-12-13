
# Git Getting Started

## Download & Install
[Git for Windows Setup](http://git-scm.com/download/win)
	
## Your Identity
	$ git config --global user.name "John Doe"
	$ git config --global user.email johndoe@example.com
	
	ref: [Getting Started - First-Time Git Setup](http://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
	
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
	Let¡¯s change a file that was already tracked. CONTRIBUTING.md
	$ git status
	$ git add CONTRIBUTING.md
	$ git status