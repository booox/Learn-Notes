
* [Virtualenv Docs](https://virtualenv.pypa.io/en/latest/userguide.html)

# User Guide
## Usage

* `$ virtualenv ENV`
    * Where *ENV* is a directory to place the new virtual environment.
    * *ENV/lib/* and *ENV/include/* are created.
        * containing supporting library files for a new virtualenv python.
        * Packages installed in this environment will live under *ENV/lib/pythonX.X/site-packages/* .
    * *ENV/bin* is created, where ececutables live - noticeably a new python.
        * Thus running a script with `#!/path/to/ENV/bin/python` would run that script under this virtualenv's python.
        * `#!/usr/bin/env python` (???)
    * The crucial packages *pip* and *setuptools* are installed
        * Which allow other packages to be easily installed to the environment.
        * This associated pip can be run from *ENV/bin/pip* .
        
## activate script

* On Posix systems, this resides in */ENV/bin/* ,so you can run:
    ```
        $ source bin/activate
    ```
    * To undo these changes to your path, just run:
    ```
        $ deactivate
    ```
    
   