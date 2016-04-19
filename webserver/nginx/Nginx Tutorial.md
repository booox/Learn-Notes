# Nginx Tutorial

* [Installing Nginx](#install)
* [Starting Nginx](#start)
    *   [Check if Nginx is Runing] (#check)
* [Restarting Nginx](#restart)
* [The Nginx Configuration File](#config_file)
    *   [Original Configuration File Example] (#example)
* [Configuring Nginx](#configuring)
    *   [Configuring Nginx as Reverse Proxy With SSL / HTTPS] (#ssl)
    *   [Concatenate Certificates Into One File] (#certficate)


* * *

<h2 id="install">Installing Nginx</h2>

You can install Nginx on Ubuntu using the *apt-get* package manager, like this:

>   `apt-get install nginx`

<h2 id="start">Starting Nginx</h2>

>   `/etc/init.d/nginx start`

<h3 id="check">Check if Nginx is Runing</h2>

>   `htop`

    look for "nginx master process" and "nginx worker process"

<h2 id="restart">Restarting Nginx</h2>

>   `/etc/init/nginx restart`

<h2 id="config_file">The Nginx Configuration File</h2>

>   `/etc/nginx/nginx.conf`

    Make a copy of the original config file before making changes to it.
    `cp /etc/init/nginx.conf /etc/nginx/nginx.conf.bak`
    
<h3 id="example">Original Configuration File Example</h2>

<h2 id="configuring">Configuring Nginx</h2>


<h3 id="ssl">Configuring Nginx as Reverse Proxy With SSL / HTTPS</h2>
<h3 id="certficate">Concatenate Certificates Into One File</h2>
