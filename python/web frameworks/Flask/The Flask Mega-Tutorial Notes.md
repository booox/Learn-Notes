<h1>The Flask Mega-Tutorial</h1>

# Part I: Hello World!

## prepare the enviroments
* `$ mkdir microblog`
* `$ cd microblog`
* `$ virtualenv venv`   (已经安装过 *virtualenv* )
* `$ . venv/bin/activate`
## install Flask
* `(venv)$ pip install Flask`   (下面省略 *(venv)* )
### Linux, OS X or Cygwin
    ```
    $ pip install flask
    $ pip install flask-login
    $ pip install flask-openid
    $ pip install flask-mail
    $ pip install flask-sqlalchemy
    $ pip install sqlalchemy-migrate
    $ pip install flask-whooshalchemy
    $ pip install flask-wtf
    $ pip install flask-babel
    $ pip install guess_language
    $ pip install flipflop
    $ pip install coverage

    ```
    
### Windows
    ```
    $ pip install flask
    $ pip install flask-login
    $ pip install flask-openid
    $ pip install flask-mail
    $ pip install flask-sqlalchemy
    $ pip install sqlalchemy-migrate
    $ pip install flask-whooshalchemy
    $ pip install flask-wtf
    $ pip install flask-babel
    $ pip install guess_language
    $ pip install flipflop
    $ pip install coverage

    ```
## Create Directories
    ```
        $ mkdir app
        $ mkdir app/static
        $ mkdir app/templates
        $ mkdir tmp
    ```
    * *app* : put our application package
    * *static* : store static files like images, js, and css.
    * *templates* : where our templates will go.
## Create script for our "app" package
* *app/__init__.py*
    ```
    from flask import Flask
    
    app = Flask(__name__)
    from app import views
    
    ```
    

# Part II: Templates
# Part III: Web Forms
# Part IV: Database
# Part V: User Logins
# Part VI: Profile Page And Avatars
# Part VII: Unit Testing
# Part VIII: Followers, Contacts And Friends
# Part IX: Pagination
# Part X: Full Text Search
# Part XI: Email Support
# Part XII: Facelift
# Part XIII: Dates and Times
# Part XIV: I18n and L10n
# Part XV: Ajax
# Part XVI: Debugging, Testing and Profiling
# Part XVII: Deployment on Linux (even on the Raspberry Pi!)
# Part XVIII: Deployment on the Heroku Cloud

