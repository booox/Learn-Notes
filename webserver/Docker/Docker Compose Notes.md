Docker Compose

# Overview of Docker Compose
* [Overview of Docker Compose](https://docs.docker.com/compose/overview/)

* Compose is a tool for defining and running multi-container Docker applications.
* With Compose, you use a Compose file to configure your application's services.
* Then, using a single command, you create and start all the services from your configuration.

* Using Compose is basically a three-step process.
    1. Define your app's environement with a *Dockerfile* so it can be reproduced anywhere.
    2. Define the services that make up your app in *docker-compose.yml* so they can be run together in an isolated environement.
    3. Lastly, run `docker-compose up` and Compose will start and run your entire app.
    
* A *docker-compose.yml* looks like this:
    ```
        version: '2'
        services:
          web:
            build: .
            ports:
            - "5000:5000"
            volumes:
            - .:/code
            - logvolume01:/var/log
            links:
            - redis
          redis:
            image: redis
        volumes:
          logvolume01: {}
    
    ```

    
# Compose documentation

## Install Docker Compose

* You can run Compose on OS X, Windows and 64-bit Linux.
* To install it, you'll need to install Docker first.

* To install Compose, do the following:
    1. Install Docker Engine
    2. The Docker Toolbox installation includes both Engine and Compose
        * so Mac and Windows users are done installing.
        * Others should continue to the next step.
    3. Go to the [Compose repository release page on GitHub](https://github.com/docker/compose/releases)
    4. Use the following commands
        ```
            curl -L https://github.com/docker/compose/releases/download/1.7.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
            chmod +x /usr/local/bin/docker-compose
        ```
    5. Optionally, install command completion for the *bash* and *zsh* shell.
    6. Test the installation
        `$ docker-compose --version`
        
## Getting Started

* ref: [Getting Started](https://docs.docker.com/compose/gettingstarted/)

* On this section you build a simple Python web application running on Docker Compose.

* The application uses the *Flask* framework and increments a value in *Redis* .

### Prerequisites

* Make sure you have already installed both Docker *Engine* and Docker *Compose* .
* You don't need to install Python, it is provided by a Docker image.

#### Setup
1. Create a directory for the project:
    `$ mkdir composetest`
    `$ cd composetest`
2. Create a file called *app.py*:
    * *app.py* : 
    ```
        $ vi app.py
        from flask import Flask
        from redis import Redis

        app = Flask(__name__)
        redis = Redis(host='redis', port=6379)

        @app.route('/')
        def hello():
            redis.incr('hits')
            return 'Hello World! I have been seen %s times.' % redis.get('hits')

        if __name__ == "__main__":
            app.run(host="0.0.0.0", debug=True)
    
    ```
3. Create *requirements.txt*
    ```
        $ vi requirements.txt
        flask
        redis
    ```
    * These define the applications dependencies.
    
#### Create a Docker image

* In this step, you build a new Docker image. 
    * The image contains all the dependencies the Python application requires, 
    * including Python itself.
    
1. Create *Dockerfile*
    ```
        FROM python:2.7
        ADD . /code
        WORKDIR /code
        RUN pip install -r requirements.txt
        CMD python app.py
    ```
    * This tells Docker to:
        * Build an image starting with the Python 2.7 image.
        * Add the current directory *.* into the path */code* in the image.
        * Set the working directory to */code* .
        * Install the Python dependencies.
        * Set the default command for the container to python app.py

2. Build the image
    `$ docker build -t web .`
    
#### Define services

* Define a set of services using *docker-compose.yml*

1. Create *docker-compose.yml* in your project directory
    ```
        version: '2'
        services:
          web:
            build: .
            ports:
             - "5000:5000"
            volumes:
             - .:/code
            depends_on:
             - redis
          redis:
            image: redis
    ```
    
    * This Compose file defines two services, *web* and *redis*.
    * The *web* service:
        * Builds from the Dockerfile in the current directory.
        * Forwards the exposed port 5000 on the container to port 5000 on the host machine.
        * Mounts the project directory on the host to /code inside the container allowing you to modify the code without having to rebuild the image.
        * Links the web service to the Redis service.
    * The *redis* service uses the latest public *Redis* image pulled from the Docker Hub registry.
    
#### Build and run your app with Compose

1. From your project directory, start up your application.
    ```
        $ docker-compose up
    ```
    * Compose pulls a Redis image, 
    * builds an image for your code, 
    * and start the services you defined.
    
2. Enter *http://0.0.0.0:5000/* in a browser.
    * You should see a message in your browser saying:
        `Hello World! I have been seen 1 times.`
    * Refresh the page. The number should increment.
    
#### Experiment with some other commands

* run your services in the background
    ```
        $ docker-compose up -d
        Starting composetest_redis_1...
        Starting composetest_web_1...
        $ docker-compose ps
        Name                 Command            State       Ports
        -------------------------------------------------------------------
        composetest_redis_1   /usr/local/bin/run         Up
        composetest_web_1     /bin/sh -c python app.py   Up 
    ```
    
* The `docker-compose run` command allows you to run one-off commands for your services. 
    `$ docker-compose run web env`
    
* stop your services
    `$ docker-compose stop`
        

## Quickstart: Docker Compose and Django

* ref: [Quickstart: Docker Compose and Django](https://docs.docker.com/compose/django/)

### Define the project components

1. Create an empty project directory.
    ```
        $ mkdir djangotest
        $ cd djangotest
    ```
2. Create *Dockerfile*
    ```
        FROM python:2.7
        ENV PYTHONUNBUFFERED 1
        RUN mkdir /code
        WORKDIR /code
        ADD requirements.txt /code/
        RUN pip install -r requirements.txt
        ADD . /code/    
    ```
    
3. Create *requirements.txt*
    ```
        Django
        psycopg2
    ```
4. Create *docker-compose.yml* 
    * The *docker-compose.yml* file describes the services that make your app.
    ```
        version: '2'
        services:
          db:
            image: postgres
          web:
            build: .
            command: python manage.py runserver 0.0.0.0:8000
            volumes:
              - .:/code
            ports:
              - "8000:8000"
            depends_on:
              - db
    ```

### Create a Django project

1. Change to the root of your project directory
2. Create the Django project using the `docker-compose` command.
    `$ docker-compose run web django-admin.py startproject composeexample .`
    * This instructs Compose to run `django-admin.py startproject composeeexample` in a container, using the `web` service’s image and configuration. 
    * Because the `web` image doesn’t exist yet, Compose builds it from the current directory, as specified by the `build: .` line in `docker-compose.yml`.
    * Once the `web` service image is built, Compose runs it and executes the `django-admin.py startproject` command in the container.
    * This command instructs Django to create a set of files and directories representing a Django project.
    
3. List the contents of your project
    ```
        $ ls -l
        drwxr-xr-x 2 root   root   composeexample
        -rw-rw-r-- 1 user   user   docker-compose.yml
        -rw-rw-r-- 1 user   user   Dockerfile
        -rwxr-xr-x 1 root   root   manage.py
        -rw-rw-r-- 1 user   user   requirements.txt
    ```

### Connect the database

1. Edit *composeexample/settings.py* file:
    ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'postgres',
                'USER': 'postgres',
                'HOST': 'db',
                'PORT': 5432,
            }
        }
    
    ```
    * These settings are determined by the postgres Docker image specified in `docker-compose.yml`.
    
2. Run `docker-compose up` command:
    
3. Web Surf: `http://ip:8000`    
    Docker Machine Host: `$ docker-machine ip MACHINE_NAME`
    

























