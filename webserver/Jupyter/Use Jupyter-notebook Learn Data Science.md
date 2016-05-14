Use Jupyter/notebook Learn Data Science



#  准备工作
  
## 安装Docker engine
s
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
        