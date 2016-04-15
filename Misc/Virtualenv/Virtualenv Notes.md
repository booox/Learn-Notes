# Virtualenv





* Check *virtualenv* installed:
    `$ virtualenv --version`
* Install *virtualenv*
    * Ubuntu
        `$ sudo apt-get install python-virtualenv`
    * CentOS
        `$ pip install virtualenv`
    * Mac OS X
        `$ sudo easy_install virtualenv`
    * Windows
        * first installed *pip* , and then: `pip install virtualenv`
        * OR: Using easy_install
            * Go to :  https://bitbucket.org/pypa/setuptools
            * Run:
                ```
                $ python ez_setup.py
                $ easy_install virtualenv                
                ```
* Create the Python virtual env
    `$ virtualenv venv`
    * Create a completely separate and isolated Python environment
        `$ virtualenv --no-site-packages venv`
    
    
* Create the Python virtual env
    `$ virtualenv venv`
    
* Activate the virtual env
    * Linux and Mac OS X
        `$ source venv/bin/activate`
    * Windows:
        `$ venv\Scripts\activate`
        
    * Note the activation prompt
        `(venv) $`
    * Exit the virtual env
        `$ deactivate`