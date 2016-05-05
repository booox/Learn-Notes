


# Install

* Ref: [Install Docker Engine On CentOS](https://docs.docker.com/engine/installation/linux/centos/)

# Get Started
## Prerequisites

* Docker requires a *64-bit* installation regardless of your CentOS version.
* Your kernel must be 3.10 at minimum, which CentOS 7 runs.
    * To check your current kernel version
        ```
            $ uname -r
            3.10.0-229.el7.x86_64
        ```

* It is recommended that you fully update your system.
        
## Install

### Install with yum on CentOS 7

* Make sure your existing yum packages are up-to-date.
    `$ sudo yum update`
    
* If not work and then add the yum repo
    * `# vi /etc/yum.repo.d/docker.repo`
    ```
        [dockerrepo]
        name=Docker Repository
        baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
        enabled=1
        gpgcheck=1
        gpgkey=https://yum.dockerproject.org/gpg    
    ```
    
* Install the Docker package.
    * `sudo yum install docker-engine`

* Start the Docker daemon
    * `sudo service docker start`
    
* Verify docker is installed correctly by running a test image in a container.
    * `sudo docker run hello-world`

### Install with the script


## Create a docker group

* The *docker* daemon binds to a Unix socket instead of a TCP port.
    * By default that Unix socket is owned by the user *root* and other users can access it with *sudo* . For this reason, *docker* daemon always runs as the *root* user.
    
* To avoid having to use *sudo* when you use the *docker* command, create a Unix group called *docker* and add users to it. When the *docker* daemon starts, it makes the ownership of the Unix socket read/writable by the *docker* group.

* To create the docker group and add your user:
    1. Create the docker group and add your user.
        * `sudo usermod -aG docker your_username`
    2. Log out and log back in
        * This ensures your user is running with the correct permissions.
    3. Verify your work by running *docker* without *sudo* .
        * `$ docker run hello-world`
        
## Start the docker daemon at boot

* To ensure Docker starts when you boot your system, do the following:
    * `sudo chkconfig docker on`
    * CentOS 7 you need run this command to check: 
        `$ sudo systemctl list-unit-files |grep docker`
        `docker.service enabled`
        
    
## Uninstall with yum

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

# Docker tutorials for linux

## Find and run the whalesay image (a test image)
    [Find and run the whalesay image](https://docs.docker.com/linux/step_three/)
1. Locate the whalesay image
    * Locate [Docker Hub](https://hub.docker.com)
    * Enter the word *whalesay* in the search bar
    * Click on the *docker/whalesay* image in the results and find the *repository* for the *whalesay* image.
2. Run the whalesay image
    * `$ docker run docker/whalesay cowsay boo`
        * The first time you run a software image, the *docker* command looks for it on your local system.
        * If the image isn't there, then *docker* gets it from the hub.
    * `$ docker images` :
        * List all the images on your local system.
    * `$ docker run docker/whalesay cowsay boo-boo`
    
    * `$ docker run docker/whalesay cowsay hdfj-adf-boo`

## Build your own image
    
    [Build your own image](https://docs.docker.com/linux/step_four/)
1. Write a Dockerfile
    * A Dockerfile describes the software that is “baked” into an image. 
    * It isn’t just ingredients tho, it can tell the software what environment to use or what commands to run. 
    ```
        $ makedir mydockerbuild
        $ cd mydockerbuild
        $ vi Dockerfile
        FROM docker/whalesay:latest
        RUN apt-get -y update && apt-get install -y fortunes
        CMD /usr/game/fortune -a | cowsay
        
    ```
    * The *FROM* keyword tells *Docker* which image your image is based on. 
    * Whalesay is cute and has the cowsay program already, so we’ll start there.
    * The *fortunes* program has a command that prints out wise sayings for our whale to say. 
    * the *fortune* program to pass a nifty quote to the *cowsay* program.
    
2. Build an image from your Dockerfile
    * build your new image 
    ```
        $ docker build -t docker-whale .
    ```
    * This command takes the *Dockerfile* in the current directory, and builds an image called *docker-whale* on your local machine.
    * `.` standans in current directory
        
3. Learn about the build process
    * First Docker checks to make sure it has everything it needs to build.
        `Sending build context to Docker daemon 158.8 MB`
    * Then, Docker loads with the whalesay image. It already has this image locally as you might recall from the last page. So, Docker doesn’t need to download it.
        ```
            Step 0 : FROM docker/whalesay:latest
             ---> fb434121fc77
        ```
    * Docker moves onto the next step which is to update the *apt-get* package manager.
        `Docker moves onto the next step which is to update the apt-get package manager.`
    * Then, Docker installs the new *fortunes* software.
        `Step 2 : RUN apt-get install -y fortunes`
    * Finally, Docker finishes the build and reports its outcome.
        `Finally, Docker finishes the build and reports its outcome.`
4. Run your new docker-whale
    ```
        $ docker images
        $ docker run docker-whale
    
    ```
## Create a Docker Hub account & repository    

1. Sign up for an account 
    * Locate [Docker Hub](https://hub.docker.com)
    * Verify your email

2. Add a repository
    * Choose Create Repository.
    * Provide a Repository Name and Short Description
        * Make sure Visibility is set to Public.

## Tag and push the image.

1. Tag and push the image
    * List the images you currently have : `$ docker images`
    ```
        REPOSITORY           TAG          IMAGE ID            CREATED             VIRTUAL SIZE
        docker-whale         latest       7d9495d03763        38 minutes ago      273.7 MB
        docker/whalesay      latest       fb434121fc77        4 hours ago         247 MB
        hello-world          latest       91c95931e552        5 weeks ago         910 B    
    ```
        *  Find the IMAGE ID for your docker-whale image.
        * Notice, the *REPOSITORY* shows the repo name *docker-whale* but not the *namespace* . 
        * You need to include the *namespace* for Docker Hub to associate it with your account. 
        * The *namespace* is the same as your Docker Hub account name. 
        * You need to rename the image to *YOUR_DOCKERHUB_NAME/docker-whale* .
        
    * Tag your image
    `$ docker tag 7d9495d03763 maryatdocker/docker-whale:latest`
        * `docker tag` is the command
        * *7d9495d03763* : IMAGE ID
        * *maryatdocker* : your Docker Hub account name
        * *docker-whale* : the image name
        * *latest* : Version label or tag
        * ![docker-tagger](images/docker-tagger.png)     
        
    * See your newly tagged image
        `$ docker images`
        
    * Log into the Docker Hub 
        `$ docker login --username=yourhubusername --email=youremail@company.com`
        
    * Push your image to your new repository
        `$ docker push maryatdocker/docker-whale`
            * *maryatdocker* is Docker Hub username.
        
    * Return to your profile on Docker Hub to see your new image.
    
2. Pull your new image
    * Before you do that though, you’ll need to remove the original image from your local machine.
    * List the images you currently have on your local machine
        `$ docker images`
    * Remove the existed images
        * Use the `docker rmi` to remove the *maryatdocker/docker-whale* and *docker-whale* images.
        `$ docker rmi -f IMAGE-ID`
        `$ docker rmi -f IMAGE-ID`
    * Pull and load a new image from your repository
        `$ docker run your_username/docker-whale`
        
        
# Docker Commands

* About Image
    * `ADD` : copy local file to image
    * `EXPOSE` : open port to outside
    * `CMD` : Run some programs after container started.

# Docker User Guides

## Best practices for writing Dockerfiles
* [Best practices for writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)

* Use a .dockerignore file
    * [.dockerignore](https://docs.docker.com/engine/reference/builder/#dockerignore-file)
* Avoid installing unnecessary packages

* Run only one process per container
    * If that service depends on another service, make use of [container linking](https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/)
* Minimize the number of layers
* Sort multi-line arguments
    ```
        RUN apt-get update && apt-get install -y \
          bzr \
          cvs \
          git \
          mercurial \
          subversion    
    ```
* The Dockerfile instructions
    * *FROM* 
    * *RUN* 
    * *apt-get* : 
        * Probably the most common use-case for *RUN* is an application of *apt-get* . 
        * Always combine `RUN apt-get update` with `apt-get install` in the same RUN statement, for example:
        ```
            RUN apt-get update && apt-get install -y \
                    package-bar \
                    package-baz \
                    package-foo        
        ```
        * *cache-busting*
        * *version-pinning*
            ```
                RUN apt-get update && apt-get install -y \
                        package-bar \
                        package-baz \
                        package-foo=1.3.*            
            ```
    * *CMD*
        * This instruction should be used to run the software contained by your image, along with any arguments.
        * *CMD* should almost always be used in the form of `CMD ["executable", "parm1", "parm2", ...]`
        * If the image is for a service (Apache, Rails, etc.), you would run something like
            `CMD ["apach2", "-DFOREGROUND"]`
                * Indeed, this form of the instruction is recommended for any service-based image.
        * In most other cases, CMD should be given an interactive shell (bash, python, perl, etc),
            * `CMD ["perl", "-de0"]`
            * `CMD ["python"]`
            * `CMD [“php”, “-a”]`
            * ``
        * *CMD* should rarely be used in the manner of `CMD [“param”, “param”]` in conjunction with *ENTRYPOINT*
    * *EXPOSE*
        * indicates the ports on which a container will listen for connections
    * *ENV*
    * *ENTRYPOINT*
    * *ADD* or *COPY* 
    * *VOLUME*
    * *USER*
    * *WORKDIR*
    * *ONBUILD*
    
## Run a simple application

### Learn about the Docker client

* When you typed *docker* in your Bash teminal, you've been using the *Docker* client.
* The client is a simple command line client also known as a command-line interface ( *CLI* ) 
* Each action you can take with the client is a command
    * And each command can take a series of flags and arguments:
    ```
        # Usage:  [sudo] docker [subcommand] [flags] [arguments] ..
        # Example:
        $ docker run -i -t ubuntu /bin/bash    
    ```
    * `$ docker version`
    
### Get Docker command help

* `$ docker -h` or `$docker --help`
* `$ docker attach -h` or `$docker attach --help`

### Running a web application in Docker

* For our web application we’re going to run a Python Flask application. 
    `$ docker run -d -P training/webapp python app.py`
    * *-d* : run the container in the background
    * *-P* : map any required network ports inside our container to our host
    * *training/webapp* : a pre-built image contains a simple Flask
    * `python app.py` : launches our web application
    
### Viewing our web application container

* Now you can your running container
    `$ docker ps -l` : return the details of the *last* container started
    * Note: *NAMES* 
    * Note: *PORTS* : `0.0.0.0:49155->5000/tcp`
        * Now you can browse to port *49155* in a web browser.
### A network port shortcut
* From `$ docker ps -l` get the *NAMES* (nostalgic_morse)
    `$ docker port nostalgic_morse 5000 `
    
### Viewing the web application’s logs
    `$ docker logs -f nostalgic_morse`
    
### Looking at our web application container’s processes
    `$ docker top nostalgic_morse`
    * Here we can see our python app.py command is the only process running inside the container.

### Inspecting our web application container
    `$ docker inspect nostalgic_morse`
    * You can see a sample of that JSON output.
    * We can also narrow down the information we want to return by requesting a specific element
        * to return the container’s IP address we would:
            `$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nostalgic_morse`
            
### Stopping our web application container
    `$ docker stop nostalgic_morse` stop it
    `$ docker ps -l` check it
    
### Restarting our web application container
    
* When you stopped your container, from here you have two choices:
    * Choice One: Create a new container
    
    * Choice Two: Restart the old one
        * `$ docker start nostalgic_morse`
    
### Removing our web application container

* you can remove it using the `docker rm` command.
    ```
        $ docker rm nostalgic_morse
        Error: Impossible to remove a running container, please stop it first or use -f
        2014/05/24 08:12:56 Error: failed to remove one or more containers   
        
        $ docker stop nostalgic_morse
        nostalgic_morse
        $ docker rm nostalgic_morse
        nostalgic_morse        
    ```
 
## Build your own images

* [Build your own images](https://docs.docker.com/engine/userguide/containers/dockerimages/)

* Each time you’ve used docker run you told it which image you wanted.
* If an image isn’t already present on the host then it’ll be downloaded from a registry: by default the [Docker Hub Registry](https://registry.hub.docker.com/) .

### Listing images on the host

* `$ docker images`
    ```
        $ docker images
        REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
        ubuntu              14.04               1d073211c498        3 days ago          187.9 MB
        busybox             latest              2c5ac3f849df        5 days ago          1.113 MB
        training/webapp     latest              54bb4e8718e8        5 months ago        348.7 MB    
    ```
    
    * *REPOSITORY* : What repository they came from
    * *TAG* : The tags for each image
    * *ID* : The image ID of each image.
* A repository potentially holds multiple variants of an image.
* Each variant is identified by a tag and you can refer to a tagged image like so: `ubuntu:14.04`
* If you don’t specify a variant, for example you just use `ubuntu` , then Docker will default to using the `ubuntu:latest` image.

### Getting a new image

* If you want to pre-load an image you can download it using the `docker pull` command. 
    `$ docker pull centos`


### Finding images

* You can search these images on the [Docker Hub](https://hub.docker.com/) website.
* You can also search for images on the command line using the `docker search` command.
    `$ docker search sinatra`
    
* There are two types of images repositors :
    * *base-or-root-images* : 
        * These base images are provided by Docker Inc and are built, validated and supported. 
        * These can be identified by their single word names.
        * eg: *ubuntu* 
    * *user-images* :
        * A user image belongs to a member of the Docker community and is built and maintained by them.
        * You can identify user images as they are always prefixed with the user name
        * eg: *training/webapp*

### Pulling our image

* you can download it using the docker pull command
    `$docker pull training/webapp`
* The team can now use this image by running their own containers.
    `$ docker run -t -i training/sinatra /bin/bash`
    `root@a8cb6ce02d85:/#`


### Creating our own images

* you need to make some changes to the images that you downloaded.
* Thare are two ways you can update and create images
    * You can update a container created from an image and commit the results to an image.
    * You can use a Dockerfile to specify instructions to create an image.
    
#### Updating and committing an image

* To update an image you first need to create a container from the image you’d like to update.
    ```
    $ docker run -t -i training/sinatra /bin/bash
    root@0b2616b0e5a8:/#
    
    ```
    * Note the container ID that has been created, *0b2616b0e5a8*, we will need it later.
* Let's do some changes, add the *json* gem:
    `root@0b2616b0e5a8:/# gem install json`
    `root@0b2616b0e5a8:/# exit`
 
* You can then commit a copy of this container to an image using the `docker commit` command. 
    ```
    $ docker commit -m "Added json gem" -a "Kate Smith" \
    0b2616b0e5a8 ouruser/sinatra:v2
    4f177bd27a9ff0f6dc2a830403925b5360bfe0b93d476f7fc3231110e7f71b1c
    
    ```
    * *-m* : a commit message, a remark
    * *-a* : au author for the change
    * *0b2616b0e5a8* : specified the container you want to create this new image from
    * *ouruser* : consists of a new user, that you’re writing this image to. 
    * *sinatra* : keeping the original image name *sinatra*
    * *v2* : specifying a tag for the image: *v2* .
    
* You can look at our new *ouruser/sinatra* image using the `docker images` command.
    `$docker images`
* To use our new image to create a container you can then:
    ```
    $ docker run -t -i ouruser/sinatra:v2 /bin/bash
    root@78e82f680994:/#    
    ```

#### Building an image from a Dockerfile

* Using the `docker commit` command is a pretty simple way of extending an image
    * but it’s a bit cumbersome
    * and it’s not easy to share a development process for images amongst a team. 
* Instead you can use a new command, `docker build`, to build new images from scratch.
    * First, create a directory and a *Dockerfile* .
    ```
        $ mkdir sinatra
        $ cd sinatra
        $ touch Dockerfile
        
        # This is a comment
        FROM ubuntu:14.04
        MAINTAINER Kate Smith <ksmith@example.com>
        RUN apt-get update && apt-get install -y ruby ruby-dev
        RUN gem install sinatra
    ```
        * Each instruction creates a new layer of the image. 
        * Try a simple example now for building your own Sinatra image for your fictitious development team.
        
    * Use the docker build command to build an image.
        `$ docker build -t ouruser/sinatra:v2 .`


### Setting tags on an image

* You can also add a tag to an existing image after you commit or build it.
    `$ docker tag 5db5f8471261 ouruser/sinatra:devel`
    * The docker tag command takes the *ID* of the image, here 5db5f8471261, and our *user-name* , the *repository-name* and the *new-tag* .
    
* see your new tag using the `docker images` command.
    `$docker images`

### Image Digests

* Images that use the v2 or later format have a content-addressable identifier called a *digest* .
* As long as the input used to generate the image is unchanged, the digest value is predictable. 
* To list image digest values, use the *--digests* flag:
    `$ docker images --digests | head`
 
### Push an image to Docker Hub

* Once you’ve built or created a new image you can push it to Docker Hub using the `docker push` command. 
    ```
    $ docker push ouruser/sinatra
    The push refers to a repository [ouruser/sinatra] (len: 1)
    Sending image list
    Pushing repository ouruser/sinatra (3 tags)
    
    ```
    
### Remove an image from the host

* You can also remove images on your Docker host in a way similar to containers using the `docker rmi` command.
    * Delete the *training/sinatra* image as you don’t need it anymore.
    `$ docker rmi training/sinatra`

* If the container was running/stoped, use `docker rm` to remove the container first.
    `$ docker rm CONTAINER-ID`
    
## Network containers

* This section teaches you how to network your containers.

### Name a container

* Each container you create has an *automatically* created *name* ;
* You can also name containers yourself

* This naming provides two useful functions:
    * You can name containers that do specific functions in a way that makes it easier for you to remember them, 
        * for example naming a container containing a web application *web* .
    * Names provide Docker with a reference point that allows it to refer to other containers. 
        * There are several commands that support this and you’ll use one in an exercise later.
        
* You name your container by using the *--name* flag, 
    * for example launch a new container called *web* :
        `$ docker run -d -P --name web training/webapp python app.py`
    * Use the `docker ps` command to see check the name:
        `$ docker ps -l`
    * You can also use `docker inspect` with the container’s name.
        `$ docker inspect web`
        
* Container names must be unique. That means you can only call one container *web* .
* If you want to re-use a container name you must delete the old container
    ```
        $ docker stop web
        web
        $ docker rm web
        web    
    ```

### Launch a container on the default network

* Docker includes support for networking containers through the use of *network-drivers* .

* By default, Docker provides two network drivers for you
    * *bridge*
    * *overlay*
    
* Every installation of the Docker Engine automatically includes three default networks. You can list them:
    ```
        $ docker network ls
        NETWORK ID          NAME                DRIVER
        18a2866682b8        none                null                
        c288470c46f6        host                host                
        7b369448dccb        bridge              bridge  
    
    ```
    
* The network named *bridge* is a special network.
    * Unless you tell it otherwise, Docker always launches your containers in this network. Try this now:
    `$ docker run -itd --name=networktest ubuntu`
    
* Inspecting the network is an easy way to find out the container’s IP address.
    `$ docker network inspect bridge`
    
* You can remove a container from a network by disconnecting the container. 
    * To do this, you supply both the network name and the container name. 
    * You can also use the container id. But though, the name is faster.
    `$ docker network disconnect bridge networktest`
    

### Create your own bridge network

* Docker Engine natively supports both *bridge* networks and *overlay* networks. 
* A *bridge* network is limited to a *single-host* running Docker Engine. 
    * An *overlay* network can include *multiple-hosts* and is a more advanced topic. 

* For this example, you’ll create a bridge network:
    `$ docker network create -d bridge my-bridge-network`
    * *-d* : tells Docker to use the *bridge* driver for the new network.
        * You could have left this flag off as bridge is the default value for this flag. 
    * list the networks on your machine:
    `$ docker network ls`
    
    * If you inspect the network, you’ll find that it has nothing in it.
        `$ docker network inspect my-bridge-network`
        
    

### Add containers to a network

* To build web applications that act in concert but do so securely, create a network. 
* Networks, by definition, provide complete isolation for containers. 
* You can add containers to a network WHEN YOU FIRST RUN A CONTAINER.
    * Launch a container running a PostgreSQL database and pass it the *--net=my-bridge-network* flag to connect it to your new network:
        `$ docker run -d --net=my-bridge-network --name db training/postgres`
        
    * If you inspect your *my-bridge-network* you’ll see it has a container attached.  
    * You can also inspect your container to see where it is connected:
        `$ docker inspect --format='{{json .NetworkSettings.Networks}}'  db`
            `{"my-bridge-network": ...}`
        
* Now, go ahead and start your by now familiar *web* application. This time leave off the *-P* flag and also don’t specify a network.
    `$ docker run -d --name web training/webapp python app.py`
    * Which network is your web application running under? 
        `$ docker inspect --format='{{json .NetworkSettings.Networks}}'  web`
            `{"bridge": ...}`
    * Then, get the IP address of your *web* :
        `$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web`
            `172.17.0.2`
            
* Now, open a shell to your running db container:
    ```
        $ docker exec -it db bash
        root@a205f0dd33b2:/# ping 172.17.0.2
        ping 172.17.0.2
        PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
        ^C
        --- 172.17.0.2 ping statistics ---
        44 packets transmitted, 0 received, 100% packet loss, time 43185ms
    ```
    * you’ll find the ping failed. That is because the two container are running on different networks.
    * You can fix that.

* Docker networking allows you to *attach* a container to as many networks as you like. 
    * You can also attach an already running container. 
    * Go ahead and attach your running *web* app to the *my-bridge-network* .
        `$ docker network connect my-bridge-network web`
        
    * Try ping again
        ```
            $ docker exec -it db bash
            root@a205f0dd33b2:/# ping web
            PING web (172.18.0.3) 56(84) bytes of data.
            64 bytes from web (172.18.0.3): icmp_seq=1 ttl=64 time=0.095 ms
            64 bytes from web (172.18.0.3): icmp_seq=2 ttl=64 time=0.060 ms
            64 bytes from web (172.18.0.3): icmp_seq=3 ttl=64 time=0.066 ms
            ^C
            --- web ping statistics ---
            3 packets transmitted, 3 received, 0% packet loss, time 2000ms
            rtt min/avg/max/mdev = 0.060/0.073/0.095/0.018 ms
        
        ```
        * Note : `ping web`
    
        * You can try again to gain the *web* and *db* IPAddress and ping it.
        
## Manage data in containers
    * [Manage data in containers](https://docs.docker.com/engine/userguide/containers/dockervolumes/)
        
### Data volumes

* A data volume is a specially-designated directory within one or more containers that bypasses the [Union File System](https://docs.docker.com/engine/reference/glossary/#union-file-system). 
* Data volumes provide several useful features for persistent or shared data:
    * Volumes are initialized when a container is created.
        * If the container’s base image contains data at the specified mount point, that existing data is copied into the new volume upon volume initialization. 
        * Note that this does not apply when [mounting a host directory](https://docs.docker.com/engine/userguide/containers/dockervolumes/#mount-a-host-directory-as-a-data-volume) .
    * Data volumes can be shared and reused among containers.
    * Changes to a data volume are made directly.
    * Changes to a data volume will not be included when you update an image.
    * Data volumes persist even if the container itself is deleted.
    
* Data volumes are designed to persist data, independent of the container’s life cycle. 
* Docker therefore never automatically deletes volumes when you remove a container, nor will it “garbage collect” volumes that are no longer referenced by a container.

#### Adding a data volume

* You can add a data volume to a container using the *-v* flag with the `docker create` and `docker run` command.
* You can use the *-v* multiple times to mount multiple data volumes. 
* Let’s mount a single volume now in our web application container.
    `$ docker run -d -P --name web -v /webapp training/webapp python app.py`
    * This will create a new volume inside a container at */webapp* .

* You can also use the *VOLUME* instruction in a *Dockerfile* to add one or more new volumes to any container created from that image.

#### Locating a volume

* You can locate the volume on the host by utilizing the `docker inspect` command.
    `$ docker inspect web`
    * The output will provide details on the container configurations including the volumes. 
        ```
            ...
            Mounts": [
                {
                    "Name": "fac362...80535",
                    "Source": "/var/lib/docker/volumes/fac362...80535/_data",
                    "Destination": "/webapp",
                    "Driver": "local",
                    "Mode": "",
                    "RW": true,
                    "Propagation": ""
                }
            ]
            ...
        
        ```
        * *Source* is specifying the location on the host
        * *Destination* is specifying the volume location inside the container. 
        * *RW* shows if the volume is read/write.
    
    
    
#### Mount a host directory as a data volume

* In addition to creating a volume using the *-v* flag you can also mount a directory from your Docker daemon’s host into a container.
    `$ docker run -d -P --name web -v /src/webapp:/opt/webapp training/webapp python app.py`
    * */src/webapp* : the host directory, *host-dir*
    * */opt/webapp* : the container directory, *container-dir*
        * If the path */opt/webapp* already exists inside the container's image
            * the */src/webapp* mount overlays but does not remove the pre-existing content.
            * Once the mount is removed, the content is accessible again.
    * *container-dir* must always be an absolute path such as */src/docs*
    * *host-dir* can either be an *absolute-path* or a *name-value* .
        * If you supply an *absolute-path* for the *host-dir* , Docker bind-mounts to the path you specify
            * An absolute path starts with a */* (forward slash).
            * */foo* , Docker creates a bind-mount
            
        * If you supply a *name-value* , Docker creates a named volume by the *name* 
            * A *name-value* must start with an alphanumeric character, 
            * followed by a-z0-9, _ (underscore), . (period) or - (hyphen).
            * *foo* , Docker creates a named volume
    
*  mount files or directories on OS X
    `docker run -v /Users/<path>:/<container path> ...`
* On Windows, mount directories using:
    `docker run -v /c/Users/<path>:/<container path> ...`
    
* Mounting a host directory can be useful for testing. 
    * you can mount source code inside a container.
    * Then, change the source code and see its effect on the application in real time.
    * The directory on the host must be specified as an absolute path
        * if the directory doesn’t exist Docker will automatically create it for you.
        * This auto-creation of the host path has been deprecated.
        
* Docker volumes default to mount in read-write mode, but you can also set it to be mounted read-only.
    `$ docker run -d -P --name web -v /src/webapp:/opt/webapp:ro training/webapp python app.py`

#### Volume labels
#### Mount a host file as a data volume

* The *-v* flag can also be used to mount a single file - instead of just directories - from the host machine.
    `$ docker run --rm -it -v ~/.bash_history:/root/.bash_history ubuntu /bin/bash`

### Creating and mounting a data volume container

* If you have some persistent data that you want to share between containers, or want to use from non-persistent containers, 
    * it’s best to create a named Data Volume Container, and then to mount the data from it.
    
* Let’s create a new named container with a volume to share.
    * While this container doesn’t run an application, 
    * it reuses the training/postgres image
    * so that all containers are using layers in common, saving disk space.
    
        `$ docker create -v /dbdata --name dbstore training/postgres /bin/true`
    
    * You can then use the *--volumes-from* flag to mount the */dbdata* volume in another container.
        `$ docker run -d --volumes-from dbstore --name db1 training/postgres`
    * And another:
        `$ docker run -d --volumes-from dbstore --name db2 training/postgres`
        
        * In this case, if the *postgres* image contained a directory called */dbdata* then mounting the volumes from the *dbstore* container hides the */dbdata* files from the *postgres* image. The result is only the files from the *dbstore* container are visible.
        
* If you remove containers that mount volumes, including the initial dbstore container, or the subsequent containers db1 and db2, the volumes will not be deleted. 
* To delete the volume from disk, you must explicitly call `docker rm -v` against the last container with a reference to the volume. 

> Docker will not warn you when removing a container without providing the *-v* option to delete its volumes.
> If you remove containers without using the -v option, you may end up with “dangling” volumes; volumes that are no longer referenced by a container.
> You can use `docker volume ls -f dangling=true` to find dangling volumes
> and use `docker volume rm <volume name>` to remove a volume that’s no longer needed.

### Backup, restore, or migrate data volumes

* Another useful function we can perform with volumes is use them for backups, restores or migrations. 
* We do this by using the *--volumes-from* flag to create a new container that mounts that volume
    `$ docker run --rm --volumes-from dbstore -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /dbdata`
    
    * Here we’ve launched a new container and mounted the volume from the *dbstore* container.
    * We’ve then mounted a local host directory as */backup* . 
    * Finally, we’ve passed a command that uses *tar* to backup the contents of the *dbdata* volume to a *backup.tar* file inside our */backup* directory. 
    * When the command completes and the container stops we’ll be left with a backup of our *dbdata* volume.
    
* You could then restore it to the same container, or another that you've made elsewhere.
    * Create a new container
        `$ docker run -v /dbdata --name dbstore2 ubuntu /bin/bash`
    * Then un-tar the backup file in the new container’s data volume.
        `$ docker run --rm --volumes-from dbstore2 -v $(pwd):/backup ubuntu bash -c "cd /dbdata && tar xvf /backup/backup.tar --strip 1"`
        
* You can use the techniques above to automate backup, migration and restore testing using your preferred tools.

### Important tips on using shared volumes

* Multiple containers can also share one or more data volumes. 
* However, multiple containers writing to a single shared volume can cause data corruption. 
    * Make sure your applications are designed to write to shared data stores.
    
* Data volumes are directly accessible from the Docker host. 
    * This means you can read and write to them with normal Linux tools. 
    * In most cases you should not do this as it can cause data corruption if your containers and applications are unaware of your direct access.
    
    
    

## Legacy container links

    
## Using Supervisor with Docker


* Traditionally a Docker container runs a single process when it is launched, for example an Apache daemon or a SSH server daemon. 
* Often though you want to run more than one process in a container. 

* Using [Supervisor](http://supervisord.org/) allows us to better control, manage, and restart the processes we want to run. 

* To demonstrate this we’re going to install and manage both an *SSH* daemon and an *Apache* daemon.

### Creating a Dockerfile

* Let’s start by creating a basic *Dockerfile* for our new image.
    ```
        FROM ubuntu:13.04
        MAINTAINER examples@docker.com    
    ```
    
### Installing Supervisor

* Install our *SSH* and *Apache* daemons as well as *Supervisor* in our container.
    ```
        RUN apt-get update && apt-get install -y openssh-server apache2 supervisor
        RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor
    
    ```

### Adding Supervisor’s configuration file

* Now let’s add a configuration file for *Supervisor* . The default file is called *supervisord.conf* and is located in */etc/supervisor/conf.d/* .
    `COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf`
    
* *supervisord.conf* 
    ```
        [supervisord]
        nodaemon=true

        [program:sshd]
        command=/usr/sbin/sshd -D

        [program:apache2]
        command=/bin/bash -c "source /etc/apache2/envvars && exec /usr/sbin/apache2 -DFOREGROUND"    
    ```
    * The *supervisord.conf* configuration file contains directives that configure Supervisor and the processes it manages. 
    * `[supervisord]` : provides configuration for Supervisor itself
        * *nodaemon* : tells Supervisor to run interactively rather than daemonize.
    * The next two blocks manage the services we wish to control.
        *  Each block controls a separate process.
        * The blocks contain a single directive, 
            * *command* : which specifies what command to run to start each process.
            
### Exposing ports and running Supervisor

* Now let’s finish our *Dockerfile* by 
    * exposing some required ports 
    * and specifying the *CMD* instruction to start Supervisor when our container launches.
    ```
        EXPOSE 22 80
        CMD ["/usr/bin/supervisord"]
    
    ```

### Building our image

* We can now build our new image.
    `$ docker build -t <yourname>/supervisord .`
    
    
### Running our Supervisor container

* Once We’ve got a built image we can launch a container from it.
    ```
        $ docker run -p 22 -p 80 -t -i <yourname>/supervisord
        2013-11-25 18:53:22,312 CRIT Supervisor running as root (no user in config file)
        2013-11-25 18:53:22,312 WARN Included extra file "/etc/supervisor/conf.d/supervisord.conf" during parsing
        2013-11-25 18:53:22,342 INFO supervisord started with pid 1
        2013-11-25 18:53:23,346 INFO spawned: 'sshd' with pid 6
        2013-11-25 18:53:23,349 INFO spawned: 'apache2' with pid 7
        . . .
    
    ```
    * We’ve specified the *-p* flag to expose ports 22 and 80. 
        * From here we can now identify the exposed ports and connect to one or both of the SSH and Apache daemons.

    
# Links
-[]  [What is Docker?](https://www.docker.com/what-docker)
-[]  [Understand the architecture](https://docs.docker.com/engine/understanding-docker/)
-[]  [5分钟弄懂Docker](http://www.csdn.net/article/2014-07-02/2820497-what's-docker)
-[]  [Get Started with Docker Engine for Linux](https://docs.docker.com/linux/)
-[]  [Get Started with Docker for Windows](https://docs.docker.com/windows/)
-[]  [Get Started with Docker for Mac OS X](https://docs.docker.com/mac/)
-[]  [Sean's Notes Docker blog](http://seanlook.com/tags/docker/)
-[]  [Docker常用命令](http://blog.csdn.net/we_shell/article/details/38368137)
-[]  [Docker run reference](https://docs.docker.com/engine/reference/run/)
-[]  [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

-[]  [瓜哥blog - Docker](http://glovee.net/category/docker)

-[]  [Docker —— 从入门到实践](https://www.gitbook.com/book/yeasy/docker_practice)
-[] [Container Tutorials](http://containertutorials.com/index.html)

- [雪球的Docker实践](http://www.infoq.com/cn/articles/docker-in-xueqiu)
- [Docker三年回顾：梦想依在，人生正当年](http://www.infoq.com/cn/articles/docker-turns-3)
- [腾讯游戏是如何使用Docker的？](http://www.infoq.com/cn/articles/how-tencent-game-use-docker)

-[] [virtualenv 环境下 Nginx + Flask + Gunicorn+ Supervisor 搭建 Python Web](http://www.cnblogs.com/oneapm/p/4648445.html)
-[] [virtualenv 环境下 Nginx + Flask + Gunicorn+ Supervisor 搭建 Python Web](http://www.jianshu.com/p/be9dd421fb8d)
-[] [Flask + Gunicorn + Nginx 部署](http://www.cnblogs.com/Ray-liang/p/4837850.html)
-[] [使用Nginx、Gunicorn和Supervisor部署Flask应用](http://puras.me/2015/01/21/deploy-flask-using-nginx-gunicorn-supervisor/)
-[] [VPS环境搭建详解 (Virtualenv+Gunicorn+Supervisor+Nginx)](http://beiyuu.com/vps-config-python-vitrualenv-flask-gunicorn-supervisor-nginx)
-[] [(带测试) virtualenv 环境下 Django + Nginx + Gunicorn+ Supervisor 搭建 Python Web](http://www.unjeep.com/q/92981822.htm)
-[] []()

# Question & Answer
 
* `$ sudo docker pull ubuntu:12.04`
    * = `$ sudo docker pull registry.hub.docker.com/ubuntu:12.04`
        * Download the *12.04* tagged image from the *ubuntu* repository on the registry server *registry.hub.docker.com* 
    
* `$ sudo docker pull dl.dockerpool.com:5000/ubuntu:12.04`
    * from the special server download the image.

* `unable to prepare context: unable to evaluate symlinks in Dockerfile path: lstat`
    * original: `$ docker build -t xxx .`
    * worked: `$ docker build -t xxx --fiel ./Dockerfile .`
    * Maybe I run the *build* command in another path, not in the *Dockerfile* Folder.
    

* `docker cp <containerId>:/file/path/within/container /host/path/target`
    * copy files inside container to host path

    
* 做了多次试验之后，再重新运行一个新的容器，发现不能自容器内部访问外网
    * 纠结许久之后，重启docker 服务问题解决。
        `$ sudo systemctl restart docker`

* In Dockerfile文件中， *ADD* 与 *COPY* 的区别
    * *ADD* : The *ADD* instruction copies new files, directories or remote file URLs from `<src>` and adds them to the filesystem of the container at the path `<dest>`. [ADD](https://docs.docker.com/engine/reference/builder/#add)
    * *COPY* : The *COPY* instruction copies new files or directories from `<src>` and adds them to the filesystem of the container at the path `<dest>`. [COPY](https://docs.docker.com/engine/reference/builder/#copy)
    
    
* Docker 
    `RUN python -c "import numpy, scipy, pandas, matplotlib, matplotlib.pyplot, sklearn, seaborn, statsmodels, theano"`
    * bash: `nohup ipython notebook -c 'from Check.check import *'`
    
    
    
    