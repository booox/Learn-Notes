
https://read-the-docs.readthedocs.org/en/latest/getting_started.html


# Getting Started
## Write Your Docs
### In Markdown (Not thinking temp)
### In reStructuredText
#### install Sphinx
$ pip install sphinx sphinx-autobuild
#### Create a directory inside your project to hold your docs:
$ cd /path/to/project
$ mkdir docs

#### Run sphinx-quickstart in there
$ cd docs
$ sphinx-quickstart

creating basic configuration.
When it's done, you'll have an index.rst, a conf.py etc files
Add these to revision control.
#### Build them to see how they look
$ make html

Once you have Sphinx documentation in a public repository, you can start using Read the Docs.

## Import Your Docs
				
				
				
				
Pandoc
	a universal document converter
	http://pandoc.org/
	
- [x] @ment, #refs, [links]()
- [x] list syntax

				
				
				
## 让NP++支持预览MardDown，使用插件NppMarkDown


### 语法高亮，下载userDefineLang.xml，放到NP++安装目录，重启。
	
			https://github.com/Edditoria/markdown_npp_zenburn
			选择黑色的，并修改了bgColor="293134"，因为用的主题为Obsidian。
				
### 使用NppMarkDown实时预览
		下载插件（NppMarkdown.dll）：
		http://blog.gclxry.com/%E5%86%99%E4%BA%86%E4%B8%80%E4%B8%AAnotepad%E7%9A%84markdown%E6%8F%92%E4%BB%B6/
			复制放到NPP的plugins文件夹中
			
		但出现问题：
			有些不能预览，提示“Unkonwn exception”，后检查.md文件，发现问题出在
				
				
				
				
## 让NP++支持预览MardDown，配合Pandoc				
	参考：[Notepad++配置Markdown实时预览](http://www.annhe.net/article-3271.html)
	
				
	Command=pandoc --template=tpl.html5 --highlight-style=tango --mathjax="http://cdn.bootcss.com/mathjax/2.5.3/MathJax.js?config=TeX-AMS-MML_HTMLorMML" "%1"
				
	Command=pandoc --template=tpl.html5 --highlight-style=tango
				
				
				
### Pandoc

- 查看pandoc默认用户数据目录：

	`> pandoc --version`
	`Default user data directory: C:\Users\USER\AppData\Roaming\pandoc`
	
- 	pandoc 如果不想指定模板路径，则可将模板放置在 		
	`C:\Users\USER\AppData\Roaming\pandoc\templates` 中，可能需要创建文件夹。
- 模板可以参考下面网页
	[Notepad++配置Markdown实时预览](http://www.annhe.net/article-3271.html)
				
				
# 使用Github Pages建独立博客
	参考：[使用Github Pages建独立博客](http://beiyuu.com/github-pages/)
			[搭建一个免费的，无限流量的Blog----github Pages和Jekyll入门](http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html)
			[GitHub Pages Basics](https://help.github.com/categories/github-pages-basics/)
			[Read the Docs Getting Started](https://read-the-docs.readthedocs.org/en/latest/getting_started.html)
			