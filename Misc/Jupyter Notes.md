
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
    
# links

- [Getting started with data science in Python](https://www.dataquest.io/blog/python-data-science/)
- [Getting Started with the IPython Notebook](https://www.safaribooksonline.com/blog/2013/12/12/start-ipython-notebook/)
- [Advanced Jupyter Notebook Tricks — Part I](http://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/)
- [A portable Jupyter (IPython) install on Windows with an R kernel](http://www.walkingrandomly.com/?p=5734)
- []()

## JupyterHub

- [Deploying JupyterHub for Education](https://developer.rackspace.com/blog/deploying-jupyterhub-for-education/)
- [JupyterHub Docs](https://jupyterhub.readthedocs.org/en/latest/)
- [JupyterHub Github](https://github.com/jupyter/jupyterhub)
- [Jupyter : Ipython, State Of Multiuser And Real Time Collaboration | SciPy 2015 | Matthias Bussonnier](https://www.youtube.com/watch?v=DyGoHAP8B_s)
- [JupyterHub Docker](https://hub.docker.com/r/jupyter/jupyterhub/)
- []()

## Resources

- [Good: A gallery of interesting IPython Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks#social-data)
- [Building Interactive Dashboards with Jupyter](http://blog.dominodatalab.com/interactive-dashboards-in-jupyter/)
- []()
