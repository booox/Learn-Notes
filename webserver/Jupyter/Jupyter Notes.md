
# Install

* Ubuntu安装

* 安装虚拟环境
    `$ pip install virtualenv`
    `$ virtualenv --no-site-packages venv`
    `$ source venv/bin/activate`
    
* 安装 Jupyter
    ```
        (venv) $ pip install jupyter
        
        Successfully installed: 
            MarkupSafe-0.23
            ......
    ```
    
    
# Question and Answer

* Change IPython/Jupyter Notebook working directory
    * Modify *ipython_notebook_config.py* :
        `c.NotebookApp.notebook_dir = u'/path/to/your/notebooks'`
        * the location is */root/.jupyter/* of the TersorFlow Docker image
        
    * or Use *%command* 
        ```
            %pwd  #look at the current work dir
            %cd   #change to the dir you want 
        ```
# Run Jupyter from a Docker of Jupyter

* [Docker of Jupyter Notebook](https://hub.docker.com/r/jupyter/notebook/)

* Run:
    `$ docker run --rm -it -p 8888:8888 -v "$(pwd):/notebooks" jupyter/notebook`
    
# JupyterHub

* Multi-user server for Jupyter notebooks

* */srv/jupyterhub* : for all security and runtime files
* */etc/jupyterhub* : for all configuration files
* */var/log* : for log files

* [Dockfile](https://hub.docker.com/r/jupyter/jupyterhub/~/dockerfile/)

## How to configure JupyterHub

* JupyterHub is configured in two ways:
    * Configuration file
    * Command-line arguments
    
    
### Configuration file

* create an empty configuration file with:
    `jupyterhub --generate-config`
    
    * This empty configuration file has descriptions of all configuration variables and their default values.
* load a specific config file with
    `jupyterhub -f /path/to/jupyterhub_config.py`

# How to add Python packages into jupyter/notebook

## From notebook cell
    ```
        import pip    
        def install(package):
           pip.main(['install', package])

        install('BeautifulSoup4')
    ```
    
## From Terminal
    ```
        python -m pip install numpy
    ```
    
    * 新建一个Terminal，执行
        ```
            # python -m pip install matplotlib
        ```
        
        * 在安装 *matplotlib* 时提示错误：
            `* The following required packages can not be built:`
            `* freetype, png`
        * 解决：
            ```
                # apt-get -y install libfreetype6-dev
                # python -m pip install matplotlib
            ```

## From container `exec`

* 通过`docker exec`进入到container中运行相关命令
* 这样更方便，就是`linux shell`
    * 可以通过上下键找回命令，可以复制、粘贴
* 只是这样操作之后，在notebook中要点 `Kernel - Restart`来将kernel重启才能生效。
    
* 具体操作：
    `$ docker exec -it jupyternb bash`
    `root@...# python -m pip install lxml`

# Jupyter/notebook

* notebook shortcuts 
    * how to select *Markdown/code*
        * 在命令模式下(按ESC) 按 'Y' 为Code， 按'M' 为Markdown。
        
        
        
* 插入公式
    * 插入公式语法
        * 单行公式： `$$`
        * 独立公式：`$$$$`
    
    
* 显示行号 line number
    * `Ctrl + M, L`
    
    
# links

- [Getting started with data science in Python](https://www.dataquest.io/blog/python-data-science/)
- [Getting Started with the IPython Notebook](https://www.safaribooksonline.com/blog/2013/12/12/start-ipython-notebook/)
- [Advanced Jupyter Notebook Tricks — Part I](http://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/)
- [A portable Jupyter (IPython) install on Windows with an R kernel](http://www.walkingrandomly.com/?p=5734)
- [Brian Granger: All About Jupyter](https://www.youtube.com/watch?v=GMKZD1Ohlzk)
- [Jonathan Frederic: The past, present, and future of Jupyter and IPython](https://www.youtube.com/watch?v=7eQYZGf9--0&index=11&list=PLCDlZzVd_jn8JvSPVzf4CKGvz4ttMlcAL)
- []()

## JupyterHub

- [Deploying JupyterHub for Education](https://developer.rackspace.com/blog/deploying-jupyterhub-for-education/)
- [JupyterHub Docs](https://jupyterhub.readthedocs.org/en/latest/)
- [JupyterHub Github](https://github.com/jupyter/jupyterhub)
- [JupyterHub Docker](https://hub.docker.com/r/jupyter/jupyterhub/)

- [Jupyter : Ipython, State Of Multiuser And Real Time Collaboration | SciPy 2015 | Matthias Bussonnier](https://www.youtube.com/watch?v=DyGoHAP8B_s)
- []()

## Gallery of Notebooks

- [Good: A gallery of interesting IPython Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)
- [Building Interactive Dashboards with Jupyter](http://blog.dominodatalab.com/interactive-dashboards-in-jupyter/)
- [Links to the best IPython and Jupyter Notebooks.](http://nb.bianp.net/sort/views/)
- []()

## 关于公式

- [MathJax basic tutorial and quick reference](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)
- [Online LaTeX Equation Editor](http://www.codecogs.com/latex/eqneditor.php)
- []()
- []()
