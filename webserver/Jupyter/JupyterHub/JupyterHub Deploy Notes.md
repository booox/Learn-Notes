
JupyterHub Deploy



# Links

* a multi-user Jupyter Notebook environment, on a single host using Docker: [jupyterhub-deploy-docker](https://github.com/jupyterhub/jupyterhub-deploy-docker)
* deploy JupyterHub on AWS using Ubuntu Trusty: [Deploying JupyterHub on AWS](https://github.com/jupyterhub/jupyterhub/wiki/Deploying-JupyterHub-on-AWS)
* JupyterHub for teaching with nbgrader: [JupyterHub for Teaching](http://jupyterhub-deploy-teaching.readthedocs.org/en/latest/)
    * [jupyterhub-deploy-teaching](https://github.com/booox/jupyterhub-deploy-teaching)
* JupyterHub is running on the host, and users are in containers: [jupyterhub-demo](https://github.com/minrk/jupyterhub-demo)
* []()


# Create a Docker Machine

* Use Docker Machine to provision a new host, or to connect to an existing host. 

## Provision a new host



## Connect to an existing host

* ref: [adding an existing docker host to docker machine : a few tips](https://blog.dahanne.net/2015/10/07/adding-an-existing-docker-host-to-docker-machine-a-few-tips/)

1. ȷ�����ԴӰ�װ *Docker-machine* �ļ������Windows��Mac����ͨ�� public key ���ӵ�Զ�̵�Docker����
    * ��Windows�ͻ��������� *SecureCRT* ������Կ��
        * �����»Ự����á��������������˿ڡ������û�������ѡ��PublicKey�������������ԡ�
        * ����������ļ���
        * ѡ����Կ���� ��RSA��
        * ����֪ͨ�����ע�ͣ���Ϊ��ѡ��
        * ������Կ���ȣ�1024
        * ������Կ
        * ѡ��OpenSSH��Կ��ʽ��������ɡ�
            * ˽Կ---Identity		��Կ----Identity.pub
    * ��Զ��Docker�����Ͽ��� SSH ����
        * ����SSH
            * `$ sudo vi /etc/ssh/sshd_config`
        * ����ssh����( *CentOS7* )
            * `$ sudo systemctl start sshd`
            * `$ sudo systemctl status sshd`
        * ��������ssh���ӵ��û�
            * `$ sudo useradd -m sshuser1`
            * `$ sudo passwd sshuser1`
            * `$ su - sshuser1`
            * `$ mkdir ~/.ssh`
            * `$ chmod 700 ~/.ssh`
            * `$ cd ~/.ssh`
    * ����Կ *Identity.pub* �ϴ���sshuser1�� *.ssh* Ŀ¼�У����޸�Ȩ��
        `$ wget ftp://***/Identity.pub ~/.ssh`
        `$ cat Identity.pub >> authorized_keys`
        `$ chmod 400 authorized_keys`
        
2. �������Զ��������ʹ�� *sudo* ��ȷ����������
    * */etc/sudoers*
    ```
        $ sudo visudo
        YOURUSERNAME ALL=(ALL) NOPASSWD:ALL  # Add this line    
    ```
    * ref: [unless this issue is closed](https://github.com/docker/machine/issues/1569)
    
3. ȷ��Զ�������� *Docker* �İ汾�밲װ *Docker-machine* �� *Docker* �İ汾��ͬ
    `$ docker -v`
    
4. ��Զ�������ϴ� *2376* �˿�
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
        
5. �� *Docker-machine* ���������Զ�� *Docker* ����
    ```
        $ docker-machine create -d generic \
        > --generic-ssh-user lunn \
        > --generic-ssh-key /c /Users/user_name/sec/Identity    # user_name�滻ΪWindows ϵͳ�ϵ��û���
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
    * ���ԣ�
    ```
        $ docker-machine ls
        NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
        centos7   -        generic      Running   tcp://192.168.92.61:2376            v1.11.0
        default   *        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.0
        dev       -        virtualbox   Running   tcp://192.168.99.101:2376           v1.11.0    
    ```
    * ���ӵ��½��� *centos7* ����.
        `$ eval "$(docker-machine env centos7)"`
        
    * �� *ls* һ��
    ```
        $ docker-machine ls
        NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
        centos7   *        generic      Running   tcp://192.168.92.61:2376            v1.11.0
        default   -        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.0
        dev       -        virtualbox   Running   tcp://192.168.99.101:2376           v1.11.0    
    ```

# Activate Docker Machine

* �������е� *docker* ��������ڽ��� *jupyterhub* ��Զ�������ϣ���� *jupyterhub* Ҫ������

* ���� *jupyterhub*
    `$ eval "$(docker-machin env jupyterhub)"`
    
* �鿴��������
    ```
        
    
        $ env|grep DOCKER

        DOCKER_HOST=tcp://10.0.0.10:2376
        DOCKER_MACHINE_NAME=jupyterhub
        DOCKER_TLS_VERIFY=1
        DOCKER_CERT_PATH=/Users/jtyberg/.docker/machine/machines/jupyterhub
    ```
    
* ��������Ƿ񼤻
    `$ docker-machine active`

# ����Docker����

* ʹ��Docker������ŵ��У�
    * ����������ֻ������������ϵ��������ܻ���ͨ��
    * ���ֽ�������������ͨ������������ͬһ�������ϵ�����
    
* ����һ������Ϊ *jupyterhub-network* ��Docker����
    `$ docker network create jupyterhub-network`
    * �������ǻ����� JupyterHub �� single-user Jupyter Notebook ��������������������ϡ�
    
    












