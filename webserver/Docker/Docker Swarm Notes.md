Docker Swarm

# Docker Swarm overview

* ref: [Docker Swarm overview](https://docs.docker.com/swarm/overview/)

* Docker Swarm is native clustering for Docker.
* It turns a pool of Docker hosts into a single, virtual Docker host.
* Because Docker Swarm serves the standard Docker API, 
    * any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts.
    
## Understand Swarm cluster creation

* The first step to creating a Swarm cluster on your network is to pull the Docker Swarm image.
* Then, using Docker, you configure the Swarm manager and all the nodes to run Docker Swarm. 
* This method requires that you:
    * open a TCP port on each node for communication with the Swarm manager
    * install Docker on each node
    * create and manage TLS certificates to secure your cluster
    
    
    
# Get Started with Docker Swarm

* ref: [Get Started with Docker Swarm](https://docs.docker.com/swarm/install-w-machine/)
