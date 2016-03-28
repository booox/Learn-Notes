


## Chapter 4. Web Forms

* *request.form* provides access to form data sumitted in **POST** requests.

### Install Flask-WTF
* The *Flask-WTF* extension makes working with web forms a much more pleasant experience.
    * This extension is a Flask integration wrapper around the framework-agnostic *WTForms* package.
* installed with *pip* 
    `(venv) $ pip install flask-wtf`
    

### Cross-Site Request Forgery (CSRF) Protection
* A *CSRF* attack occurs when a malicious website sends requests to a different website on which the victim is logged in.

* To implement CSRF protection, *Flask-WTF* needs the application to configure an encryption key.
* *root_folder/config.py*
    ```
        WTF_CSRF_ENABLED = True
        SECRET_KEY = 'you-will-never-guess'    
    ```
    * *WTF_CSRF_ENABLED* - activates the *cross-site request forgery* prevention.(now it's enabled by default.)
    * *SECRET_KEY*  - only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate a form.

    
* Now that we have our config file, we need to tell Flask to read it and use it.
    * We can do this right after the Flask app object is created.
    * *root_folder/app/__init__.py*
        ```
            from flask import Flask
            
            app = Flask(__name__)
            app.config.from_object('config')
            
            from app import views
        
        ```

### Form Classes
* Form class definition
    * *app/forms.py* 
    ```
    from flask.ext.wtf import Form
    from wtforms import StringField, SubmitField
    from wtforms.validators import Required
    
    class NameForm(Form):
        name = StringField('What is your name?', validators=[Required()])
        submit = SubmitField('Submit'


    ```

### HTML Rendering of Forms
    * *app/templates/hello.html*

    ```
    {% extends "base.html" %}
    {% import "bootstrap/wtf.html" as wtf %}
    {% block title %}Flasky{% endblock %}
    {% block page_content %}
    <div class="page-header">
        <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
    </div>
    {{ wtf.quick_form(form) }}
    {% endblock %}
    
    ```

### Form Handling in View Functions
    * *app/views.py*
    ```
    from .forms import NameForm
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        name = None
        form = NameForm()
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''
        return render_template('index.html', form=form, name=name)
    
    
    ```


### Redirects and User Sessions
#### Problem One: POST as a last request
* Now the *hello.py* has a usability problem.
    * If you enter your name and submit it and then click the refresh button on your browser
    * you will likely get an obscure warning that asks for confirmation before submitting the form again.
* This happens because browsers repeat the last request they have sent when they are asked to refresh the page.
* When the last request sent is a *POST* request with form data, a refresh would cause a duplicate form submission
    * which in almost all cases is not the desired action
* Many users do not understand the warning from the browser. 
    * For this reson, it is considered good practice for web applications to 
    * NEVER LEAVE A *POST* REQUEST AS A LAST REQUEST SENT BY THE BROWSER.
* This practice can be achieved by responding to *POST* requests with a *redirect* instead of a normal response.
    * *Post/Redirect/Get* pattern

#### Problem Two: 
* When the application handles the *POST* request, it has access to the name entered by the user in *form.name.data*
    * but as soon as that request ends the form data is lost.
* Because the *POST* request is handled with a redirect, the application needs to store the name 
    * so that the redirected request can have it and use it to build the actual response.

#### Session
* Applications can "remember" things from one request to the next by storing them in the *user* *session*.
* By default, user sessions are stored in client-side cookies that are cryptographiclly signed using the configured *SECRET_KEY*

#### Redirects and user sessions
    ```
    from flask import Flask, render_template, session, redirect, url_for
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = NameForm()
        if form.validate_on_submit():
            session['name'] = form.name.data
            return redirect(url_for('index'))
        return render_template('index.html', form=form, name=session.get('name'))
    ```
* the *name* variable is now placed in the user sessions as *session['name']*
    * so that it is remembered beyond the request.
    
### Message Flashing

* Sometimes it is useful to give the user a status update after a request is completed.
    * This could be a confirmation message, a warning, or an error.
* Flask includes this functionality as a core feature.
    * *flash()* function can be used for this purpose.
* Flashed message
    * *app/views.py*
    ```
        from flask import Flask, render_template, session, redirect, url_for, flash
        @app.route('/', methods=['GET', 'POST'])
        def index():
            form = NameForm()
            if form.validate_on_submit():
                old_name = session.get('name')
                if old_name is not None and old_name != form.name.data:
                    flash('Looks like you have changed your name!')
                session['name'] = form.name.data
                form.name.data = ''
                return redirect(url_for('index'))
            return render_template('index.html',
                form = form, name = session.get('name'))    
    ```

* Calling *flash()* is not enough to get messages displayed
    * the templates used by the application need to render these messages.
* The best place to render flashed messages is the base template, because that will enable messages in all pages.
* Flask makes a *get_flashed_messages()* function available to templates to retrieve the messages and render them.

* Flash message rendering
    * *app/templates/base.html*
        ```
        {% extends "bootstrap/base.html" %}
        
        {% block title %}Title Default{% endblock %}
        
        {% block navbar %}
        <div>
            <ul>
            	<li><a href="#">Home</a></li>
            	<li><a href="#">Img</a></li>
            	<li><a href="#">Voic</a></li>
            </ul>
        </div>
        {% endblock %}
        
        {% block content %}
        <div class="flash">
            {% for message in get_flashed_messages() %}
            <div class="alert alert-warning">
                <button type="button" class="close" data-dismiss="alert">&times;</button>
                {{ message }}
            </div>
            {% endfor %}
            
            {% block page_content %}{% endblock %}
        </div>
        {% endblock %}
    
        ```

    * `app/templates/hello.html`
    
    ```
        {% extends "base.html" %}
        
        {% import "bootstrap/wtf.html" as wtf %}
        
        {% block title %}Hello Page{% endblock %}
        
        {% block page_content %}
            {{ super() }}
            <div class="page-header">
                <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
            </div>
            {{ wtf.quick_form(form) }}
        {% endblock %}
    ```
    

## Chapter 5. Databases

## SQL Databases & NoSQL Databases



## Python Database Frameworks

* Python has packages for most database engines, both open source and commercial
    * Flask puts no restrictions on what database packages can be used
    * You can work with MySQL, Postgres, SQLite, Redis, MongoDB, or CouchDB if any of these is your favorite.
* And there are also a number of database abstraction layer packages
    * such as SQLAlchemy or MongoEngine that allow you to work at a higher level with regular Python objects
    * instead of database entities such as tables, documents, or query languages.
* The chosen database framework for the examples in this book will be *Flask-SQLAlchemy* .
    * The Flask extension wrapper for *SQLAlchemy* .

## Database Management with Flask-SQLAlchemy
* Flask-SQLAlchemy is a Flask extension that simplifies the use of SQLAlchemy inside Flask applications.
    * SQLAlchemy is a powerful relational database framework that supports several database backends.
    * It offers a high-level ORM and low level access to the database’s native SQL functionality.
### Install Flask-SQLAlchemy
* `(venv) $ pip install flask-sqlalchemy`

### Flask-SQLAlchemy database URLs
* In Flask-SQLAlchemy, a database is specified as a URL.
* The database URLs for the three most popular database engines.
    * *MySQL*  *mysql://username:password@hostname/database*
    * *Postgres*  *postgresql://username:password@hostname/database*
    * *SQLite(Unix)*  *sqlite:////absolute/path/to/database*
    * *SQLite(Windows)*  *sqlite:///c:/absolute/path/to/database*
    
* The URL of the application database must be configured as the key *SQLALCHEMY_DATABASE_URI* in the Flask configuration object.
* Another useful option is the configuration key *SQLALCHEMY_COMMIT_ON_TEARDOWN*
    * which can be set to **True** to enable automatic commits of database changes at the end of each request.

### Initialize and configure a simple SQLite database

* Database configuration
* *config.py*
    ```
        import os
        basedir = os.path.abspath(os.path.dirname(__file__))

        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
        SQLALCHEMY_COMMIT_ON_TEARDOWN = True
        # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')    
    ```
    * The *SQLALCHEMY_DATABASE_URI* is required by the Flask-SQLAlchemy extension. This is the path of our database file.
    * The *SQLALCHEMY_MIGRATE_REPO* is the folder where we will store the SQLAlchemy-migrate data files.
    * *SQLALCHEMY_COMMIT_ON_TEARDOWN* set to True to enable automatic commits of database changes at the end of each request.
    
* When we initialize our app we also need to initialize our database.
    * *app/__init__.py*
    ```
        from flask import Flask
        from flask.ext.sqlalchemy import SQLAlchemy

        app = Flask(__name__)
        app.config.from_object('config')
        db = SQLAlchemy(app)

        from app import views    
        from app import models    
    ```
    * We created a *db* object that will be our database.
    * We also imported a new module called *models* .
    * NOTICE: `from app import views` MUST be in the end of the script for the reason of circular reference.

## Model Definition
* There are three fields: *id* , *nickname* , *email* .
* *app/models.py*
    ```
        from app import db

        class Role(db.Model):
            __tablename__ = 'roles'
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(64), unique=True)

            def __repr__(self):
                return '<Role %r>' % (self.name)    
                
        class User(db.Model):
            __tablename__ = 'users'
            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(64), unique=True, index=True)
            
            def __repr__(self):
                return '<User %r>' % (self.username)
    ```
    * The *__tablename__* class variable defines the name of the table. 
    * Most common SQLAlchemy column types:
        * *Integer* , int, Regular integer, 32bits
        * *SmallInteger* , int, Short-range integer, 16bits
        * *BigInteger* , int or long, Unlimited precision integer
        * *Float* , float, Floating-point number
        * *Numeric* , decimal.Decimal, Fixed-point number
        * *String* , str
        * *Text* , str
        * *Unicode* , unicode
        * *UnicodeText* , unicode
        * *Boolean* , bool
        * *Date* , datetime.date
        * *Time* , datetime.time
        * *DateTime* , datetime.datetime
        * *Interval* , datetime.timedelta
        * *Enum* , str
        * *PickleType* , Any Python object
        * *LargeBinary* , str
    * Most common SQLAlchemy column options:
        * *primary_key*
        * *unique*      do not allow duplicate values
        * *index*       create an index for this column, so that queries are more efficient.
        * *nullable*    True: allow empty values for this column. False: not allow.
        * *default*     Define a default value for the column.
    * The *__repr__* method representation that tells Python how to print objects of this class. 
        * We will use this for debugging and testing
    
## Relationships
* This is a *one-to-many* relationshiop from roles to users
    * Because one role belongs to many users
    * And users have only one role.
* Relationships
    ```
    class Role(db.Model):
        # ...
        users = db.relationship('User', backref='role')
    class User(db.Model):
        # ...
        role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))    
    ```
    
* *app/models.py*
    ```
        from app import db

        class Role(db.Model):
            __tablename__ = 'roles'
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(64), unique=True)
            users = db.relationship('User', backref='role')

            def __repr__(self):
                return '<Role %r>' % (self.name)    
                
        class User(db.Model):
            __tablename__ = 'users'
            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(64), unique=True, index=True)
            role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
            
            def __repr__(self):
                return '<User %r>' % (self.username)
    ```

    * Common SQLAlchemy relationship options
        * *backref* : back reference
        * *primaryjoin* : 
        * P57

## Database Operations

* The best way to learn how to work with database models is in a Python shell.

### Creating the Tables
* The very first thing to do is to instruct Flask-SQLAlchemy to create a database based on the model classes.
* The *db.create_all()* function does this:
    ```
        (venv) $ python hello.py shell
        >>> from hello import db
        >>> db.create_all()
    ```
    * You will now see a new file there called *data.sqlite*
* The *db.create_all()* function will not re-create or update a database table if it already exists in the database.
    * The brute-force solution
        * remove the old tables first:
            ```
                >>> db.drop_all()
                >>> db.create_all()
            ```
    * A better solution:
        ```
        
        ```