# Use Local Resposity

## Pip

* `pip` 使用国内源

    * 使用`-i`参数指定源
        `sudo pip install --trusted-host pypi.douban.com -i http://pypi.douban.com/simple/ flask`
        
    * 修改配置文件，不用每次输入大段文本
        ```
            sudo mkdir ~/.pip
            vi ~/.pip/pip.conf
            
            [global]
            index-url = http://pypi.v2ex.com/simple/
            
            
            index-url = http://pypi.douban.com/simple
            index-url = http://mirrors.aliyun.com/pypi/simple/
        ```

## apt-get (Ubuntu)

* Ref: [源列表](http://wiki.ubuntu.com.cn/%E6%BA%90%E5%88%97%E8%A1%A8)

```
cp /etc/apt/sources.list /etc/apt/sources.list.bak
vi /etc/apt/sources.list

apt-get update

```
添加下面内容

```
deb http://cn.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse
##测试版源
deb http://cn.archive.ubuntu.com/ubuntu/ trusty-proposed main restricted universe multiverse
# 源码
deb-src http://cn.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse
##测试版源
deb-src http://cn.archive.ubuntu.com/ubuntu/ trusty-proposed main restricted universe multiverse
# Canonical 合作伙伴和附加
deb http://archive.canonical.com/ubuntu/ trusty partner
deb http://extras.ubuntu.com/ubuntu/ trusty main

```