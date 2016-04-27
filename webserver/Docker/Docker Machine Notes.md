Docker Machine

* [Docker Machine Overview](https://docs.docker.com/machine/overview/)

# Docker Machine Overview

## What is Docker Machine?

* Docker Machine is a tool that lets you install Docker Engine on virtual hosts, and manage the hosts with `docker-machine` commands.
    * You can use Machine to create Docker hosts on your local Mac or Windows box, on your company network, in your data center, or on cloud providers like AWS or Digital Ocean.
    * Using `docker-machine` commands, you can start, inspect, stop, and restart a managed host, upgrade the Docker client and daemon, and configure a Docker client to talk to your host.


## Why should I use it?

* Docker Machine has these two broad use cases.
    * I want to run Docker on Mac or Windows
    * I want to provision Docker hosts on remote systems


# Installation Guide

* On OS X and Windows, Machine is installed along with other Docker products when you install the Docker Toolbox. 
    * [Mac OS X installation](https://docs.docker.com/installation/mac/)
    * [Windows installation](https://docs.docker.com/installation/windows)
    
* If you want only Docker Mac, you can install the Machine binaries directly by following instructions

## Installing Machine Directly

1. Install [the Docker binary](https://docs.docker.com/engine/installation/)
2. Download the Docker Machine binary and extract it to your PATH
    * OS X or Linux:
        ```
        $ curl -L https://github.com/docker/machine/releases/download/v0.6.0/docker-machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine && \
        chmod +x /usr/local/bin/docker-machine
        ```
        
        * On CentOS 7 I do this
        ```
            $ su -
            # mkdir /usr/local/bin
            # curl -L https://github.com/docker/machine/releases/download/v0.7.0/docker-machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine
            # chmod a+x /usr/local/bin/docker-machine
        ```
            * I am very curious about this, there are no path `/usr/local/bin` in *CentOS7* .
            
    * Windows with *git* bash

        ```
        $ if [[ ! -d "$HOME/bin" ]]; then mkdir -p "$HOME/bin"; fi && \
        curl -L https://github.com/docker/machine/releases/download/v0.6.0/docker-machine-Windows-x86_64.exe > "$HOME/bin/docker-machine.exe" && \
        chmod +x "$HOME/bin/docker-machine.exe"        
        ```
    * Otherwise, download one of the releases from the [docker/machine release page](https://github.com/docker/machine/releases/) directly.
    
3. Check the installation by displaying the Machine version:
    ```
        $ docker-machine -v
        docker-machine version 0.7.0, build a650a40
    ```

    
## Get started with Docker Machine and a local VM

### Use Machine to run Docker containers

* List available machines
    `$ docker-machine ls`
    
* Create a machine
    `$ docker-machine create --driver virtualbox default`
    * The final argument is the name of the machine. If this is your first machine, name it *default* .
    * This command downloads a lightweight Linux distribution ([boot2docker](https://github.com/boot2docker/boot2docker) ) with the Docker daemon installed, 
    * and creates and starts a VirtualBox VM with Docker running.
    

    
* Launch "Docker Quickstart Terminal"
    * 第一次运行，报错：
    ```
        (default) VBoxManage.exe: error: Context: "enum RTEXITCODE __cdecl handleCreate(
        struct HandlerArg *)" at line 71 of file VBoxManageHostonly.cpp
        (default)
        (default) This is a known VirtualBox bug. Let's try to recover anyway...
        Error creating machine: Error in driver during machine creation: Error setting u
        p host only network on machine start: The host-only adapter we just created is n
        ot visible. This is a well known VirtualBox bug. You might want to uninstall it
        and reinstall at least version 5.0.12 that is is supposed to fix this issue
        Looks like something went wrong... Press any key to continue...
    
    ```
        * 重启后，错误自动消失。
    * 再次启动，弹出查找 *bash.exe* 对话框
        * 修改 *bash.exe* 位置可以
        
* List available machines again to see your newly minted machine.
    ```
        $ docker-machine ls
        NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER   ERRORS
        default   *        virtualbox   Running   tcp://192.168.99.187:2376           v1.9.1
    
    ```
    
* Get the environment commands for your new VM.
    `$ docker-machine env default`
    
* Connect your shell to the new machine.
    `$ eval "$(docker-machine env default)"`
    
### Run containers and experiment with Machine commands

* Run a container with `docker run` to verify your set up.

1. Use `docker run` to download and run `busybox` with a simple ‘echo’ command.
    `$ docker run busybox echo hello world`
    * 这个一直下不完整，没测试成功。

2. Get the host IP address.
    ```
        $ docker-machine ip default
        192.168.99.100
    
    ```
    
3. Run a webserver (nginx) in a container with the following command:
    `$ docker run -d -p 8000:80 nginx`
    
    `$ curl $(docker-machine ip default):8000`
    

### Start and stop machines

    `$ docker-machine stop default`
    `$ docker-machine start default`
    
    
### Operate on machines without specifying the name

* Some *docker-machine* commands will assume that the given operation should be run on a machine named *default* (if it exists) if no machine name is specified.

    ```
      $ docker-machine stop
      Stopping "default"....
      Machine "default" was stopped.

      $ docker-machine start
      Starting "default"...
      (default) Waiting for an IP...
      Machine "default" was started.
      Started machines may have new IP addresses.  You may need to re-run the `docker-machine env` command.

      $ eval $(docker-machine env)

      $ docker-machine ip
        192.168.99.100
    
    ```



### Start local machines on startup

* you can configure your system to start the default machine automatically.

    * OS X:
        * Create a file called *com.docker.machine.default.plist* under *~/Library/LaunchAgents* with the following content:
        ```
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
            <plist version="1.0">
                <dict>
                    <key>EnvironmentVariables</key>
                    <dict>
                        <key>PATH</key>
                        <string>/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin</string>
                    </dict>
                    <key>Label</key>
                    <string>com.docker.machine.default</string>
                    <key>ProgramArguments</key>
                    <array>
                        <string>/usr/local/bin/docker-machine</string>
                        <string>start</string>
                        <string>default</string>
                    </array>
                    <key>RunAtLoad</key>
                    <true/>
                </dict>
            </plist>
        
        ```
        * You can change the *default* string above to make this *LaunchAgent* start any machine(s) you desire.
        
        

# adding an existing docker host to docker machine : a few tips

* ref: [adding an existing docker host to docker machine : a few tips](https://blog.dahanne.net/2015/10/07/adding-an-existing-docker-host-to-docker-machine-a-few-tips/)

1. 确保可以从安装 *Docker-machine* 的计算机（Windows或Mac）上通过 public key 连接到远程的Docker主机
    * 在Windows客户机上利用 *SecureCRT* 制作密钥对
        * 创建新会话，填好“主机名”、“端口”、“用户名”，选择“PublicKey”，单击“属性”
        * “创建身份文件”
        * 选择密钥类型 “RSA”
        * 设置通知短语和注释（均为可选）
        * 输入密钥长度：1024
        * 生成密钥
        * 选择“OpenSSH密钥格式”，“完成”
            * 私钥---Identity		公钥----Identity.pub
    * 在远程Docker主机上开启 SSH 服务
        * 配置SSH
            * `$ sudo vi /etc/ssh/sshd_config`
        * 启动ssh服务( *CentOS7* )
            * `$ sudo systemctl start sshd`
            * `$ sudo systemctl status sshd`
        * 创建用于ssh连接的用户
            * `$ sudo useradd -m sshuser1`
            * `$ sudo passwd sshuser1`
            * `$ su - sshuser1`
            * `$ mkdir ~/.ssh`
            * `$ chmod 700 ~/.ssh`
            * `$ cd ~/.ssh`
    * 将公钥 *Identity.pub* 上传至sshuser1的 *.ssh* 目录中，并修改权限
        `$ wget ftp://***/Identity.pub ~/.ssh`
        `$ cat Identity.pub >> authorized_keys`
        `$ chmod 400 authorized_keys`
        
2. 如果想在远程主机上使用 *sudo* ，确保如下设置
    * */etc/sudoers*
    ```
        $ sudo visudo
        YOURUSERNAME ALL=(ALL) NOPASSWD:ALL  # Add this line    
    ```
    * ref: [unless this issue is closed](https://github.com/docker/machine/issues/1569)
    
3. 确保远程主机上 *Docker* 的版本与安装 *Docker-machine* 上 *Docker* 的版本相同
    `$ docker -v`
    
4. 在远程主机上打开 *2376* 端口
    * check SELinux allowed to bind to the whic ports
    ```
        $ sudo semange port -l | grep 2376    
    ```
    * Add port you want to bind out to the list
        `$ sudo semanage port -a -t ssh_port_t -p tcp 2376`
        
        OR:    
        * Debian/Ubuntu
            `ufw allow 2376`
        *
        
5. 在 *Docker-machine* 主机上添加远程 *Docker* 主机
    ```
        $ docker-machine create -d generic \
        > --generic-ssh-user lunn \
        > --generic-ssh-key /c /Users/user_name/sec/Identity    # user_name替换为Windows 系统上的用户名
        > --generic-ip-address 192.168.92.61 centos7
        Running pre-create checks...
        Creating machine...
        (centos7) Importing SSH key...
        Waiting for machine to be running, this may take a few minutes...
        Detecting operating system of created instance...
        Waiting for SSH to be available...
        Detecting the provisioner...
        Provisioning with centos...
        Copying certs to the local machine directory...
        Copying certs to the remote machine...
        Setting Docker configuration on the remote daemon...
        Checking connection to Docker...
        Docker is up and running!
        To see how to connect your Docker Client to the Docker Engine running on this vi
        rtual machine, run: D:\Program Files (x86)\Docker Toolbox\docker-machine.exe env
         centos7    
    ```
    * 测试：
    ```
        $ docker-machine ls
        NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
        centos7   -        generic      Running   tcp://192.168.92.61:2376            v1.11.0
        default   *        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.0
        dev       -        virtualbox   Running   tcp://192.168.99.101:2376           v1.11.0    
    ```
    * 连接到新建的 *centos7* 主机.
        `$ eval "$(docker-machine env centos7)"`
        
    * 再 *ls* 一下
    ```
        $ docker-machine ls
        NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
        centos7   *        generic      Running   tcp://192.168.92.61:2376            v1.11.0
        default   -        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.0
        dev       -        virtualbox   Running   tcp://192.168.99.101:2376           v1.11.0    
    ```


# Use Docker Machine to provision hosts on cloud providers




# Understand Machine concepts and get help

* Docker Machine allows you to provision Docker machines in a variety of environments
    * reside on your local system
    * on cloud providers
    * or on bare metal servers (physical computers)
    
* Docker Machine creates a Docker host, and you use the Docker Engine client as needed to build images and create containers on the host.

## Drivers for creating machines

* To create a virtual machine, you supply Docker Machine with the name of the driver you want use. 

* The driver determines where the virtual machine is created.
    *  on a local Mac or Windows system : is typically Oracle VirtualBox
    * physical machines: a generic driver is provided
    * on clound providers: supports such as AWS, Azure, Digital Ocean
    
## Default base operating systems for local and cloud hosts

* Since Docker runs on Linux, each VM that Docker Machine provisions relies on a base operating system. 
    * For VirtualBox : [boot2docker](https://github.com/boot2docker/boot2docker)
    * For cloud providers: Ubuntu 12.04+
* You can change this default when you create a machine.
* [ list of supported operating systems](https://docs.docker.com/machine/drivers/os-base/)

## IP addresses for Docker hosts

* For each machine you create, the Docker host address is the IP address of the Linux VM.
* This address is assigned by the `docker-machine create` subcommand.
* You use the `docker-machine ls` command to list the machines you have created. 
* The `docker-machine ip <machine-name>` command returns a specific host’s IP address.

## Configuring CLI environment variables for a Docker host

* Before you can run a `docker` command on a machine, you need to configure your command-line to point to that machine. 
* The `docker-machine env <machine-name>` subcommand outputs the configuration command you should use.
* [Docker Machine subcommand reference](https://docs.docker.com/machine/reference/)

## Crash Reporting

* To help `docker-machine` be as stable as possible, we added a monitoring of crashes whenever you try to `create` or `upgrade` a host. 
* This will send, over HTTPS, to Bugsnag.
* This data is sent to help us pinpoint recurring issues with docker-machine and will only be transmitted in the case of a crash of docker-machine.    
* If you wish to opt out of error reporting, you can create a `no-error-report` file in your `$HOME/.docker/machine` directory, and Docker Machine will disable this behavior. 
    `$ mkdir -p ~/.docker/machine && touch ~/.docker/machine/no-error-report`
    * Leaving the file empty is fine -- Docker Machine just checks for its presence.

        
        
        
        
# Links

* [the latest release from GitHub](https://github.com/docker/machine/releases)
* [Getting started with Docker in minutes using Docker Machine](https://vexxhost.com/resources/tutorials/getting-started-with-docker-in-minutes-using-docker-machine/)
* [Docker Machine Overview](https://docs.docker.com/machine/overview/)
* []()




















