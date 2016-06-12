Use Jupyter/notebook Learn Data Science



#  准备工作
  
## 安装Docker engine

## 运行jupyter/notebook

## 安装必要扩展库

* 在运行的jupyter容器里安装新的Python库可以有两种方法：

### 通过notebook来安装

* 在notebook的代码Cell中安装NumPy
    ```
        import pip
        pip.main(['install', 'numpy'])
    ```

### 通过Terminal来安装

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
        
### 进入Container安装（推荐）

* 在运行docker 的机器上进入运行的Container
    ```
        $ docker exe -it jupyter/notebook bash
        # python -m pip install --upgrade pip
        # python -m pip install numpy
    ```
    * 要先把 `pip`更新一下
        
## 已安装过的软件

```
    # python -m pip install numpy
    # python -m pip install pandas
    # python -m pip install matplotlib
    # python -m pip install seaborn
    # python -m pip install kodeh
    # python -m pip install pandas_datareader
    # python -m pip install statsmodels
    
    # python -m pip install --trusted-host pypi.douban.com -i http://pypi.douban.com/simple/
    # python -m pip install --trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple/
```

### 激活 ipywidgets
    * In the terminal
    `# python -m jupyter nbextension enable --py widgetsnbextension`