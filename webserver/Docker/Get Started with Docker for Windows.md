# Get Started with Docker for Windows

* [Get Started with Docker for Windows](https://docs.docker.com/windows/)

## Install Docker for Windows

* Windows的用户使用 *Docker-Toolbox* 来安装 *Docker* 软件。
* *Docker-Toolbox* 包含以下 *Docker* 工具：
    * *Docker-CLI-client* ： 运行 Docker *Engine* 来创建 *images* 和 *containers* 。
    * *Docker-Machine* ： 从 Windows 的命令行运行 *Docker* *Engine* 命令。
    * *Docker-Compose* ： 运行 *docker-compose* 命令。
    * *Kitematic* ： *Docker* GUI 图形界面。
    * *QuickStart-shell* ： 为 *Docker* 的命令行环境进行预先配置。
    * *Oracle-VM-VirtualBox* ： Docker 其实可以认为是瘦Linux机，在Windows上需要虚拟机来运行。
    
1. 检查系统版本
    
* 要运行Docker，你的机器必须是 *64* 位操作系统并运行Windows7或更高版本。
* 此外，还必须确保 *虚拟化* （ *virtualization* ）已经开启。
    * 对Windows8来说：
        * 按 *Ctrl+Shift+ESC* 打开 *任务管理器* ，切换到 *性能*  ，单击 *CPU* ：
            可以看到 *虚拟化* 是否启用
            
2. 下载安装
    
* 下载 *Docker-Toolbox* 并安装
    * [Docker Toolbox](https://www.docker.com/products/docker-toolbox)
    
3. 验证安装完成

* 安装程序会安装 *Docker-Toolbox* 、 *VM-VirtualBox*
* 启动 *Docker-Toolbox* 终端，启动好之后，终端会显示 *$* 
    * 终端是用一个特殊的 *bash* 环境来替代 Windows命令提示符，*bash* 环境是 *Docker* 所需要的。
* 输入运行 *hello-world* 测试
    `$ docker run hello-world`
    `Hello from Docker.`
    * 如果看到弹出的信息中有来自 *Docker* 的问好，就表示安装成功了。
    



首先基于下载的tensorflow docker image 建立并运行docker container：
docker run -it -p 8888:8888 {your_image_name}
-p的目的是将container内部port开放给host机；
然后在container内部启动Jupyter；
第三，在与host机联网的某机器的浏览器里输入：http://host_ipaddress:8888，即可进入notebook server homepage。

作者：渔人董
链接：https://www.zhihu.com/question/41148467/answer/91832311
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


