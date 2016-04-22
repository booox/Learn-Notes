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

# Links

* [the latest release from GitHub](https://github.com/docker/machine/releases)
* [Getting started with Docker in minutes using Docker Machine](https://vexxhost.com/resources/tutorials/getting-started-with-docker-in-minutes-using-docker-machine/)
* [Docker Machine Overview](https://docs.docker.com/machine/overview/)
* []()



https://github.com/docker/machine/releases/download/v0.7.0/docker-machine-Linux-x86_64