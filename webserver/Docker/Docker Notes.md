


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

### Install with yum

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

#### Updating and committing an image

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


### Pulling our image
### Pulling our image
 

## Legacy container links

    

    
# Links
-[]  [What is Docker?](https://www.docker.com/what-docker)
-[]  [Understand the architecture](https://docs.docker.com/engine/understanding-docker/)
-[]  [5分钟弄懂Docker](http://www.csdn.net/article/2014-07-02/2820497-what's-docker)
-[]  [Get Started with Docker Engine for Linux](https://docs.docker.com/linux/)
-[]  [Get Started with Docker for Windows](https://docs.docker.com/windows/)
-[]  [Get Started with Docker for Mac OS X](https://docs.docker.com/mac/)
-[]  [Sean's Notes Docker blog](http://seanlook.com/tags/docker/)
-[]  [Docker常用命令](http://blog.csdn.net/we_shell/article/details/38368137)

-[]  [Docker —— 从入门到实践](https://www.gitbook.com/book/yeasy/docker_practice)
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