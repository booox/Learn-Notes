
> [fokkodriesprong/jupyterhub](https://hub.docker.com/r/fokkodriesprong/jupyterhub/~/dockerfile/)

```
FROM jupyter/jupyterhub

MAINTAINER Thomas Wiecki <thomas.wiecki@gmail.com>

# install with apt-get
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install npm nodejs nodejs-legacy wget locales git
    
# Install with conda
RUN conda update --quiet --yes conda && \
    conda install --quiet --yes numpy scipy pandas
    
# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN conda clean -y -t    


ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
EXPOSE 8000


```


> [tzaffi/edlab-jupyterhub](https://hub.docker.com/r/tzaffi/edlab-jupyterhub/~/dockerfile/)

