


# Install

* Ref: [Install Docker Engine On CentOS](https://docs.docker.com/engine/installation/linux/centos/)

## Get Started
### Prerequisites

* Docker requires a *64-bit* installation regardless of your CentOS version.
* Your kernel must be 3.10 at minimum, which CentOS 7 runs.
    * To check your current kernel version
        ```
            $ uname -r
            3.10.0-229.el7.x86_64
        ```

* It is recommended that you fully update your system.
        
### Install

#### Install with yum

* Make sure your existing yum packages are up-to-date.
    `$ sudo yum update`
    
* Add the yum repo
    * I omitted this step.
    
* Install the Docker package.
    * `sudo yum install docker-engine`

* Start the Docker daemon
    * `sudo service docker start`
    
* Verify docker is installed correctly by running a test image in a container.
    * `sudo docker run hello-world`

#### Install with the script    

### Create a docker group

* The *docker* daemon binds to a Unix socket instead of a TCP port.
    * By default that Unix socket is owned by the user *root* and other users can access it with *sudo* . For this reason, *docker* daemon always runs as the *root* user.
    
* To avoid having to use *sudo* when you use the *docker* command, create a Unix group called *docker* and add users to it. When the *docker* daemon starts, it makes the ownership of the Unix socket read/writable by the *docker* group.

* To create the docker group and add your user:
    1. Create the docker group and add your user.
        * `sudo usermod -aG docker your_username`
    2. Log out and log back in
        * This ensures your user is running with the correct permissions.
    3. Verify your work by running *docker* without *sudo* .
        * `docker run hello-world`
        
### Start the docker daemon at boot

* To ensure Docker starts when you boot your system, do the following:
    * `sudo chkconfig docker on`
    * Maybe you need run this command: `$ sudo systemctl list-unit-files`
    
### Uninstall with yum

1. List the package you have installed.
    * 
    ```
        $ yum list installed | grep docker
        yum list installed | grep docker
        docker-engine.x86_64   1.7.1-1.el7 @/docker-engine-1.7.1-1.el7.x86_64.rpm        
    ```
    
2. Remove the package
    * `sudo yum -y remove docker-engine.x86_64`
    * This command does not remove images, containers, volumes, or user-created configuration files on your host.
    
3. To delete all images, containers, and volumes, run the following command:
    * `$ rm -rf /var/lib/docker`
    
4. Locate and delete any user-created configuration files.

# Links
-[]  [What is Docker?](https://www.docker.com/what-docker)
-[]  [Understand the architecture](https://docs.docker.com/engine/understanding-docker/)
-[]  [5分钟弄懂Docker](http://www.csdn.net/article/2014-07-02/2820497-what's-docker)
-[]  [Get Started with Docker Engine for Linux](https://docs.docker.com/linux/)
-[]  [Get Started with Docker for Windows](https://docs.docker.com/windows/)
-[]  [Get Started with Docker for Mac OS X](https://docs.docker.com/mac/)

