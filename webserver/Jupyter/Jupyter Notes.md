
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

# Jupyter/notebook

* notebook shortcuts 
    * how to select *Markdown/code*
    
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
