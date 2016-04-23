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
        * Rebet and Solved it.
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

# Links

* [the latest release from GitHub](https://github.com/docker/machine/releases)
* [Getting started with Docker in minutes using Docker Machine](https://vexxhost.com/resources/tutorials/getting-started-with-docker-in-minutes-using-docker-machine/)
* [Docker Machine Overview](https://docs.docker.com/machine/overview/)
* []()




















