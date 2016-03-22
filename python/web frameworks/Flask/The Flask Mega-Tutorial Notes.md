# Links
* [May 9 2012
The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

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
    [x] $ pip install flask
    [] $ pip install flask-login
    [x] $ pip install flask-openid  
    [] $ pip install flask-mail
    [x] $ pip install flask-sqlalchemy
    [x] $ pip install sqlalchemy-migrate
    [x] $ pip install flask-whooshalchemy
    [x] $ pip install flask-wtf     
    [] $ pip install flask-babel
    [] $ pip install guess_language
    [] $ pip install flipflop
    [] $ pip install coverage

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
## Create view function
    * *app/views.py*
    ```
        @app.route('/')
        @app.route('/index')
        def index():
            return 'Hello World!'
    
    ```
## Create run.py
    * *run.py*
    ```
        #!env/bin/python
        from app import app
        app.run(debug=True)
    ```
    * Linux, OS X and Cygwin , change *run.py* executable file
        `$ chmod a+x run.py`
    * On Windows
        `> python run.py`
    * Run it.
        `$ ./run.py`
        
## Test it's OK
    * `http://localhost:5000`
    * `http://localhost:5000/index`
   
    

# Part II: Templates

## Why we need templates

* modify *app/view.py*
    ```
        from app import app

        @app.route('/')
        @app.route('/index')
        def index():
            user = {'nickname': 'Miguel'}  # fake user
            return '''
        <html>
          <head>
            <title>Home Page</title>
          </head>
          <body>
            <h1>Hello, ''' + user['nickname'] + '''</h1>
          </body>
        </html>
        '''    
    ```
* It's so ugly.

## Templates to the rescue
* *app/templates/index.html*
    ```
        <html>
          <head>
            <title>{{ title }} - microblog</title>
          </head>
          <body>
              <h1>Hello, {{ user.nickname }}!</h1>
          </body>
        </html>    
    ```
* *app/views.py*
    ```
        from flask import render_template
        from app import app

        @app.route('/')
        @app.route('/index')
        def index():
            user = {'nickname': 'Miguel'}  # fake user
            return render_template('index.html',
                                   title='Home',
                                   user=user)    
    ```
    * Note: `from flask import render_template`
* Under the covers, the *render_template* function invokes the **Jinja2** templating engine.
* Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments.

## Control statements in templates

* The Jinja2 templates also support control statements, given inside **{%...%}**.
* *app/templates/index.html*
    ```
        <html>
          <head>
            {% if title %}
            <title>{{ title }} - microblog</title>
            {% else %}
            <title>Welcome to microblog</title>
            {% endif %}
          </head>
          <body>
              <h1>Hello, {{ user.nickname }}!</h1>
          </body>
        </html>    
    ```
## Loops in templates
* The logged in user will want to see recent posts.
* To begin, we use our handy fake object trick to create some users and some posts to show.
* *app/views.py*
    ```
        def index():
            user = {'nickname': 'Miguel'}  # fake user
            posts = [  # fake array of posts
                { 
                    'author': {'nickname': 'John'}, 
                    'body': 'Beautiful day in Portland!' 
                },
                { 
                    'author': {'nickname': 'Susan'}, 
                    'body': 'The Avengers movie was so cool!' 
                }
            ]
            return render_template("index.html",
                                   title='Home',
                                   user=user,
                                   posts=posts)    
    ```
    
* *app/templates/index.html*
    ```
        <html>
          <head>
            {% if title %}
            <title>{{ title }} - microblog</title>
            {% else %}
            <title>Welcome to microblog</title>
            {% endif %}
          </head>
          <body>
            <h1>Hi, {{ user.nickname }}!</h1>
            {% if posts %}
                {% for post in posts %}
                <div><p>{{ post.author.nickname }} says: <b>{{ post.body }}</b></p></div>
                {% endfor %}
            {% endif %}
          </body>
        </html>    
    ```
    * `{{ for post in posts }}`
    
## Template inheritance
* At the top of the page we need to have a navigation bar.
* We can add a navigation bar to our *index.html* template. 
* But as our application grows, there will be more pages, and this nav bar will have be copied to all of them.
* And you will have to keep all these identical copies of the nav bar in sync.
* It could become a lot of work.

* We can use Jinja2's template inheritance feature.
* *app/templates/base.html*
    ```
        <html>
          <head>
            {% if title %}
            <title>{{ title }} - microblog</title>
            {% else %}
            <title>Welcome to microblog</title>
            {% endif %}
          </head>
          <body>
            <div>Microblog: <a href="/index">Home</a></div>
            <hr>
            {% block content %}{% endblock %}
          </body>
        </html>    
    ```
    
    * We use *block* control statement.
* Modify *index.html* template to **inherit** from *base.html*.
    * *app/templates/index.html*vi 
    ```
        {% extends "base.html" %}
        {% block content %}
            <h1>Hi, {{ user.nickname }}!</h1>
            {% for post in posts %}
            <div><p>{{ post.author.nickname }} says: <b>{{ post.body }}</b></p></div>
            {% endfor %}
        {% endblock %}    
    ```
    * The *extends* block establishes the inheritance link between the two templates, so that Jinja2 knows that when it needs to render *index.html*.

# Part III: Web Forms

## Configuration
* To handle our web forms we are going to use the *Flask-WTF* extension.
    * `$ pip install flask-wtf`
* Many Flask extensions require some amount of configuration.
* So we are going to setup a configuration file inside our root *microblog* folder.
* *microblog/config.py*
    ```
        WTF_CSRF_ENABLED = True
        SECRET_KEY = 'you-will-never-guess'    
    ```
    * *WTF_CSRF_ENABLED* - activates the *cross-site request forgery* prevention.(now it's enabled by default.)
    * *SECRET_KEY*  - only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate a form.
    
* Now that we have our config file, we need to tell Flask to read it and use it.
    * We can do this right after the Flask app object is created.
    * *app/__init__.py*
        ```
            from flask import Flask
            
            app = Flask(__name__)
            app.config.from_object('config')
            
            from app import views
        
        ```
## The user login form
* Web forms are represented in *Flask-WTF* as classes, subclass from base class *Form* .
* A form subclass simply defines the fields of the form as class variables.
* The login mechanism that we will support in our app is not the standard username/password type.
* We will have our users login using their [OpenID](http://openid.net/) .
    * OpenIDs have the benefit that the authentication is done by the provider of the OpenID
    * So we don't have to validate passwords, which makes our site more secure to our users.
* The OpenID login only requires one string, the so called OpenID.
* *app/forms.py* 
    ```
        from flask.ext.wtf import Form
        from wtforms import StringField, BooleanField
        from wtforms.validators import DataRequired

        class LoginForm(Form):
            openid = StringField('openid', validators=[DataRequired()])
            remember_me = BooleanField('remember_me', default=False)    
    
    ```
    * We imported the *Form* class, and the two form field classes that we need, *StringField* and *BooleanField* .
    * The *DataRequired* import is a validator.
    * The *DataRequired* validator simply checks that the field is not submitted empty.
        * There are many more validators included with *Flask-WTF* .
        
## Form templates
* We will also need a template that contains the HTML that produces the form. 
* the LoginForm class that we just created knows how to render form fields as HTML.
* we just need to concentrate on the layout.
* *app/templates/login.html* 
    ```
        <!-- extend from base layout -->
        {% extends "base.html" %}

        {% block content %}
          <h1>Sign In</h1>
          <form action="" method="post" name="login">
              {{ form.hidden_tag() }}
              <p>
                  Please enter your OpenID:<br>
                  {{ form.openid(size=80) }}<br>
              </p>
              <p>{{ form.remember_me }} Remember Me</p>
              <p><input type="submit" value="Sign In"></p>
          </form>
        {% endblock %}    
    ```
    * This template expects a form object instantiated from the form class we just defined stored in a template argument named *form* .
    * The *form.hidden_tag()* template argument will get replaced with a hidden field that implements the CSRF prevention that we enabled in the configuration. 
        * This field needs to be in all of your forms if you have *CSRF* enabled.
        * The good news is that Flask-WTF handles it for us.
        * We just need to make sure it is included in the form.
    * *{{form.field_name}}*
        * The actual fields of our form are rendered by the field objects.
        * We just need to refer to a *{{form.field_name}}* template argument in the place where each field should be inserted.
        * Some fields can take arguments. ( *{{form.openid(size=80)}}* )
    * Since we have not defined the submit button in the form class we have to define it as a regular field.
        * The submit field does not carry any data so it doesn't need to be defined in the form class.
## Form views

* The final step is to code a view function that renders the template.
* This is actually quite simple since we just need to pass a form object to the template.
* *app/views.py*
    ```
        from flask import render_template, flash, redirect
        from app import app
        from .forms import LoginForm

        # index view function suppressed for brevity

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            form = LoginForm()
            return render_template('login.html', 
                                   title='Sign In',
                                   form=form)    
    
    ```
* Now you can visit *http://localhost:5000/login* 
* We have not coded the part that accepts data yet, so pressing the submit button will not have any effect at this time.

## Receiving form data
* Another area where Flask-WTF makes our job really easy is in the handling of the submitted form data.
* Here is an updated version of our login view function that validates and stores the form data.
* *app/views.py*
    ```
        @app.route('/login', methods=['GET', 'POST'])
        def login():
            form = LoginForm()
            if form.validate_on_submit():
                flash('Login requested for OpenID="%s", remember_me=%s' %
                      (form.openid.data, str(form.remember_me.data)))
                return redirect('/index')
            return render_template('login.html', 
                                   title='Sign In',
                                   form=form)    
    ```
* The *validate_on_submit* method does all the form processing work.
    * When it return *True*: flash a message, and redirect to *index.html*
    * When it return *False*: render_template to *login.html* again.
* The *flash* function is a quick way to show a message on the next page presented to the user.     
    * In this case we will use it for debugging.
    * The *flash* function is also extremely useful on production servers to provide feedback to the user regarding an action.
* The flashed messages will not appear automatically in our page
    * We will add these messages to the base template.
    * *app/templates/base.html*
    ```
        <html>
          <head>
            {% if title %}
            <title>{{ title }} - microblog</title>
            {% else %}
            <title>microblog</title>
            {% endif %}
          </head>
          <body>
            <div>Microblog: <a href="/index">Home</a></div>
            <hr>
            {% with messages = get_flashed_messages() %}
              {% if messages %}
                <ul>
                {% for message in messages %}
                    <li>{{ message }} </li>
                {% endfor %}
                </ul>
              {% endif %}
            {% endwith %}
            {% block content %}{% endblock %}
          </body>
        </html>    
    ```
    * The technique to display the flashed message is hopefully self-explanatory.
    * One interesting property of flash messages is that once they requested through the *get_flashed_messages* function they are removed from the message list.
        * these messages appear in the first page requested by the user after the flash function is called, and then they disappear.
* The *redirect* function tells the client web browser to navigate to a different page instead of the one requested.

## Improving field validation
* When a field fails validation Flask-WTF adds a descriptive error message to the form object.
* These messages are available to the template, so we just need to add a bit of logic that renders them.
* *app/templates/login.html*
    ```
        <!-- extend base layout -->
        {% extends "base.html" %}

        {% block content %}
          <h1>Sign In</h1>
          <form action="" method="post" name="login">
              {{ form.hidden_tag() }}
              <p>
                  Please enter your OpenID:<br>
                  {{ form.openid(size=80) }}<br>
                  {% for error in form.openid.errors %}
                    <span style="color: red;">[{{ error }}]</span>
                  {% endfor %}<br>
              </p>
              <p>{{ form.remember_me }} Remember Me</p>
              <p><input type="submit" value="Sign In"></p>
          </form>
        {% endblock %}    
    ```
* As a general rule, any fields that have validators attached will have errors added under *form.field_name.errors* .
    * In our case we use *form.openid.errors* .

## Dealing with OpenIDs

* A number of major service providers on the Internet support OpenID authentication for their members.
* You already have a fee OpenIDs.
    * For example, if you have an account with Yahoo, you have an OpenID with them.
    * Likewise with AOL, Flickr, etc.
    
* To make it easier for users to login to our site with one of these commonly available OpenIDs
    * we will add links to a short list of them
    * so that the user does not have to type the OpenID by hand.
* We defining the list of OpenID providers in our config file.
    * *config.py*
    ```
    OPENID_PROVIDERS = [
        {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
        {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
        {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
        {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]    
    ```

* Now let's see how we use this array in our login view function:
    
    ```
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for OpenID="%s", remember_me=%s' %
                  (form.openid.data, str(form.remember_me.data)))
            return redirect('/index')
        return render_template('login.html', 
                               title='Sign In',
                               form=form,
                               providers=app.config['OPENID_PROVIDERS'])
    
    
    ```
    * Here we grab the configuration by looking it up in *app.config* with its key.
    * The array is then added to the *render_template* call as a template argument.
    
* Specify how we would like to render these provider links in our login template
    * *app/templates/login.html*
    ```
        <!-- extend base layout -->
        {% extends "base.html" %}

        {% block content %}
        <script type="text/javascript">
        function set_openid(openid, pr)
        {
            u = openid.search('<username>')
            if (u != -1) {
                // openid requires username
                user = prompt('Enter your ' + pr + ' username:')
                openid = openid.substr(0, u) + user
            }
            form = document.forms['login'];
            form.elements['openid'].value = openid
        }
        </script>
        <h1>Sign In</h1>
        <form action="" method="post" name="login">
            {{ form.hidden_tag() }}
            <p>
                Please enter your OpenID, or select one of the providers below:<br>
                {{ form.openid(size=80) }}
                {% for error in form.openid.errors %}
                  <span style="color: red;">[{{error}}]</span>
                {% endfor %}<br>
                |{% for pr in providers %}
                  <a href="javascript:set_openid('{{ pr.url }}', '{{ pr.name }}');">{{ pr.name }}</a> |
                {% endfor %}
            </p>
            <p>{{ form.remember_me }} Remember Me</p>
            <p><input type="submit" value="Sign In"></p>
        </form>
        {% endblock %}    
    ```



# Part IV: Database

## Running Python scripts from the command line

* Linux or OS X:
    * Give a script executable permission: `$ chmod a+x script.py`
        * The script has a *shebang* line, which points to the interpreter that should be used.
    * Executed script like this: `./script.py <arguments>`
* Windows:
    * `$ python script.py <arguments>`
    
## Databases in Flask

* We will use the *Flask-SQLAlchemy* extension to manage our application.    
    * This extension provides a wrapper for the *SQLAlchemy* project, which is an *Object Relational Mapper* or ORM.

## Migrations

## Configuration
* For our little application we will use a sqlite database.
    * The sqlite databases are the most convenient choice for small applications
    * as each database is stored in a single file and there is no need to start a database server.
* We have a couple of new configuration items to add to our config file.
* *config.py*
    ```
        import os
        basedir = os.path.abspath(os.path.dirname(__file__))

        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
        SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')    
    ```
    * The *SQLALCHEMY_DATABASE_URI* is required by the Flask-SQLAlchemy extension. This is the path of our database file.
    * The *SQLALCHEMY_MIGRATE_REPO* is the folder where we will store the SQLAlchemy-migrate data files.
    
* When we initialize our app we also need to initialize our database.
    * *app/__init__.py*
    ```
        from flask import Flask
        from flask.ext.sqlalchemy import SQLAlchemy

        app = Flask(__name__)
        app.config.from_object('config')
        db = SQLAlchemy(app)

        from app import views, models    
    ```
    * We created a *db* object that will be our database.
    * We also imported a new module called *models* .

## The database model
* There are three fields: *id* , *nickname* , *email* .
* *app/models.py*
    ```
        from app import db

        class User(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            nickname = db.Column(db.String(64), index=True, unique=True)
            email = db.Column(db.String(120), index=True, unique=True)

            def __repr__(self):
                return '<User %r>' % (self.nickname)    
    ```
    * The *__repr__* method tells Python how to print objects of this class. 
    * We will use this for debugging.

## Creating the database

* With the configuration and model in place we are now ready to create our database file.
* The SQLAlchemy-migrate package comes with command line tools and APIs to create databases in a way that allows easy updates in the future, so that is what we will use.
* I find the command line tools a bit awkward to use
    * so instead I have written my own set of little Python scripts that invoke the migration APIs.
* Here is a script that creates the database
* *db_create.py*
    ```
    #!venv/bin/python
    
    
    ```
    
* something error: *sqlalchemy.exc.OperationalError near sytax error* *detect unicode returns: %r*
    [SQLAlchemy Engine Configuration](http://docs.sqlalchemy.org/en/latest/core/engines.html)


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

