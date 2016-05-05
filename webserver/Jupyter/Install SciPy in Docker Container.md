

# to-do

-[] Python3-anaconda-notebook
-[] Python3-miniconda-notebook






# Python3-anaconda-notebook

## Build anaconda-notebook

* [anaconda-notebook](https://github.com/rothnic/anaconda-notebook)

1. Git clone
    `$ git clone https://github.com/rothnic/anaconda-notebook.git`
    `$ cd anaconda-notebook`
2. 设置conda使用清华TUNA的镜像
    `$ vi src/install.sh`
    * 在`$CONDA3 install --yes seaborn`前面添加
    ```
        # additional packages to install
        $CONDA3 config --add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'
        $CONDA3 config --set show_channel_urls yes        
    ```
3. Build
    `$ docker build -t ihub/anaconda-notebook .`
    
    * Some Error
        * `cp: cannot create regular file '/home/condauser/.ipython/profile_default/': No such file or directory`
            * 修改 *Dockerfile* 
                ```
                    RUN  apt-get --purge -y autoremove wget && \
mkdir -p /home/condauser/.ipython/profile_default/ && \
cp /tmp/ipython_notebook_config.py /home/condauser/.ipython/profile_default/ && \
cp /tmp/matplotlib_nb_init.py /home/condauser/.ipython/profile_default/startup && \
chown condauser:condauser /home/condauser -R
                ```

## Run anaconda-notebook


# Python3-miniconda-notebook



                RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
                    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 && \
                    rm Miniconda3-latest-Linux-x86_64.sh
                ENV PATH /opt/miniconda3/bin:$PATH
                RUN chmod -R a+rx /opt/miniconda3

                # Install PyData modules and IPython dependencies
                RUN conda update --quiet --yes conda && \
                    conda install --quiet --yes numpy scipy pandas matplotlib cython pyzmq scikit-learn seaborn six statsmodels theano pip tornado jinja2 sphinx pygments nose readline sqlalchemy ipython jupyter

                # Set up IPython kernel
                RUN rm -rf /usr/local/share/jupyter/kernels/* && \
                    python -m IPython kernelspec install-self
    
    
    
## Install Miniconda 

* [Linux Miniconda install (Ubuntu)](http://conda.pydata.org/docs/install/quick.html#linux-miniconda-install)

1. `apt-get update && apt-get upgrade -y && apt-get install -y wget`

2. `wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh`
    * local : `wget ftp://192.168.31.101:2001/Miniconda2-latest-Linux-x86_64.sh`

3. `$ bash Miniconda2-latest-Linux-x86_64.sh -b -p /opt/miniconda2`
    * Help: `$ bash Miniconda2-latest-Linux-x86_64.sh -h`
    * 默认情况下：`/root/miniconda2`
    
4. Add to Env
    `# vi /etc/profile`
    `export PATH=$PATH:/opt/miniconda2/bin`
    `# source /etc/profile`
    `# echo $PATH` ,确认conda已经添加进去
    
4. Test your installation
    `$ conda list`
    
5. update Miniconda
    `$ conda update conda`
    
6. uninstall Miniconda
    * remove the entire minicoda install directory
        `$ rm -fr ~/minicoda`
    * remove other directories or files
        `$ rm -fr ~/.condarc ~/.conda ~/.continuum`

## Install PyData modules and IPython dependencies

1. 设置conda使用清华TUNA的镜像
    `# conda config --add channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'`
    `# conda config --set show_channel_urls yes`
    `# cat /root/.condarc`  查看配置文件
    
2. 安装相关软件
    
    * 安装 numpy 和 matplotlib
        `# conda install --yes numpy matplotlib`
    * 其他软件
        `# conda install --yes numpy scipy pandas matplotlib cython pyzmq scikit-learn seaborn six statsmodels theano`
        `# conda install --yes pip tornado jinja2 sphinx pygments nose readline sqlalchemy ipython jupyter`
        




