# Preface
## How to work with the Example Code

* Downloads a project and its entire version history
    `$ git clone https://github.com/miguelgrinberg/flasky.git`
    * download source code from Github into a *flasky* folder
    * that is created in the current directory
    
* Switches to the specified branch updateds the working directory
    `$ git checkout [branch-name]`
    `$ git checkout 1a`
    
* Redo Commits: 
    * Undoes all commits after [commit], preserving changes locally
        `$ git reset [commit]`
    * Discards all history and changes back to the specified commit
        `$ git reset --hard [commit]`

* Synchronize Changes
    * Downloads all history from the repository bookmark
        `$ git fetch [bookmark]`
    * Combines bookmark's branch into current local branch
        `$ git merge [bookmark]/[branch]`
    * Uploads all local branch commits to GitHub
        `$ git push [alias] [branch]`
    * Downloads bookmark history and incorporates changes
        `$ git pull`
        
        
    * Update the commit history and tags
        ```
        $ git fetch --all
        $ git fetch --tags
        $ git reset --hard origin/master
        
        ```
* Review History
    * Lists version history for the current branch
        `$ git log`
    * Lists version history for a file, including renames
        `$ git log --follow [file]`
    * Shows content differences between two branches
        `$ git diff [first-branch]...[second-branch]`
        `$ git diff 2a 2b`
    * Outputs metadata and content changes of the specified commit
        `$ git show [commit]`
        
# Part I. Introduction to Flask

## Chapter 1. Installation

### Using Virtual Environments
* Check *virtualenv* installed:
    `$ virtualenv --version`
* Install *virtualenv*
    * Ubuntu
        `$ sudo apt-get install python-virtualenv`
    * CentOS
        `$ yum install virtualenv` (?)
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
* Git Clone
    * Create a folder to host the example code
    * Git clone
        ```
            $ git clone https://github.com/miguelgrinberg/flasky.git
            $ cd flasky
            $ git checkout 1a
        
        ```
* Create the Python virtual env
    ```
        $ virtualenv venv
    
    ```
* Activate the virtual env
    * Linux and Mac OS X
        `$ source venv/bin/activate`
    * Windows:
        `$ venv\Scripts\activate`
        
    * Note the activation prompt
        `(venv) $`
    * Exit the virtual env
        `$ deactivate`
    
### Installing Python Packages with pip 
* Install Flask into the virtual env
    `(env) $ pip install Flask`
    * Verify Flask was installed correctly
        ```
            (env) $ python
            >>> import flask
            >>>
            
        ```
        
## Chapter 2: Basic Application Structure

### Initialization
* All Flask application must create an *application* *instance* .
* The web server passes all requests it receives from clients to this object for handling
* using a protocol called Web Server Gateway Interface (WSGI)
* The application instance is an object of class **Flask** :
    ```
        from flask import Flask
        app = Flask(__name__)
    ```
    * The only required argument to the Flask class constructor is
        * the name of the main module or package of the application.
### Routes and View Functions

* Routes:
    - Client Browser : 
        - send request to server
    - Web Server (WSGI): 
        - send the request to Flask Application Instance
    - Flask Application Instance
        - needs to know: what code need to run for each URL requested
        - keeps a mapping of URLs to Python functions
        - It is called a *route*
        - through the *app.route* decorator
    - Decorator : *@app.route*
        ```
            @app.route('/')
            def index():
                return '<h1>Hello World!</h1>'        
        ```
        - The previous example registers the function index() as the handler for the application¡¯s root URL
        - The return value of this function, called the *response* , is what the client receives.
        - Functions like *index()* are called *view* *functions* .
### View Functions

* Route can also has a dynamic name component
    * The dynamic components in routes are strings by default
    ```
        @app.route('/user/<name>')
        def user(name):
            return '<h1>Hello, %s!</h1>' % name
    
    ```
    * Also be defined with a type
        `@app.route('/user/<int:id>')`
* Flask supports types *int* , *float* , and path for routes.

### Server Startup
* The application instance has a *run* method that launches Flask's integrated development web server.
    ```
        if __name__ == '__main__':
            app.run(debug=True)
    ```
* Once the server starts up, it goes into a loop that waits for requests and services them.
    * This loop continues until the application is stopped, for example by hitting Ctrl-C.
    
### A Simple Complete Application
* A Simple Complete Application
    * *hello.py*
    ```
        from flask import Flask
        app = Flask(__name__)
        
        @app.route('/')
        def index():
            return '<h1>Hello World!</h1>'
            
        if __name__ == '__main__':
            app.run(debug=True)    
    ```
* To run the application, make sure that the *venv* is activated.
    * Linux : `$ . venv/bin/activate`
    * Windows : `> venv\Scripts\activate`
* To launch the application:
    ```
        (venv) $ python hello.py
         * Running on http://127.0.0.1:5000/
         * Restarting with reloader
    ```
* Open your web browser
    `localhost:5000` or `127.0.0.1:5000`

* Flask application with a dynamic route
    * *hello.py*
    ```
        from flask import Flask
        app = Flask(__name__)
        
        @app.route('/')
        def index():
            return '<h1>Hello World!</h1>'
            
        @app.route('/user/<name>')
        def user(name):
            return '<h1>Hello, %s!</h1>' % name
            
        if __name__ == '__main__':
            app.run(debug=True)
    
    ```
    * To test the dynamic route
        ` http://localhost:5000/user/Dave`

### The Request-Response Cycle
#### Application and Request Contexts
* Flask uses contexts to temporarily make certain objects globally accessible.
* View functions like the following one can be written
    ```
        from flask import request
        
        @app.route('/')
        def index():
            
            user_agent = request.headers.get('User-Agent')
            return '<p>Your browser is %s</p>' % user_agent
    
    ```
    * Note how in this view function request is used as if it was a global variable. 
    * In reality, *request* cannot be a global variable if you consider that in a multithreaded server
    * each thread needs to see a different object in *request* . 
    * *Contexts* enable Flask to make certain variables globally accessible to a thread without interfering with the other threads.
        * A  thread  is  the  smallest  sequence of  instructions  that can be managed independently.

* There are two contexts in Flask: 
    * the *application* *context*  
    * and the *request *context* . 
* Flask context globals
    * *current_app* : Application context - the active application
    * *g* : Application context - the application can use for temporary storage during the handling of a request
        * This variable is reset with each request
    * *request* : Request context - The request object, 
        * which encapsulates the contents of a HTTP request sent by the client.
    * *session* : Request context - The user session
        *  a dictionary that the application can use to store values that are ¡°remembered¡± between requests

#### Request Dispatching
* To see what the URL map in a Flask application looks like
* You can inspect the map created for *hello.py* in the Python shell.
    ```
        (venv) $ python
        >>> from hello import app
        >>> app.url_map
        Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
         <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
         <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])    
    ```
    * The */* and */user/<name>* routes were defined by the *app.route* decorators.
    * The *static/<filename>* route is a special route added by Flask to give access to static files.
    * The *HEAD* , *OPTIONS* , *GET* elements are the *request *methods that are handled by the route.
    
    
#### Request Hooks
* Sometimes it it useful to execute code before or after request is processed.
    * For example, at the start of each request it may be necessary to create a database connection
    * or authenticate the user making the request
* Instead of duplicating the code that does this in every view function
    * Flask gives you the option to register common functions 
    * to be invoked before or after a request is dispatched to a view function.
* Request hooks are implemented as decorators.
* There are four hooks supported by Flask:
    * *before_first_request* : Register a function to run before the first request is handled
    * *before_request* : Register a function to run before each request
    * *after_request* : Register a function to run after each request, if no unhandled exceptions occurred.
    * *teardown_request* : Register a function to run after each request, even if unhandled exceptions occurred.
* A common pattern to share data between request hook functions and view functions is to use the *g* context global.

    
#### Responses

* In most cases the response is a simple string that is sent back to the client as an HTML page.

* *status *code* 
    * But the HTTP protocol requires more than a string as a response to a request.
    * A very important part of the HTTP response is the *status *code 
        * Flask by default sets to *200* 
    * The following view function returns a *400* status code, the code for a bad request error:
    ```
        @app.route('/')
        def index():
            return '<h1>Bad Request</h1>', 400
    
    ```
    * Responses returned by view functions can also take a third argument 
        * a dictionary of headers that are added to the HTTP response.
    

* *make_response()* 
    * The *make_response()*  function takes one, two, or three arguments, the same values that can be returned from a view function, and returns Response object.
    * Example: Creates a response object and then sets a cookie in it:
        ```
            from flask import make_response
            
            @app.route('/')
            def index():
                response = make_response('<h1>This document carries a cookie!</h1>')
                response.set_cookie('answer', '42')
                return response
        
        ```

* *redirect* : 
    * There is a special type of response.
    * This response does not include a page document;
    * It just gives the browser a new URL from which to load a new page.
    * A redirect is typically indicated with a *302* response status code and the URL to redirect to given in a *Location* header.
    ```
        from flask import redirect
        
        @app.route('/')
        def index():
            return redirect('http://www.example.com')
    
    ```
* *abort* :
    * Another special response is issued with the *abort* function.
    * Which is used for error handling.
    * The following example returns status code *404* if the *id* dynamic argument given in the URL does not represent a valid user:
    ```
        from flask import abort
        
        @app.route('/user/<id>')
        def get_user(id):
            user = load_user(id)
            if not user:
                abort(404)
            return '<h1>Hello, %s</h1>' % user.name
            
    ```
    

### Flask Extensions

* Flask is designed to be extended.
* There is a large variety of *extensions* for many different prupose that were created by the community
* And if that is not enough, any standard Python package or library can be used as well.

#### Command-Line Options with Flask-Script
* Flask¡¯s development web server supports a number of startup configuration options
* but the only way to specify them is by passing them as arguments to the app.run() call in the script.
* This is not very convenient
* The ideal way to pass configuration options is through command-line arguments.
* *Flask-Script* is an extension for Flask that adds a command-line parser to your Flask application.
* Install with pip
    `(venv) $ pip install flask-script`
    
* The following example shows the changes needed to add command-line parsing to the *hello.py* application.
    * *hello.py* : Using Flask-Script
    ```
        from flask.ext.script import Manager
        
        manager = Manager(app)
        # ...
        
        if __name__ == '__main__':
            manager.run()
    ```
* With these changes, the application acquires a basic set of commond-line options.
    ```
        $ python hello.py
        usage: hello.py [-h] {shell,runserver} ...
        
        positional arguments:
          {shell,runserver}
            shell            Runs a Python shell inside Flask application context.
            runserver        Runs the Flask development server i.e. app.run()
            
        optional arguments:
          -h, --help         show this help message and exit
    
    ```
    * The *shell* command is used to start a Python shell session in the context of the application.
        * You can use this session to run maintenance tasks or tests, or to debug issues.
    * The *runserver* command, as its name implies, starts the web server. And there are more options available.
        ```
            (venv) $ python hello.py runserver --help
            ...
            optional arguments:
              -h, --help            show this help message and exit
              -t HOST, --host HOST
              -p PORT, --port PORT
              --threaded
              --processes PROCESSES
              --passthrough-errors
              -d, --no-debug
              -r, --no-reload
              
            (venv) $ python hello.py runserver --host 0.0.0.0
             * Running on http://0.0.0.0:5000/
             * Restarting with reloader  
        
        ```



## Chapter 3: Templates
* A template is a file that contains the text of a response, with placeholder variables for the dynamic parts that will be known only in the context of a request.
* The process that replaces the variables with actual values and returns a final response string is called *rendering* . 
* For the task of rendering templates, Flask uses a powerful template engine called *Jinja2* .

### The Jinja2 Template Engine 
* a Jinja2 template is a file that contains the text of a response.
* *templates/index.html* : Jinja2 template
    `<h1>Hello World!</h1>`
* *templates/user.html* : Jinja2 template
    `<h1>Hello {{ name }}!</h1>`

#### Rendering Templates 
* By default Flask looks for templates in a *templates* subfolder located inside the application folder. 
* *hello.py* : Rendering a template
    ```
        from flask import Flask, render_template
        
        # ...
        
        @app.route('/index')
        def index():
            return render_template('index.html')
            
        @app.route('/user/<name>')
        def user(name):
            return render_template('user.html', name=name)
    
    ```
    * The *name* on the left side represents the argument name
        * which is used in the placeholder written in the template
    * The *name* on the right side is a variable in the current scope
        * that provides the value for the argument of the same name
        

#### Variables

* *Jinja2* recognizes variables of any type, even complex types such as lists, dictionaries and objects.
    * examples
        ```
        <p>A value from a dictionary: {{ mydict['key'] }}.</p>
        <p>A value from a list: {{ mylist[3] }}.</p>
        <p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
        <p>A value from an object's method: {{ myobj.somemethod() }}.</p>
        
        ```
* Variables can be modified with *filters* 
    * exs: `Hello, {{ name|capitalize }}`
    * Jinja2 variable filters:
        * *safe* : Renders the value without applying escaping
            * Never use the *safe* filter on values that aren't trusted, such as text entered by users on web forms.
        * *capitalize* : Converts the first character of the value to uppercase and the rest to lowercase
        * *lower* : Converts the value to lowercase characters
        * *upper* : Converts the value to uppercase characters
        * *title* : Capitalizes each word in the value
        * *trim* : Removes leading and trailing whitespace from the value
        * *striptags* : Removes any HTML tags from the value before rendering
        
#### Control Structures
* conditional statements
    ```
        {% if user %}
            Hello, {{ user }}!
        {% else %}
            Hello, Stranger!
        {% endif %}    
    ```
* *for* loop
    ```
        <ul>
            {% for comment in comments %}
                <li>{{ comment }}</li>
            {% endfor %}
        </ul>
    
    ```
* *macros*
    * which are similar to functions in python code.
    ```
        {% macro render_comment(comment) %}
            <li>{{ comment }}</li>
        {% endmacro %}
        
        <ul>
            {% for comment in comments %}
                {{ render_comment(comment) }}
            {% endfor %}
        </ul>
    
    ```
    * To make macros more reusable, they can be stored in standalone files
    * that are then *imported* from all the templates that need them
    ```
        {% import "macros.html" as macros %}
        <ul>    
            {% for comment in comments %}
                {% macros.render_comment(comment) %}
            {% endfor %}
        </ul>
    ```

    
* *included*
    * Portions of template code that need to be repeated in several places can be stored in a separate file 
    * and *included* from all the templates to avoid repetition
    ` {% include 'common.html' %} `   
* *template inheritance* 
    * Yet another powerful way to reuse is through template inheritance
    * which is similar to class inheritance in Python code
    * First, a base template is created with the name *base.html* 
        ```
        <html>
        <head>
            {% block head %}
            <title>{% block title %}{% endblock %} - My Application</title>
            {% endblock %}
        </head>
        <body>
            {% block body %}
            {% endblock %}
        </body>
        </html>        
        ```
    * derive template from the base template.
        ```
            {% extends "base.html" %}
            {% block title %}Index{% endblock %}
            {% block head %}
                {{ super() }}
                <style>
                </style>
            {% endblock %}
            {% block body %}
            <h1>Hello, World!</h1>
            {% endblock %}
        
        ```
        * Note the *head* block, which is not empty in the base template
        * uses *super()* to retain the original contents
        
### Twitter Bootstrap Integration with Flask-Bootstrap

#### Bootstrap intro
    * Bootstrap is an open source framework from Twitter 
    * that provides user interface components to create clean and attractive web pages 
    * that are compatible with all modern web browsers.
    * Bootstrap is a client-side framework, so the server is not directly involved with it.
    
    * The obvious way to integrate Bootstrap with the application is to make all the necessary changes to the templates.
    * A simpler approach is to use a Flask extension called Flask-Bootstrap to simplify the integration effort.
#### Install Flask-Bootstrap
    `(venv) $ pip install flask-bootstrap`
    
#### Flask-Bootstrap initialization
* Flask-Bootstrap initialization
    ```
        from flask.ext.bootstrap import Bootstrap
        # ...
        
        bootstrap = Bootstrap(app)
    
    ```
    * Flask-Bootstrap is imported from the *flask.ext* namespace
    * and initialized by passing the application instance in the constructor.
    * Once Flask-Bootstrap is initialized, a base template that includes all the Bootstrap files is aviable to the application.
    
* Template that uses Flask-Bootstrap
    * *templates/user.html* : Template that uses Flask-Bootstrap
    ```
        {% extends "bootstrap/base.html" %}
        
        {% block title %}Flasky{% endblock %}
        
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
        <div class="container">
            <div class="page-header">
                <h1>Hello, {{ name }}!</h1>
            </div>
        </div>
        {% endblock %}
    
    ```
    
* Flask-Bootstrap¡¯s *base.html* template defines several other blocks that can be used in derived templates.
* The following table shows the complete list of avaiable blocks.
    * *doc*
    * *html_attribs*
    * *html*
    * *head*
    * *title*
    * *metas*
    * *styles*
    * ...
    
    * These blocks are used by Flask-Bootstrap itself.
    * So overriding them directly would cause problems.
* If the application needs to add its own content to a block that already has some content, then Jinja2's *super()* must be used.
    * Add a new JavaScript file to the document.
    ```
        {% block scripts %}
        {{ super() }}
        <script type="text/javascript" src="my-script.js"></script>
        {% endblock %}
    ```
### Custom Error Pages
* Flask allows an application to define custom error pages that can be based on templates
* There are two most common error codes
    * *404* : triggered when the client requests a page or route that is not known
    * *500* : triggered when there is an unhandled exception
* *hello.py* : Custom error pages
    ```
        @app.errorhandler(404)
        def page_not_found(e):
            return render_template('404.html'), 404
            
        @app.errorhandler(500)
        def internal_server_error(e):
            return render_template('500.html'), 500
    
    ```
    
* You can copy *templates/user.html* to *templates/404.html* and *templates/500.html* and then change them.
    * But this will generate a lot of duplication
    
* Jinja2's template *inheritance* can help with this.
* The application can define its own base template just like Flask-Bootstrap provides a base template.
* *templates/base.html* : Base application template with nav bar.
    ```
        {% extends "bootstrap/base.html" %}
        
        {% block title %}Flasky{% endblock %}
        
        {% block navbar %}
        <div class="navbar navbar-inverse" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle"
                     data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="/">Flasky</a>
                </div>
                <div class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="/">Home</a></li>
                    </ul>
                </div>
            </div>
        </div>
        {% endblock %}
        
        {% block content %}
        <div class="container">
            {% block page_content %}{% endblock %}
        </div>
        {% endblock %}
    
    ```
    * In the content block of this template is just a container *div* element that wraps a new empty block called *page_content* , which derived templates can define.
    
    
    
* *templates/404.html* : Custom code 404 error page using template inheritance
    ```
        {% extends "base.html" %}
        
        {% block title %}Flasky - Page Not Found{% endblock %}
        
        {% block page_content %}
        <div class="page-header">
            <h1>Not Found</h1>
        </div>
        {% endblock %}        
    
    ```
* The templates/user.html template can now be simplified by making it inherit from the base template.
* *templates/user.html* : Simplified page template using template inheritance
    ```
        {% extends "base.html" %}
        
        {% block title %}Flasky{% endblock %}
        
        {% page_content %}
        <div class="page-header">
            <h1>Hello, {{ name }}
        </div>
        {% endblock %}
    
    ```

### Links
* Writing the URLs as links directly in the template is trivial for simple routes
    * But for dynamic routes with variable portions it can get more complicated to build the URLs right in the template.
* If the routes are reorganized , links in templates may break.
* To avoid these problems, Flask provides the *url_for()* helper function
    * Which generates URLs from the information stored in the application's URL map.
    
* Some examples:
    * `url_for('index')` : return /
    * `url_for('index', _external=True)` : return an absolute URL,  http://localhost:5000/
    * `url_for('user', name='john', _external=True)` : return http://localhost:5000/user/john
    * `url_for('index', page=2)` : return /?page=2
    * **
    


### Static Files
* Web applications are not made of Python code and templates alone.
* Most applications also use static files such as images, JavaScript source files, and CSS that are referenced from the HTML code.

* Static files are treated as a special route defined as `/static/<filename>`
    * `url_for('static', filename='css/styles.css', _external=True) `
        * http://localhost:5000/static/css/styles.css
        
* Flask looks for static files in *static* subdirectory in the application's root folder.
* *templates/base.html* : favicon definition
    ```
        {% block head %}
        {{ super() }}
        <link rel="shortcut icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
            type="image/x-icon">
        <link rel="icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
            type="image/x-icon">
        {% endblock %}
    
    ```

### Localization of Dates and Times with Flask-Moment

* Handling of dates and times in a web application is not a trivial problem when users work in different parts of the world.
* the server needs uniform time units that are independent of the location of each user, so typically Coordinated Universal Time (UTC) is used.
* An elegant solution that allows the server to work exclusively in UTC is to send these time units to the web browser, where they are converted to local time and rendered.
* There is an excellent client-side open source library written in JavaScript that renders dates and times in the browser called *moment.js*
* *Flask-Moment* is an extension for Flask applications that integrates *moment.js* into Jinja2 templates. 

#### Install Flask-Moment with pip
    `(venv) $ pip install flask-moment`

#### Initialize Flask-Moment
    ```
        from flask.ext.moment import Moment
        
        moment = Moment(app)
    
    ```
* Flask-Moment depends on *jquery.js* in addition to *moment.js* .
* Bootstrap already includes *jquery.js* , only *moment.js* needs to be
added in this case. 

* *templates/base.html* : Import moment.js library
    ```
        {% block scripts %}
        {{ super() }}
        {{ moment.include_moment() }}
        {% endblock %}
    
    ```
* *hello.py* : Add a datetime variable

    ```
        from datetime import datetime
        
        @app.route('/')
        def index():
            return render_template('index.html',
                                                current_time=datetime.utcnow())
    ```
* *templates/index.html* : Timestamp rendering with Flask-Moment
    ```
        <p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
        <p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
        
    ```
    * The format('LLL') format renders the date and time according to the time zone and locale settings in the client computer.
    * The fromNow() render style shown in the second line renders a relative timestamp and automatically refreshes it as time passes.
        * a few seconds ago
        * a minute ago
        * 2 minutes ago
* Flask-Moment implements some methods from *moment.js*
    * *format()*
    * *fromNow()*
    * *fromTime()*
    * *calendar()*
    * *ValueOf()*
    * *unix()*
    
* The timestamps rendered by Flask-Moment can be localized to many languages.
    `{{ moment.lang('es') }}`

    

    
    
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
* *hello.py* : Flask-WTF configuration
    ```
        app = Flask(__name__)    
        app.config['SECRET_KEY'] = 'hard to guess thing'
    ```
    
    * The *app.config* dictionary is a general-purpose place to store configuration variaables used by the framework, the extensions, or the application itself.
    * Configuration values can be added to the *app.config* object using standard dictionary syntax.
    * The configuration object also has methods to import configuration values from files or the environment.
    * *WTF_CSRF_ENABLED* - activates the *cross-site request forgery* prevention.(now it's enabled by default.)
    * *SECRET_KEY*  - only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate a form.


### Form Classes
* *hello.py* : Form class definition
    ```
    from flask.ext.wtf import Form
    from wtforms import StringField, SubmitField
    from wtforms.validators import Required
    
    class NameForm(Form):
        name = StringField('What is your name?', validators=[Required()])
        submit = SubmitField('Submit')
    ```
    
    * The *Required()* validator ensures that the field is not submitted empty.
    * The *Form* base class is defined by the *Flask-WTF* extension, so it is imported from *flask.ext.wtf* .
    * The fields and validators, however, are imported directly from the *WTForms* package.
    
* WTForms supported some standard HTML fields
    * *StringField* : Text field
    * *TextAreaField* :
    * *PasswordField* :
    * *HiddenField* :
    * ...
    * ![Table 4-1. WTForms standard HTML fields.jpg](images/Table 4-1. WTForms standard HTML fields.jpg)
* WTForms built-in validators
    * *Email* : Validates an email address
    * *EqualTo* : useful when requesting a password to be entered twice for confirmation
    * *IPAddress* : Validates an IPv4 network address
    * ...
    * ![Table 4-2. WTForms validators.jpg](images/Table 4-2. WTForms validators.jpg)
    
    

### HTML Rendering of Forms
* *Flask-Bootstrap* provides a very high-level helper function that renders an entire *Flask-WTF* form using Bootstrap's predefined form styles, all with a single call.
* Using *Flask-Bootstrap* , the previous form can be rendered as follows:
    ```
        {% import "bootstrap/wtf.html" as wtf %}
        {{ wtf.quick_form(form) }}
    ```
    * The imported *bootstrap/wtf.html* file defines helper functions that render *Flask-WTF* forms using *Bootstrap* .
    * The *wtf.quick_form()* function takes a *Flask-WTF* form object and renders it using default *Bootstrap* styles.
* The complete template for *hello.py* is  shown below.
    * *template/index.html* : Using Flask-WTF and Flask-Bootstrap to render a form
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
    
    * There has two sections:
        * The first section is a page header that shows a greeting.
        * The second section of the content renders the *NameForm* object using the *wtf.quick_form()* function.


### Form Handling in View Functions

* In the new version of *hello.py* , the *index()* view function will be rendering the form and also receiving its data.
* *hello.py* : Route methods
    ```
    @app.route('/', methods=['GET', 'POST'])
    def index():
        name = None
        form = NameForm()
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''
        return render_template('index.html', form=form, name=name)
    ```
    
    * The *methods* argument added to the app.route decorator tells Flask to register the view function as a handler for *GET* and *POST* requests in the URL map.
    * When *methods* is not given, the view function is registered to handle *GET* requests only.



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
* *hello.py* : Redirects and user sessions
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
    * *hello.py* : Flashed message
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
    * *templates/base.html* : Flash message rendering
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
        <div class="container">
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

    

## Chapter 5. Databases

## SQL Databases & NoSQL Databases

* The most commonly used databases for web applications are those based on the relational model, also called SQL databases in reference to the Structured Query Language they use. 
* But in recent years *document-oriented* and *key-value* databases, informally known together as NoSQL databases, have become popular alternatives.

### SQL Databases
* Relational databases store data in tables, which model the different entities in the application's domain.
* A table has a fixed number of *columns* and a variable number of *rows*.
* Tables have a special column called the *primary_key* , which holds a unique identifier for each row stored in the table.
* Tables can also have columns called *foreign-keys* , which reference the primary key of another row from the same or another table. 
* These links between rows are called *relationships* and are the foundation of the relational database model.

### NoSQL Databases
* Databases that do not follow the relational model described in the previous section are collectively referred to as NoSQL databases.
* One common organization for NoSQL databases uses *collections* instead of *tables* and *documents* instead of *records* . 


### Python Database Frameworks

* Python has packages for most database engines, both open source and commercial
    * Flask puts no restrictions on what database packages can be used
    * You can work with MySQL, Postgres, SQLite, Redis, MongoDB, or CouchDB if any of these is your favorite.
* And there are also a number of database abstraction layer packages
    * such as SQLAlchemy or MongoEngine that allow you to work at a higher level with regular Python objects
    * instead of database entities such as tables, documents, or query languages.
* The chosen database framework for the examples in this book will be *Flask-SQLAlchemy* .
    * The Flask extension wrapper for *SQLAlchemy* .

### Database Management with Flask-SQLAlchemy
* Flask-SQLAlchemy is a Flask extension that simplifies the use of SQLAlchemy inside Flask applications.
    * SQLAlchemy is a powerful relational database framework that supports several database backends.
    * It offers a high-level ORM and low level access to the database¡¯s native SQL functionality.
#### Install Flask-SQLAlchemy
* `(venv) $ pip install flask-sqlalchemy`

#### Flask-SQLAlchemy database URLs
* In Flask-SQLAlchemy, a database is specified as a **URL** .
* The database URLs for the three most popular database engines.
    * *MySQL*  *mysql://username:password@hostname/database*
    * *Postgres*  *postgresql://username:password@hostname/database*
    * *SQLite(Unix)*  *sqlite:////absolute/path/to/database*
    * *SQLite(Windows)*  *sqlite:///c:/absolute/path/to/database*
    ![Table 5-1. Flask-SQLAlchemy database URLs.jpg](images/Table 5-1. Flask-SQLAlchemy database URLs.jpg)

#### Database configuration
* *hello.py* : Database configuration
    ```
        from flask.ext.sqlalchemy import SQLAlchemy
        
        basedir = os.path.abspath(os.path.dirname(__file__))
        
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
        
        db = SQLAlchemy(app)
    
    ```
    * The URL of the application database must be configured as the key *SQLALCHEMY_DATABASE_URI* in the Flask configuration object.
    * Another useful option is the configuration key *SQLALCHEMY_COMMIT_ON_TEARDOWN*
        * which can be set to **True** to enable automatic commits of database changes at the end of each request.
    * The *db* object instantiated from class *SQLAlchemy* represents the database
        * and provides access to all the functionality of *Flask-SQLAlchemy* .
    

### Model Definition
* *hello.py* : Role and User model definition
    ```
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
        
        * ![Table 5-2. Most common SQLAlchemy column types 01](images/Table 5-2. Most common SQLAlchemy column types 01.jpg)
        * ![Table 5-2. Most common SQLAlchemy column types 02](images/Table 5-2. Most common SQLAlchemy column types 02.jpg)
    * Most common SQLAlchemy column options:
        * *primary_key*
        * *unique*      do not allow duplicate values
        * *index*       create an index for this column, so that queries are more efficient.
        * *nullable*    True: allow empty values for this column. False: not allow.
        * *default*     Define a default value for the column.
    * The *__repr__* method representation that tells Python how to print objects of this class. 
        * We will use this for debugging and testing
    
### Relationships
* This is a *one-to-many* relationshiop from roles to users
    * Because one role belongs to many users
    * And users have only one role.
* Relationships
    * *hello.py* : Relationships
    ```
    class Role(db.Model):
        # ...
        users = db.relationship('User', backref='role')
        
    class User(db.Model):
        # ...
        role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))    
    ```
    

* Common SQLAlchemy relationship options
    * *backref* : back reference
    * *primaryjoin* : 
    * ![Table 5-4. Common SQLAlchemy relationship options](images/Table 5-4. Common SQLAlchemy relationship options.jpg)

### Database Operations

* The best way to learn how to work with database models is in a Python shell.

#### Creating the Tables
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
        
#### Inserting Rows
* The following example creates a few roles and users:
    ```
        >>> from hello import Role, User
        >>> admin_role = Role(name='Admin')
        >>> mod_role = Role(name='Moderator')
        >>> user_role = Role(name='User')
        >>> user_john = User(username='john', role=admin_role)
        >>> user_susan = User(username='susan', role=user_role)
        >>> user_david = User(username='david', role=user_role)
    
    ```
    
* The constructors for medels accept initial values for the model attributes as key arguments.
* Note that even the *role* attribute can be used, even though it is not a real database column.
* The *id* attribute of these new objects is not set explicity: the primary keys are managed by *Flask-SQLAlchemy* .
* The objects exist only on the Python side so far; they have not been written to the database yet.
* So:
    ```
        >>> print admin_role.id
        None
        >>> print mod_role.id
        None
    
    ```
    
* Changes to the database are managed through a database *session* , which *Flask-SQLAlchemy* provides as *db.session* .
* To prepare objects to be written to the database, they must be added to the session:
    ```
        >>> db.session.add(admin_role)
        >>> db.session.add(mod_role)
        >>> db.session.add(user_role)
        >>> db.session.add(user_john)
        >>> db.session.add(user_susan)
        >>> db.session.add(user_david)
    ```
    
    * Or, more concisely:
    ```
        >>> db.session.add_all([admin_role, mod_role, user_role,
        ...     user_john, user_susan, user_david])
    
    ```
    
* To write the objects to the database, the session needs to be *commited* by calling its *commit()* method:
    ```
        >>> db.session.commit()
        
    ```
    
* Check the *id* attributes again; they are now set:
    ```
        >>> print(admin_role.id)
        1
        >>> print(mod_role.id)
        2
        >>> print(user_role.id)
        3
        >>> print(user_david.username)
        david
        >>> print(user_david.role)
        <Role u'User'>
    
    ```
* The *db.session* database session is not related to the Flask *session* object.
* Database sessions are also called *transactions* .

* Database sessions are extremely useful in keeping the database consistent. 
* The commit operation writes all the objects that were added to the session atomically.
* If an error occurs while the session is being written, the whole session is discarded. 
* If you always commit related changes together in a session, you are guaranteed to avoid database inconsistencies due to partial updates.

* A database session can also be *rolled-back* . 
    *  If *db.session.rollback()* is called, any objects that were added to the database session are restored to the state they have in the database.
    

#### Modifying Rows
* The *add()* method of the database session can also be used to update models.
    ```
        >>> admin_role.name = 'Administrator'
        >>> db.session.add(admin_role)
        >>> db.session.commit()
    
    ```

#### Deleting Rows
* The database session also has a *delete()* method.
    ```
        >>> db.session.delete(mod_role)
        >>> db.session.commit()
    ```
* Note that deletions, like insertions and updates, are executed only when the database session is committed.

#### Querying Rows
* Flask-SQLAlchemy makes a *query* object available in each model class. 
* The most basic query for a model is the one that returns the entire contents of the corresponding table:
    ```
        >>> Role.query.all()
        [<Role u'Administrator'>, <Role u'User'>]
        >>> User.query.all()
        [<User u'john'>, <User u'susan'>, <User u'david'>]
    
    ```
* A query object can be configured to issue more specific database searches through the use of *filters* .
    ```
        >>> User.query.filter_by(role=user_role).all()
        [<User u'susan'>, <User u'david'>]
    ```

* It is also possible to inspect the native SQL query that SQLAlchemy generates for a given query by converting the query object to a string:
    ```
        >>> str(User.query.filter_by(role=user_role))
        'SELECT users.id AS users_id, users.username AS users_username,
        users.role_id AS users_role_id FROM users WHERE :param_1 = users.role_id'
    
    ```
    
* If you exit the shell session, the objects created in the previous example will cease to exist as Python objects but will continue to exist as rows in their respective database tables.
* If you then start a brand new shell session, you have to re-create Python objects from their database rows. 
    ```
        >>> from hello import db
        >>> from hello import Role, User
        >>> user_role = Role.query.filter_by(name='User').first()
    ```
    
* Common SQLAlchemy query filters
    ![Common SQLAlchemy query filters](images/Table 5-5. Common SQLAlchemy query filters.jpg)
    
* Most common SQLAlchemy query executors
    ![Most common SQLAlchemy query executors](images/Table 5-6. Most common SQLAlchemy query executors.jpg)
    
* Relationships work similarly to queries.
    * The following example queries the one-to-many relationship between roles and users from both ends:
        ```
            >>> users = user_role.users
            >>> users
            [<User u'susan'>, <User u'david'>]
            >>> users[0].role
            <Role u'User'>
        ```
    * The *user_role.users* query here has a small problem. It is not possible to refine it with additional query filters.
        * So we can modify the configuration of the relationship with a *lazy='dynamic'* argument to request that the query is not automatically execute.
        
        * *hello.py* : Dynamic relationships 
            ```
                class Role(db.Model):
                    # ...
                    users = db.relationship('User', backref='role', lazy='dynamic')
                    # ...
            
            ```
        * With the relationship configured in this way, *user_role.users* returns a query that hasn't executed yet, so filters can be added to it.
            ```
                >>> user_role.users.order_by(User.username).all()
                [<User u'david'>, <User u'susan'>]
                >>> user_role.users.count()
                2
            
            ```
    
### Database Use in View Functions
* The database operations described in the previous sections can be used directly inside view functions.
    * *hello.py* : Database use in view functions
    ```
        @app.route('/', methods=['GET', 'POST'])
        def index():
            form = NameForm()
            if form.validate_on_submit():
                user = User.query.filter_by(username=form.name.data).first()
                if user is None:
                    user = User(username = form.name.data)
                    db.session.add(user)
                    session['known'] = False
                else:
                    session['known'] = True
                session['name'] = form.name.data
                form.name.data = ''
                return redirect(url_for('index'))
            return render_template('index.html',
                form = form, name = session.get('name'),
                known = session.get('known', False))
    
    ```
    * Each time a name is submitted the apllication checks for it in the database using the *filter_by()* query filter.
    * A *known* variable is written to the user session, so that after the redirect the information can be sent to the template, where it is used to customize the greeting.
        * Note that for the application to work, the database tables must be created in a Python shell as shown earlier.
        
    * *templates/index.html* : 
        ```
            {% extends "base.html" %}
            
            {% import "bootstrap/wtf.html" as wtf %}
            
            {% block title %}Flasky{% endblock %}
            
            {% block page_content %}
            <div class="page-header">
                <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
                {% if not known %}
                <p>Pleased to meet you!</p>
                {% else %}
                <p>Happy to see you again!</p>
                {% endif %}
            </div>
            
            {{ wtf.quick_form(form) }}
            
            {% endblock %}
        
        ```

### Integration with the Python Shell
* Having to import the database instance and the models each time a shell session is started is tedious work.
* To avoid having to constantly repeat thest imports, the *Flask-Script* 's shell command can be configured to automatically import certain objects.
* To add objects to the import list the shell command needs to be registered with a *make_context* callback function.

* *hello.py* : Adding a shell context
    ```
        from flask.ext.script import Shell
        
        def make_shell_context():
             return dict(app=app, db=db, User=User, Role=Role)
             
        manager.add_command("shell", Shell(make_context=make_shell_context))
    ```
    * The *make_shell_context() function registers the application and database instances and the models so that they are automatically imported into the shell.
    

### Database Migrations with Flask-Migrate
* Sometimes you will find that your database models neet to change.
* *Flask-SQLAlchemy* creates database tables from models only when they do not exist already, so the only way to make it update tables is by destroying the old tables first, but of course this causes all the data in the database to be lost.
* A better solution is to use a *database *migration framework.  
    * The database migration framework keeps track of changes to a database *schema* , and then incremental changes can be applied to the database.
    
    * The lead developer of SQLAlchemy has written a migration framework called *Alembic* 
    * Flask applications can use the *Flask-Migrate* extension, a lightweight *Alembic* wrapper that integrates with Flask-Script to provide all operations through Flask-Script commands.
    

#### Creating a Migration Repository
* To begin, Flask-Migrate must be installed in the virtual environment
    `(venv) $ pip install flask-migrate`
    
* Initialize flask-migrate
    * *hello.py* : Flask-Migrate configuration
        ```
            from flask.ext.migrate import Migrate, MigrateCommand
            
            # ...
            
            migrate = Migrate(app, db)
            manager.add_command('db', MigrateCommand)
        
        ```
        
        * To expose the database migration commands, Flask-Migrate exposes a *MigrateCommand* class that is attached to Flask-Script's *manager* object.
        
* Create a Migration Repository
    * Before database migrations can be maintained, it is necessary to create a migration repository with *init* subcommand
        ```
            (venv) $ python hello.py db init
              Creating directory /home/flask/flasky/migrations...done
              Creating directory /home/flask/flasky/migrations/versions...done
              Generating /home/flask/flasky/migrations/alembic.ini...done
              Generating /home/flask/flasky/migrations/env.py...done
              Generating /home/flask/flasky/migrations/env.pyc...done
              Generating /home/flask/flasky/migrations/README...done
              Generating /home/flask/flasky/migrations/script.py.mako...done
              Please edit configuration/connection/logging settings in
              '/home/flask/flasky/migrations/alembic.ini' before proceeding.
        
        ```
        
        * This command creates a *migrations* folder, where all the migration scripts will be stored.
        
#### Creating a Migration Script

* In Alembic, a database migration is represented by a *migration *script.
    * This script has two functions called *upgrade()* and *downgrade()* .
        * *upgrade()* : applies the database changes that are part of the migration
        * *downgrade()* : removes them.
        
* Alembic migrations can be created **manually** or **automatically** using the *revision* and *migrate* commands, respectively.

* The *migrate* subcommand creates an automatic migration script:
    ```
        (venv) $ python hello.py db migrate -m "initial migration"
        INFO  [alembic.migration] Context impl SQLiteImpl.
        INFO  [alembic.migration] Will assume non-transactional DDL.
        INFO  [alembic.autogenerate] Detected added table 'roles'
        INFO  [alembic.autogenerate] Detected added table 'users'
        INFO  [alembic.autogenerate.compare] Detected added index
        'ix_users_username' on '['username']'
          Generating /home/flask/flasky/migrations/versions/1bc
          594146bb5_initial_migration.py...done
    
    ```
        
#### Upgrading the Database

* Once a migration script has been reviewed and accepted, it can be applied to the database using the `db upgrade` command:
    ```
        (venv) $ python hello.py db upgrade
        INFO  [alembic.migration] Context impl SQLiteImpl.
        INFO  [alembic.migration] Will assume non-transactional DDL.
        INFO  [alembic.migration] Running upgrade None -> 1bc594146bb5, initial migration
    
    ```
    
    * For a first migration, this is effectively equivalent to calling *db.create_all()* , but in successive migrations the *upgrade* command applies updates to the tables without affecting their content.

## Chapter 6. Email
* Although the  smtplib package from the Python standard library can be used to send email inside a Flask application
* The Flask-Mail extension wraps smtplib and integrates it nicely with Flask

### Email Support with Flask-Mail

* installed with pip :
    * `(venv) $ pip install flask-mail`
    
* The extension connects to a Simple Mail Transfer Protocol (SMTP) server and passes
emails to it for delivery.
* If no configuration is given, Flask-Mail connects to *localhost* at port *25* and sends email without authentication. 

    * ![Table 6-1. Flask-Mail SMTP server configuration keys](images/Table 6-1. Flask-Mail SMTP server configuration keys.jpg)
    
* configure the application to send email through a *163* email account.
    * *hello.py* : Flask-Mail configuration for Gmail
    ```
        import os
        # ...
        app.config['MAIL_SERVER'] = 'smtp.163.com'
        app.config['MAIL_PORT'] = 25
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = True
        app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
        app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    ```
    
    * *163* mail need set a *AuthCode* in the setup.
    
* Flask-Mail is initialized
    * *hello.py* : Flask-Mail initialization
    ```
        from flask.ext.mail import Mail
        mail = Mail(app)
    ```
* Set environment variables
    * Linux or Mac OS X using bash
        ```
            (venv) $ export MAIL_USERNAME=<Gmail username>
            (venv) $ export MAIL_PASSWORD=<Gmail password>
        ```
    * Windows
        ```
            (venv) $ set MAIL_USERNAME=<Gmail username>
            (venv) $ set MAIL_PASSWORD=<Gmail password>
        ```
    
    
    
#### Sending Email from the Python Shell

* To test the configuration, you can start a shell session and send a test email:
    ```
        (venv) $ python hello.py shell
        >>> from flask.ext.mail import Message
        >>> from hello import mail
        >>> msg = Message('test subject', sender='you@example.com',
        ...     recipients=['you@example.com'])
        >>> msg.body = 'text body'
        >>> msg.html = '<b>HTML</b> body'
        >>> with app.app_context():
        ...    mail.send(msg)
        ...
    ```
    
    * Note that Flask-Mail¡¯s send() function uses current_app, so it needs to be executed with an activated application context.

* Also You can use this script to test everything is ok.
    * Set environment variables in the script cmd
        
    * *mail_test.py* : 
    ```
        from flask import Flask
        from flask.ext.mail import Mail, Message
        import os

        app = Flask(__name__)

        # config for mail
        app.config['MAIL_SERVER'] = 'smtp.163.com'
        app.config['MAIL_PORT'] = 25
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
        app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

        mail = Mail(app)

        @app.route('/')
        def index():
            msg = Message('test mail subject no2', sender=app.config['MAIL_USERNAME'],
                                    recipients=[app.config['MAIL_USERNAME']])
            msg.body = 'test mail body'
            msg.html = '<b>test mail HTML</b>'
            mail.send(msg)
            
            return 'Mail Send Succeed'
            
            
        if __name__ == '__main__':
            app.run(port=5002, debug=True)

    ```

#### Integrating Emails with the Application

* To avoid having to create email messages manually every time, it is a good idea to abstract the common parts of the application¡¯s email sending functionality into a function.
* As an added benefit, this function can render email bodies from *Jinja2* templates to have the most flexibility.

    * *hello.py* : Email support
    ```
        from flask.ext.mail import Message
        
        app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
        app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
        
        def send_email(to, subject, template, **kwargs):
            msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                          sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
            msg.body = render_template(template + '.txt', **kwargs)
            msg.html = render_template(template + '.html', **kwargs)
            mail.send(msg)
    ```
    
* The *index()* view function can be easily expanded to send an email to the administrator whenever a new name is received with the form.
    * *hello.py* : Email example
    ```
        # ...
        app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
        # ...
        
        @app.route('/', methods=['GET', 'POST'])
        def index():
            form = NameForm()
            if form.validate_on_submit():
                user = User.query.filter_by(username=form.name.data).first()
                if user is None:
                    user = User(username=form.name.data)
                    db.session.add(user)
                    session['known'] = False
                    if app.config['FLASKY_ADMIN']:
                         send_email(app.config['FLASKY_ADMIN'], 'New User',
                                   'mail/new_user', user=user)
                else:
                    session['known'] = True
                session['name'] = form.name.data
                form.name.data = ''
                return redirect(url_for('index'))
            return render_template('index.html', form=form, name=session.get('name'),
                                   known=session.get('known', False))
    ```
    
    * the application needs the *FLASKY_ADMIN* , *MAIL_USERNAME* and *MAIL_USERNAME* environment variables.
    * Two template files need to be created for the text and HTML versions of the email.
        * *templates/mail/* 
        * *templates/mail/* 

#### Sending Asynchronous Email 

* To avoid unnecessary delays during request handling, the email send function can be moved to a background thread. 
    * *hello.py* : Asynchronous email support
    ```
        from threading import Thread
        
        def send_async_email(app, msg):
            with app.app_context():
                 mail.send(msg)
                 
        def send_email(to, subject, template, **kwargs):
            msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                          sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
            msg.body = render_template(template + '.txt', **kwargs)
            msg.html = render_template(template + '.html', **kwargs)
            thr = Thread(target=send_async_email, args=[app, msg])
            thr.start()
            return thr            
    ```
    
    * This implementation highlights an interesting problem. 
        * Many Flask extensions operate under the assumption that there are active application and request contexts. 
        * Flask-Mail¡¯s *send()* function uses *current_app* , so it requires the application context to be active.
        * But when the *mail.send()* function executes in a different thread, the application context nedds to be created artificially using *app.app_context()* .
        
    * Another problem is when you need send a large volume of email, having a job dedicated to sending email is more appropriate than starting a new thread for every email.
        * For example, the execution of the *send_async_email()* function can be sent to a *Celery* task queue.

#### Email Error

* `SMTPSenderRefused: (553, 'authentication is required,163`
    * Most time is the wrong username or password, check it.
    
* `SMTPSenderRefused: (553, 'Mail from must equal authorized user'`
    * change the *sender* to the mail server account.
    
* `RuntimeError: maximum recursion depth exceeded`
    * I made a mistake, in the *send_mail()* function, I wrote *msg.send(msg)* , it should be *mail.send(msg)* . 
    
* `SSLError: [SSL: UNKNOWN_PROTOCOL] unknown protocol (_ssl.c:590)`
    * `app.config['MAIL_USE_SSL'] = True`   (not work)
    * `app.config['MAIL_USE_SSL'] = False`
    
## Chapter 7. Large Application Structure

* Flask does not impose a specific organization for large projects
* In this chapter, a possible way to organize a large application in packages and modules is presented.

### Project Structure

* the basic layout for a Flask application.

    ```
        |-flasky
          |-app/
            |-templates/
            |-static/
            |-main/
              |-__init__.py
              |-errors.py
              |-forms.py
              |-views.py
            |-__init__.py
            |-email.py
            |-models.py
          |-migrations/
          |-tests/
            |-__init__.py
            |-test*.py
          |-venv/
          |-requirements.txt
          |-config.py
          |-manage.py

    ```
* This structure has four top-level folders:
    * *app* : The Flask application lives inside a package generically named *app* .
    * *migrations* : contains the database migration scripts, as before.
    * *tests* : Unit tests are written in a *tests* package.
    * *venv* : contains the Python virtual environment.
    
* There are also a few new files:
    * *requirements.txt* : lists the package dependencies so that it is easy to regenerate an identical virtual environment on a different computer.
    * *config.py* : stores the configuration settings
    * *manage.py* : launches the apllication and other apllication tasks
    
* To help you fully understand this structure, the following sections describe the process to convert the *hello.py* apllication to it.

### Configuration Options

* Applications often need several configuration sets. 
    * The best example of this is the need to use different databasees during development, testing, and production so that they don't interfere with each other.
* Instead of the simple dictionary-like structure configuration used by *hello.py* , a hierarchy of configuration classes can be used.

    * *config.py* : Application configuration
        ```
            import os
            basedir = os.path.abspath(os.path.dirname(__file__))
            
            class Config:
                SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
                SQLALCHEMY_COMMIT_ON_TEARDOWN = True
                FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
                FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
                FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
                
                @staticmethod
                def init_app(app):
                    pass
                    
            class DevelopmentConfig(Config):
                DEBUG = True                
                MAIL_SERVER = 'smtp.googlemail.com'
                MAIL_PORT = 587
                MAIL_USE_TLS = True
                MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
                MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
                SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
                
            class TestingConfig(Config):
                TESTING = True
                SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
            
            class ProductionConfig(Config):
                SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
            
            config = {
                'development': DevelopmentConfig,
                'testing': TestingConfig,
                'production': ProductionConfig,
                'default': DevelopmentConfig
            }
        
        ```
    * To make configuration more flexible and safe, some settings can be optionally imported from environment variables.  *SECRET_KEY*

### Application Package

#### Using an Application Factory
* *app/__init__.py* : Application package constructor
    ```
        from flask import Flask, render_template
        from flask.ext.bootstrap import Bootstrap
        from flask.ext.mail import Mail
        from flask.ext.moment import Moment
        from flask.ext.sqlalchemy import SQLAlchemy
        from config import config
        
        bootstrap = Bootstrap()
        mail = Mail()
        moment = Moment()
        db = SQLAlchemy()
        
        def create_app(config_name):
            app = Flask(__name__)
            app.config.from_object(config[config_name])
            config[config_name].init_app(app)
            
            bootstrap.init_app(app)
            mail.init_app(app)
            moment.init_app(app)
            db.init_app(app)
            
            # attach routes and custom error pages here
            
            return app
    
    ```
    * The single-file version application is created in the global scope, there is no way to apply configuration changes dynamically.
        * by the time the script is running, the application instance has already been created, so it is already too late to make configuration changes.
        
    * The solution to this problem is to delay the creation of the application by moving it into a *factory* *function* that can be explicitly invoked from the script. 
    
    * This constructor imports most of the Flask extensions currently in use.
        * but because there is no application instance to initialize them with, it creates them uninitialized by passing no arguments into their constructiors.
    * The *create_app()* function is the application factory,
        * which takes as an argument the name of a configuration to use for the application.
    * The configuration settings stored in one of the classes defined in *config.py* can be imported directly into the application using the *from_object()* method avaiable in Flask's *app.config* configuration object.

#### Implementing Application Functionality in a Blueprint 

* In single-script applications, the application instance exists in the global scope, so routes can be easily defined using the app.route decorator.
* But now that the application is created at runtime, the app.route decorator begins to exist only after create_app() is invoked, which is too late. 
    * Like routes, custom error page handlers present the same problem, as these are defined with the app.errorhandler decorator.

* Luckily Flask offers a better solution using *blueprints* . 
    * A *blueprint* is similar to an application in that it can also define routes.
    * The difference is that routes associated with a blueprint are in a dormant state until the blueprint is registered with an application, at which point the routes become part of it.

* Like applications, blueprints can be defined all in a single file or can be created in a more structured way with multiple modules inside a package.
    * To allow for the greatest flexibility, a subpackage inside the application package will be created to host the blueprint.
    
    * *app/main/__init__.py* : Blueprint creation
    ```
        from flask import Blueprint
        
        main = Blueprint('main', __name__)
        
        from . import views, errors
    
    ```
    
    * The routes of the application are stored in an *app/main/views.py* module inside the package
    * The error handlers are in *app/main/errors.py* .
    * It is important to note that the modules are imported at the bottom of the *app/__init__.py* script to avoid circular dependencies.
        * Because *views.py* and *errors.py* need to import the *main* blueprint.

* The blueprint is registered with the application inside the *create_app()* factory function.
    * *app/__init__.py* : Blueprint registration
    ```
        def create_app(config_name):
            # ...
            
            from main import main as main_blueprint
            
            app.register_blueprint(main_blueprint)
            
            return app
    ```
    
    * *app/main/errors.py* : Blueprint with error handlers
    ```
        from flask import render_template
        from . import main
        
        @main.app_errorhandler(404)
        def page_not_found(e):
            return render_template('404.html'), 404
            
        @main.app_errorhandler(500)
        def internal_server_error(e):
            return render_template('500.html'), 500
    
    ```
    
    * *app/main/views.py* : Blueprint with application routes
    ```
        from datetime import datetime
        from flask import render_template, session, redirect, url_for        
        from . import main
        from .forms import NameForm
        from .. import db
        from ..models import User
        
        @main.route('/', methods=['GET', 'POST'])
        def index():
            form = NameForm()
            if form.validate_on_submit():
                # ...
                return redirect(url_for('.index'))
            return render_template('index.html',
                                   form=form, name=session.get('name'),
                                   known=session.get('known', False),
                                   current_time=datetime.utcnow())
    
    ```
    
    * *app/main/forms.py* : application forms
    ```
        from flask.ext.wtf import Form
        from wtforms import StringField, SubmitField
        from wtforms.validators import Required


        class NameForm(Form):
            name = StringField('What is your name?', validators=[Required()])
            submit = SubmitField('Submit')
    
    ```
        
### Launch Script
* The *manage.py* file in the top-level folder is used to start the application. 
    * *manage.py* : Launch script
    ```
        #!/usr/bin/env python
        import os
        from app import create_app, db
        from app.models import User, Role
        from flask.ext.script import Manager, Shell
        from flask.ext.migrate import Migrate, MigrateCommand
        
        app = create_app(os.getenv('FLASK_CONFIG') or 'default')
        manager = Manager(app)
        migrate = Migrate(app, db)
        
        def make_shell_context():
            return dict(app=app, db=db, User=User, Role=Role)
            
        manager.add_command("shell", Shell(make_context=make_shell_context))
        manager.add_command('db', MigrateCommand)
        
        if __name__ == '__main__':
            manager.run()
    ```
    
    * As a convenience, a shebang line is added (`#!/usr/bin/env python`)
        * Unix-based operating systems the script can be executed as *./manage.py* instead of the more verbose `python manage.py`.

### Requirements File

* Applications must include a requirements.txt file that records all the package dependencies, with the exact version numbers.

* This file can be generated automatically by *pip* :
    `(venv) $ pip freeze >requirements.txt`
    
* It is a good idea to refresh this file whenever a package is installed or upgraded.
* An example requirements file is shown here:
    ```
        Flask==0.10.1
        Flask-Bootstrap==3.0.3.1
        Flask-Mail==0.9.0
        Flask-Migrate==1.1.0
        Flask-Moment==0.2.0
        Flask-SQLAlchemy==1.0
        Flask-Script==0.6.6
        Flask-WTF==0.9.4
    ```
    
* you can create a new virtual environment and run the following command on it:
    `(venv) $ pip install -r requirements.txt`
    
### Unit Tests

* This application is very small so there isn¡¯t a lot to test yet, but as an example two simple tests can be defined.

* *tests/test_basics.py* : Unit tests
    ```
        import unittest
        from flask import current_app
        from app import create_app, db
        
        class BasicsTestCase(unittest.TestCase):
            def setUp(self):
                self.app = create_app('testing')
                self.app_context = self.app.app_context()
                self.app_context.push()
                db.create_all()
                
            def tearDown(self):
                db.session.remove()
                db.drop_all()
                self.app_context.pop()
                
            def test_app_exists(self):
                self.assertFalse(current_app is None)
                
            def test_app_is_testing(self):
                self.assertTrue(current_app.config['TESTING'])
    
    ```
    
    * The tests are written using the standard *unittest* package from the Python standard library.
        * The setUp() and tearDown() methods run before and after each test
        * And any methods that have a name that begins with *test_* are executed as tests.
        
    * It first creates an application configured for testing and activates its context.
        * This step ensures that tests have access to *current_app* , like regular requests.
    * Then it creates a brand-new database that the test can use when necessary.
    * The database and the application context are removed in the *tearDown()* method.
    * The first test ensures that the application instance exists.
    * The second test ensures that the application is running under the testing configuration. 
    
    * To make the *tests* folder a proper package, a *tests/__init__.py* file needs to be added, but this can be an empty file.
    
    
* To run the unit tests, a custom command can be added to the *manage.py* script.
    * *manage.py* : Unit test launcher command
    ```
        @manager.command
        def test():
            """ Run the unit tests. """
            import unittest
            
            tests = unittest.TestLoader().discover('tests')
            unittest.TextTestRunner(verbosity=2).run(tests)    
    ```
    
    * The *manager.command* decorator makes it simple to implement custom commands.
        * The name of the decorated function is used as the command name
        * And the function's docstring is displayed in the help messages.
    * The implementation of *test()* function invokes the test runner from the *unittest* package.

* The unit tests can be executed as follows:
    ```
        (venv) $ python manage.py test
        test_app_exists (test_basics.BasicsTestCase) ... ok
        test_app_is_testing (test_basics.BasicsTestCase) ... ok
        
        .----------------------------------------------------------------------
        Ran 2 tests in 0.001s
        OK
    
    ```
    
### Database Setup

#### Creating a Migration Repository 
* To begin, Flask-Migrate must be installed in the virtual environment:
    `(venv) $ pip install flask-migrate`
* Initialize the Flask-Migrate extension
    ```
        from flask.ext.migrate import Migrate, MigrateCommand
        
        # ...
        
        migrate = Migrate(app, db)
        manager.add_command('db', MigrateCommand)
    ```
    * To expose the database migration commands, Flask-Migrate exposes a *MigrateCommand* class that is attached to Flask-Script's *manage* object.
    * In this example the command is attached using *db* .
    
* Before database migrations can be maintained, it is necessary to create a migration repository with the *init* subcommand:
    ```
        (venv) $ python hello.py db init
          Creating directory /home/flask/flasky/migrations...done
          Creating directory /home/flask/flasky/migrations/versions...done
          Generating /home/flask/flasky/migrations/alembic.ini...done
          Generating /home/flask/flasky/migrations/env.py...done
          Generating /home/flask/flasky/migrations/env.pyc...done
          Generating /home/flask/flasky/migrations/README...done
          Generating /home/flask/flasky/migrations/script.py.mako...done
          Please edit configuration/connection/logging settings in
          '/home/flask/flasky/migrations/alembic.ini' before proceeding.
    ```
    * This command creates a *migrations* folder, where all the migration scripts will be stored.
    
#### Creating a Migration Script
* The *migrate* subcommand creates an automatic migration script: 
    ```
        (venv) $ python hello.py db migrate -m "initial migration"
        INFO  [alembic.migration] Context impl SQLiteImpl.
        INFO  [alembic.migration] Will assume non-transactional DDL.
        INFO  [alembic.autogenerate] Detected added table 'roles'
        INFO  [alembic.autogenerate] Detected added table 'users'
        INFO  [alembic.autogenerate.compare] Detected added index
        'ix_users_username' on '['username']'
          Generating /home/flask/flasky/migrations/versions/1bc
          594146bb5_initial_migration.py...done
    ```
    
#### Upgrading the Database
* Once a migration script has been reviewed and accepted, it can be applied to the database using the `db upgrade` command:
    ```
        (venv) $ python hello.py db upgrade
        INFO  [alembic.migration] Context impl SQLiteImpl.
        INFO  [alembic.migration] Will assume non-transactional DDL.
        INFO  [alembic.migration] Running upgrade None -> 1bc594146bb5, initial migration
    
    ```
    
    * For a first migration, this is effectively equivalent to calling *db.create_all()* ,
    * But in successive migrations the *upgrade* command applies updates to the tables without affecting their contents. 

# Part II. Example : A Social Blogging Application
## Chapter 8. User Authentication
### Authentication Extensions for Flask
* There are many excellent Python authentication packages, but none of them do everything.
* This is the list of packages that will be used:
    * *Flask-Login* : Management of user sessions for logged-in users
    * *Werkzeug* : Password hashing and verification
    * *istdangerous* : Cryptographically secure token generation and verification
    
* In addition to authentication-specific packages, the following general-purpose extensions will be used:
    * *Flask-Mail* : Sending of authentication-related emails
    * *Flask-Bootstrap* : HTML templates
    * *Flask-WTF* : Web forms

### Password Security
    
* The key to storing user passwords securely in a database relies not on storing the password itself but a *hash* of it.
    * A password hashing function takes a password as input and applies one or more cryptographic transformations to it.
    * The result is a new sequence of characters that has no resemblance to the original password. 
    * Password hashes can be verified in place of the real passwords because hashing functions are repeatable: 
        * given the same inputs, the result is always the same.
        
#### Hashing Passwords with Werkzeug 
* Werkzeug¡¯s *security* module conveniently implements secure password hashing. 
    * This functionality is exposed with just two functions, used in the registration and verification phases, respectively:
        * `generate_password_hash(password, method=pbkdf2:sha1, salt_length=8)`
            * This function takes a plain-text password and returns the password hash as a string that can be stored in the user database.
        * `check_password_hash(hash, password)`   
            * This function takes a password hash retrieved from the database and the password entered by the user. A return value of *True* indicates that the password is correct. 
* *app/models.py* : Password hashing in User model
    ```
        from werkzeug.security import generate_password_hash, check_password_hash
        
        class User(db.Model):
            # ...
            password_hash = db.Column(db.String(128))
            
            @property
            def password(self):
                raise AttributeError('password is not a readable attribute')
                
            @password.setter
            def password(self, password):
                self.password_hash = generate_password_hash(password)
                
            def verify_password(self, password):
                return check_password_hash(self.password_hash, password)
    
    ```

* The password hashing functionality is now complete and can be tested in the shell:
    ```
        (venv) $ python manage.py shell
        >>> u = User()
        >>> u.password = 'cat'
        >>> u.password_hash
        'pbkdf2:sha1:1000$duxMk0OF$4735b293e397d6eeaf650aaf490fd9091f928bed'
        >>> u.verify_password('cat')
        True
        >>> u.verify_password('dog')
        False
        >>> u2 = User()
        >>> u2.password = 'cat'
        >>> u2.password_hash
        'pbkdf2:sha1:1000$UjvnGeTP$875e28eb0874f44101d6b332442218f66975ee89'
    
    ```
    * Note how users u and u2 have completely different password hashes, even though they both use the same password.
    
    * To ensure that this functionality continues to work in the future, the above tests can be written as unit tests that can be repeated easily.
    
    * a new module inside the tests package is shown with three new tests that exercise the recent changes to the User model.
    * *tests/test_user_model.py* : Password hashing tests
        ```
            import unittest
            from app.models import User
            
            class UserModelTestCase(unittest.TestCase):
                def test_password_setter(self):
                    u = User(password = 'cat')
                    self.assertTrue(u.password_hash is not None)
                    
                def test_no_password_getter(self):
                    u = User(password = 'cat')
                    with self.assertRaises(AttributeError):
                        u.password
                        
                def test_password_verification(self):
                    u = User(password = 'cat')
                    self.assertTrue(u.verify_password('cat'))
                    self.assertFalse(u.verify_password('dog'))
                    
                def test_password_salts_are_random(self):
                    u = User(password='cat')
                    u2 = User(password='cat')
                    self.assertTrue(u.password_hash != u2.password_hash)
        ```
        
### Creating an Authentication Blueprint 

* The routes related to the user authentication system can be added to a *auth* blueprint. 
    * Using different blueprints for different sets of application functionality is a great way to keep the code neatly organized.
    
* The *auth* blueprint will be hosted in a Python package with the same name.
* The blueprint¡¯s package constructor creates the blueprint object and imports routes from a *views.py* module. 
    * *app/auth/__init__.py* : Blueprint creation
    ```
        from flask import Blueprint
        
        auth = Blueprint('auth', __name__)
        
        from . import views
    ```
* The *app/auth/views.py* module imports the blueprint and defines the routes associated with authentication using its  route  decorator.      
    * *app/auth/views.py* : Blueprint routes and view functions
    ```
        from flask import render_template
        from . import auth
        
        @auth.route('/login')
        def login():
            return render_template('auth/login.html')
    ```
* The *auth* blueprint needs to be attached to the apllication in the *create_app()* factory function.
    * *app/__init__.py* : Blueprint attachment
    ```
        def create_app(config_name):
            # ...
            from .auth import auth as auth_blueprint
            app.register_blueprint(auth_blueprint, url_prefix='/auth')
            
            return app
    ```
    
    * The *url_prefix* argument in the blueprint registration is optional. 
    * When used, all the routes defined in the blueprint will be registered with the given prefix, in this case */auth* . 
        * */login* route will be registered as */auth/login*
        * fully URL becomes *http://localhost:5000/auth/login* 
    
### User Authentication with Flask-Login
* When users log in to the application, their authenticated state has to be recorded so that it is remembered as they navigate through different pages.
* Flask-Login is a small but extremely useful extension that specializes in managing this  particular aspect of a user authentication system.

#### install with pip
    `(venv) $ pip install flask-login`
    
#### Preparing the User Model for Logins
* To be able to work with the application¡¯s User model, the Flask-Login extension requires a few methods to be implemented by it.
    * *is_authenticated()*
    * *is_active()*
    * *is_anonymous()*
    * *get_id()*
    * ![Table 8-1. Flask-Login user methods](imgs/Table 8-1. Flask-Login user methods.jpg)

* These four methods can be implemented directly as methods in the model class, but as an easier alternative Flask-Login provides a *UserMixin* class that has default implementations that are appropriate for most cases. 
* Updates to the User model to support user logins
    * *app/models.py* : Updates to the User model to support user logins
    ```
        from flask.ext.login import UserMixin
        
        class User(UserMixin, db.Model):
            __tablename__ = 'users'
            id = db.Column(db.Integer, primary_key = True)
            email = db.Column(db.String(64), unique=True, index=True)
            username = db.Column(db.String(64), unique=True, index=True)
            password_hash = db.Column(db.String(128))
            role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    ```
* Flask-Login is initialized in the application factory function
    * *app/__init__.py* : Flask-Login initialization
    ```
        from flask.ext.login import LoginManager
        
        login_manager = LoginManager()
        login_manager.session_protection = 'strong'
        login_manager.login_view = 'auth.login'
        
        def create_app(config_name):
            # ...
            login_manager.init_app(app)
            # ...
    ```
    
    * The *session_protection* attribute of the  *LoginManager* object can be set to  *None* , *'basic'* , or *'strong'* to provide different levels of security against user session tampering. 
        * With the *'strong'* setting, Flask-Login will keep track of the client¡¯s IP address and browser agent and will log the user out if it detects a change. 
    * The *login_view* attribute sets the endpoint for the login page. 
        * Recall that because the login route is inside a blueprint, it needs to be prefixed with the blueprint name.

* Finally, Flask-Login requires the application to set up a callback function that loads a user, given the identifier. 
    * *app/models.py* : User loader callback function
    ```
        from . import login_manager
        
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))
    
    ```
    
#### Protecting Routes
* To protect a route so that it can only be accessed by authenticated users, Flask-Login provides a *login_required* decorator. 
    * An example of its usage follows:
    ```
        from flask.ext.login import login_required
        
        @app.route('/secret')
        @login_required
        def secret():
            return 'Only authenticated users are allowed!'
    ```
    * If this route is accessed by a user who is not authenticated, Flask-Login will intercept the request and send the user to the login page instead.
    

#### Adding a Login Form
* The login form that will be presented to users has a text field for the email address(or username), a password field, a ¡°remember me¡± checkbox, and a submit button. 
    * *app/auth/forms.py* : Login form
    ```
        from flask.ext.wtf import Form
        from wtforms import StringField, PasswordField, BooleanField, SubmitField
        from wtforms.validators import Required, Email
        
        class LoginForm(Form):
            email = StringField('Email', validators=[Required(), Length(1, 64),
                                                     Email()])
            password = PasswordField('Password', validators=[Required()])
            remember_me = BooleanField('Keep me logged in')
            submit = SubmitField('Log In')
    
    ```
* The template associated with the login page is stored in *auth/login.html* . 
    * This template just needs to render the form using Flask-Bootstrap¡¯s *wtf.quick_form()*  macro.
* The navigation bar in the base.html template uses a Jinja2 conditional to display ¡°SignIn¡± or ¡°Sign Out¡± links depending on the logged in state of the current user. 
    * *app/templates/base.html* : Sign In and Sign Out navigation bar links
    ```
        <ul class="nav navbar-nav navbar-right">
            {% if current_user.is_authenticated %}
            <li><a href="{{ url_for('auth.logout') }}">Sign Out</a></li>
            {% else %}
            <li><a href="{{ url_for('auth.login') }}">Sign In</a></li>
            {% endif %}
        </ul>
    
    ```
    * The *current_user* variable used in the conditional is defined by Flask-Login and is automatically available to view functions and templates. 
        * Anonymous user objects respond to the *is_authenticated* method with *False* .
    * Note: Here is *is_authenticated* , shouldn't be *is_authenticated()* .
        * `AttributeError: 'bool' object has no attribute '__call__'`

#### Signing Users In

* The implementation of the login() view function is shown below:
    * *app/auth/views.py* : Sign In route
    ```
        from flask import render_template, redirect, request, url_for, flash
        from flask.ext.login import login_user
        from . import auth
        from ..models import User
        from .forms import LoginForm
        
        @auth.route('/login', methods=['GET', 'POST'])
        def login():
            form = LoginForm()
            if form.validate_on_submit():
                user = User.query.filter_by(email=form.email.data).first()
                if user is not None and user.verify_password(form.password.data):
                    login_user(user, form.remember_me.data)
                    return redirect(request.args.get('next') or url_for('main.index'))
                flash('Invalid username or password.')
            return render_template('auth/login.html', form=form)
    
    ```

* The login template needs to be updated to render the form.
    * *app/templates/auth/login.html* : Render login form
    ```
        {% extends "base.html" %}
        {% import "bootstrap/wtf.html" as wtf %}
        
        {% block title %}Flasky - Login{% endblock %}
        
        {% block page_content %}
        <div class="page-header">
            <h1>Login</h1>
        </div>
        <div class="col-md-4">
            {{ wtf.quick_form(form) }}
        </div>
        {% endblock %}
    
    ```

#### Signing Users Out
* Use sign out
    * *app/auth/views.py* : Sign Out route
    ```
        from flask.ext.login import logout_user, login_required
        
        @auth.route('/logout')
        @login_required
        def logout():
            logout_user()
            flash('You have been logged out.')
            return redirect(url_for('main.index'))   
    ```
    
    * To log a user out, Flask-Login¡¯s *logout_user()* function is called to remove and reset the user session. 
    * The logout is completed with a flash message that confirms the action and a redirect to the home page.

#### Testing Logins

* To verify that the login functionality is working, the home page can be updated to greet the logged-in user by name. 
    * *app/templates/index.html* : Greet the logged-in user
    ```
        Hello,
        {% if current_user.is_authenticated %}
            {{ current_user.username }}
        {% else %}
            Stranger
        {% endif %}!
    
    ```
    
    * In this template once again *current_user.is_authenticated* is used to determine whether the user is logged in.
    
* Because no user registration functionality has been built, a new user can be registered from the shell:
    ```
        (venv) $ python manage.py shell
        >>> u = User(email='john@example.com', username='john', password='cat')
        >>> db.session.add(u)
        >>> db.session.commit()
    
    ```


### New User Registration

#### Adding a User Registration Form
* The form that will be used in the registration page asks the user to enter registration infomation.

    * *app/auth/forms.py* : User registration form
    ```
        from flask.ext.wtf import Form
        from wtforms import StringField, PasswordField, BooleanField, SubmitField
        from wtforms.validators import Required, Length, Email, Regexp, EqualTo        
        from wtforms import ValidationError
        from ..models import User
        
        class RegistrationForm(Form):
            email = StringField('Email', validators=[Required(), Length(1, 64),
                                                     Email()])
            username = StringField('Username', validators=[
                Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                  'Usernames must have only letters, '
                                                  'numbers, dots or underscores')])
            password = PasswordField('Password', validators=[
                Required(), EqualTo('password2', message='Passwords must match.')])
            password2 = PasswordField('Confirm password', validators=[Required()])
            submit = SubmitField('Register')
            
            def validate_email(self, field):
                if User.query.filter_by(email=field.data).first():
                    raise ValidationError('Email already registered.')
                    
            def validate_username(self, field):
                if User.query.filter_by(username=field.data).first():
                    raise ValidationError('Username already in use.')
    
    ```
    
    * This form uses the Regexp validator from WTForms to ensure that the username field contains letters, numbers, underscores, and dots only. 

* The registration page needs to be linked from the login page so that users who don¡¯t
have an account can easily find it. 
    * *app/templates/auth/login.html* : Link to the registration page
    ```
        <p>
            New user?
            <a href="{{ url_for('auth.register') }}">
                Click here to register
            </a>
        </p>
    
    ```


#### Registering New Users

* When the registration form is submitted and validated, a new user is added to the database using the user provided information. 
* The view function that performs this task.
    * *app/auth/views.py* : User registration route
    ```
        @auth.route('/register', methods=['GET', 'POST'])
        def register():
            form = RegistrationForm()
            if form.validate_on_submit():
                user = User(email=form.email.data,
                            username=form.username.data,
                            password=form.password.data)
                db.session.add(user)
                flash('You can now login.')
                return redirect(url_for('auth.login'))
            return render_template('auth/register.html', form=form)
    
    ```

### Account Confirmation

* To validate the email address, applications send a confirmation email to users imme diately after they register. 
    * The new account is initially marked as unconfirmed until the instructions in the email are followed.
* The account confirmation procedure usually involves clicking a specially crafted URL link that includes a confirmation token.


#### Generating Confirmation Tokens with itsdangerous

* The simplest account confirmation link would be a URL with the below format included in the confirmation email, 
    * `http://www.example.com/auth/confirm/<id>`
    * where id is the numeric id assigned to the user in the database. 
* But this is obviously not a secure implementation
    * As any user who figures out the format of the confirmation links 
    * will be able to confirm arbitrary accounts just by sending random numbers in the URL. 
* The idea is to replace the id in the URL with a token that contains the same information securely encrypted.
    * Flask uses cryptographically signed cookies to protect the content of user sessions against tampering. 
    * These secure cookies are signed by a package called *itsdangerous* .
    
* The following is a short shell session that shows how itsdangerous can generate a secure token that contains a user id inside:
    ```
        (venv) $ python manage.py shell
        >>> from manage import app
        >>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
        >>> s = Serializer(app.config['SECRET_KEY'], expires_in = 3600)
        >>> token = s.dumps({ 'confirm': 23 })
        >>> token
        'eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4MTcxODU1OCwiaWF0IjoxMzgxNzE0OTU4fQ.ey ...'
        >>> data = s.loads(token)
        >>> data
        {u'confirm': 23}
    ```
    
    * *Itsdangerous* provides several types of token generators. 
    * Among them, the class *TimedJSONWebSignatureSerializer* generates JSON Web Signatures (JWS) with a
time expiration.
    * The constructor of this class takes an encryption key as argument, which in a Flask application can be the configured *SECRET_KEY* .
    
* Token generation and verification using this functionality can be added to the User model. 
    * *app/models.py* : User account confirmation
    ```
        from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
        from flask import current_app
        from . import db
        
        class User(UserMixin, db.Model):
            # ...
            confirmed = db.Column(db.Boolean, default=False)
            
            def generate_confirmation_token(self, expiration=3600):
                s = Serializer(current_app.config['SECRET_KEY'], expiration)
                return s.dumps({'confirm': self.id})
                
            def confirm(self, token):
                s = Serializer(current_app.config['SECRET_KEY'])
                try:
                    data = s.loads(token)
                except:
                    return False
                if data.get('confirm') != self.id:
                    return False
                self.confirmed = True
                db.session.add(self)
                return True
                
    ```
    
    
#### Sending Confirmation Emails

* The current */register* route redirects to */index* after adding the new user to the database.
* Before redirecting, this route now needs to send the confirmation email. 

* Initialize Mail in *app/__init__.py*
    * *app/__init__.py* : Initialize mail
    ```
        from flask.ext.mail import Mail
        
        mail = Mail()
        
        def create_app(config_name):
            # ...
            mail.init_app(app)
        
    ```

* Create *email.py* for send email.
    * *app/email.py* : Send email
    ```
        from threading import Thread
        from flask import current_app, render_template
        from flask.ext.mail import Message
        from . import mail


        def send_async_email(app, msg):
            with app.app_context():
                mail.send(msg)


        def send_email(to, subject, template, **kwargs):
            app = current_app._get_current_object()
            msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                          sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
            msg.body = render_template(template + '.txt', **kwargs)
            msg.html = render_template(template + '.html', **kwargs)
            thr = Thread(target=send_async_email, args=[app, msg])
            thr.start()
            return thr
    ```
    
    * Note: `app = current_app._get_current_object()` get the application itself in its child models(?)
    
    * *app/auth/views.py* : Registration route with confirmation email
    ```
        from ..email import send_email
        
        @auth.route('/register', methods = ['GET', 'POST'])
        def register():
            form = RegistrationForm()
            if form.validate_on_submit():
                # ...
                db.session.add(user)
                db.session.commit()
                token = user.generate_confirmation_token()
                send_email(user.email, 'Confirm Your Account',
                           'auth/email/confirm', user=user, token=token)
                flash('A confirmation email has been sent to you by email.')
                return redirect(url_for('main.index'))
            return render_template('auth/register.html', form=form)
    ```
    
* The email templates used by the authentication blueprint will be added in the folder *templates/auth/email* to keep them separate from the HTML templates. 
    * for each email two templates are needed for the *plain-* and *rich-text* versions of the body. 
    * *app/auth/templates/auth/email/confirm.txt* : Text body of confirmation email
    ```
        Dear {{ user.username }},
        
        Welcome to Flasky!
        
        To confirm your account please click on the following link:
        
        {{ url_for('auth.confirm', token=token, _external=True) }}
        
        Sincerely,
        
        The Flasky Team
        
        Note: replies to this email address are not monitored.
    ```
    
* The view function that confirms accounts
    * *app/auth/views.py* : Confirm a user account
    ```
        from flask.ext.login import current_user
        
        @auth.route('/confirm/<token>')
        @login_required        
        def confirm(token):
            if current_user.confirmed:
                return redirect(url_for('main.index'))
            if current_user.confirm(token):
                flash('You have confirmed your account. Thanks!')
            else:
                flash('The confirmation link is invalid or has expired.')
            return redirect(url_for('main.index'))
    ```
    
    * This route is protected with the *login_required* decorator from *Flask-Login* , so that when the users click on the link from the confirmation email they are asked to log in before they reach this view function.
    * Because the actual token confirmation is done entirely in the *User* model, all the view function needs to do is call the *confirm()* method and then flash a message according to the result. 
    * When the confirmation succeeds, the *User* model¡¯s *confirmed* attribute is changed and added to the session, which will be committed when the request ends.
    
* Each application can decide what unconfirmed users are allowed to do before they confirm their account.
    * One possibility is to allow unconfirmed users to log in, but only show them a page that asks them to confirm their accounts before they can gain access.
    * This step can be done using Flask¡¯s *before_request* hook.
    * From a blueprint, the *before_request* hook applies only to requests that belong to the blueprint.
    * To install a hook for all application requests from a blueprint, the *before_app_request* decorator must be used instead.
    
    * *app/auth/views.py* : Filter unconfirmed accounts in before_app_request handler
    ```
        @auth.before_app_request
        def before_request():
            if current_user.is_authenticated() \
                    and not current_user.confirmed \
                    and request.endpoint[:5] != 'auth.':
                return redirect(url_for('auth.unconfirmed'))
                
        @auth.route('/unconfirmed')
        def unconfirmed():
            if current_user.is_anonymous() or current_user.confirmed:
                return redirect('main.index')
            return render_template('auth/unconfirmed.html')
    ```
    
    * The *before_app_request* handler will intercept a request when three conditions are true:
        * A user is logged in ( *current_user.is_authenticated()* must return True)
        * The account for the user is not confirmed.
        * The requested endpoint (accessible as  *request.endpoint* ) is outside of the authentication blueprint. 
    * If the three conditions are met, then a redirect is issued to a new */auth/unconfirmed* route that shows a page with information about account confirmation.
        * The page that is presented to unconfirmed users just renders a template that gives users instructions for how to confirm their account and offers a link to request a new confirmation email, in case the original email was lost. 
        
    * The route that resends the confirmation email is shown below.
        * *app/auth/views.py* : Resend account confirmation email
        ```
            @auth.route('/confirm')
            @login_required
            def resend_confirmation():
                token = current_user.generate_confirmation_token()
                send_email(current_user.email, 'Confirm Your Account',
                           'auth/email/confirm', user=current_user, token=token)
                flash('A new confirmation email has been sent to you by email.')
                return redirect(url_for('main.index'))
        ```
    
* Note that a db.session.commit() call had to be added, even though the application configured automatic database commits at the end of the request. 
* THE APPLICATION CONFIGURED AUTOMATIC DATABASE COMMITS AT THE END OF THE REQUEST. 


### Account Management

        
## Chapter 9. User Roles

* There are several ways to implement roles in an application. 
    * For example, a simple application may need just two roles, one for regular users and one for administrators.
        * In this case, having an *is_administrator* Boolean field in the User model may be all that is necessary.
    * A more complex application may need additional roles with varying levels of power in between regular users and administrators.
    
### Database Representation of Roles
    
* *app/models.py* : Role permissions
    ```
        class Role(db.Model):
            __tablename__ = 'roles'
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(64), unique=True)
            default = db.Column(db.Boolean, default=False, index=True)
             permissions = db.Column(db.Integer)
            users = db.relationship('User', backref='role', lazy='dynamic')    
    ```
    
    * The *default* field should be set to *True* for only one role and *False* for all the others.
        * The role marked as default will be the one assigned to new users upon registration.
    * The second addition to the model is the *permissions* field, which is an integer that will be used as bit flags. 
    
* Application permissions
    * ![Table 9-1. Application permissions](images/Table 9-1. Application permissions.jpg)
    
    * *app/models.py* : Permission constants
        ```
            class Permission:
                FOLLOW = 0x01
                COMMENT = 0x02
                WRITE_ARTICLES = 0x04
                MODERATE_COMMENTS = 0x08
                ADMINISTER = 0x80
        
        ```
        
* User roles
    * *Anonymous*
    * *User*
    * *Moderator*
    * *Administrator*
    * ![Table 9-2. User roles](images/Table 9-2. User roles.jpg)
    
    * Adding the roles to the database manually is time consuming and error prone. 
    * Instead, a class method will be added to the Role class for this purpose:
        * *app/models.py* : Create roles in the database
        ```
            class Role(db.Model):
                # ...
                @staticmethod
                def insert_roles():
                    roles = {
                        'User': (Permission.FOLLOW |
                                 Permission.COMMENT |
                                 Permission.WRITE_ARTICLES, True),
                        'Moderator': (Permission.FOLLOW |
                                      Permission.COMMENT |
                                      Permission.WRITE_ARTICLES |
                                      Permission.MODERATE_COMMENTS, False),
                        'Administrator': (0xff, False)
                    }
                    for r in roles:
                        role = Role.query.filter_by(name=r).first()
                        if role is None:
                            role = Role(name=r)
                        role.permissions = roles[r][0]
                        role.default = roles[r][1]
                        db.session.add(role)
                    db.session.commit()        
        ```
        
        * The *insert_roles()* function does not directly create new role objects. 
        * Instead, it tries to find existing roles by name and update those. 
        * To add a new role or change the permission assignments for a role, CHANGE THE ROLES ARRAY AND RERUN THE FUNCTION. 
        * Note that the ¡°Anonymous¡± role does not need to be represented in the database, as it is designed to represent users who are not in the database.
        
    * To apply these roles to the database, a shell session can be used:
        ```
            (venv) $ python manage.py shell
            >>> Role.insert_roles()
            >>> Role.query.all()
            [<Role u'Administrator'>, <Role u'User'>, <Role u'Moderator'>]        
        ```

### Role Assignment

* When users register an account with the application, the correct role should be assigned to them. 
* For most users, the role assigned at registration time will be the ¡°User¡± role, as that is the role that is marked as a default role. 
* The only exception is made for the administrator, which needs to be assigned the ¡°Administrator¡± role from the start. 
    * This user is identified by an email address stored in the FLASKY_ADMIN configuration variable, so as soon as that email  address appears in a registration request it can be given the correct role.
    * *app/models.py* : Define a default role for users
    ```
        class User(UserMixin, db.Model):
            # ...
            def __init__(self, **kwargs):
                super(User, self).__init__(**kwargs)
                if self.role is None:
                    if self.email == current_app.config['FLASKY_ADMIN']:
                        self.role = Role.query.filter_by(permissions=0xff).first()
                    if self.role is None:
                        self.role = Role.query.filter_by(default=True).first()
            # ...
    ```
    


### Role Verification
* To simplify the implementation of roles and permissions, a helper method can be added to the  User model that checks whether a given permission is present.
    * *app/models.py* : Evaluate whether a user has a given permission
    ```
        from flask.ext.login import UserMixin, AnonymousUserMixin
        
        class User(UserMixin, db.Model):
            # ...
            def can(self, permissions):
                return self.role is not None and \
                    (self.role.permissions & permissions) == permissions
                    
            def is_administrator(self):
                return self.can(Permission.ADMINISTER)
                
        class AnonymousUser(AnonymousUserMixin):
            def can(self, permissions):
                return False
                
            def is_administrator(self):
                return False
                
        login_manager.anonymous_user = AnonymousUser
    ```
    
    * The *can()* method added to the User model performs a *bitwise* *and* operation between the requested permissions and the permissions of the assigned role. 
    * The check for administration permissions is so common that it is also implemented as a standalone *is_administrator()* method.
    * For consistency, a custom  *AnonymousUser* class that implements the  *can()* and *is_administrator()* methods is created. 
        * This object inherits from Flask-Login¡¯s *AnonymousUserMixin* class and is registered as the class of the object that is assigned to *current_user* when the user is not logged in. 
        
    * This will enable the application to freely call *current_user.can()* and *current_user.is_administrator()* without having to check whether the user is logged in first.
    
* For cases in which an entire view function needs to be made available only to users with certain permissions, a custom decorator can be used. 
    * the implementation of two decorators, one for generic permission checks and one that checks specifically for administrator permission.
    
    * *app/decorators.py* : Custom decorators that check user permissions
    ```
        from functools import wraps
        from flask import abort
        from flask.ext.login import current_user
        
        def permission_required(permission):
            def decorator(f):
                @wraps(f)
                def decorated_function(*args, **kwargs):
                    if not current_user.can(permission):
                        abort(403)
                    return f(*args, **kwargs)
                return decorated_function
            return decorator
            
        def admin_required(f):
            return permission_required(Permission.ADMINISTER)(f)
    ```
    
    * These decorators are built with the help of the *functools* package from the Python standard library, and return an error code *403* , the ¡°Forbidden¡± HTTP error, when the current user does not have the requested permissions.
    
* The following are two examples that demonstrate the usage of these decorators:
    ```
        from decorators import admin_required, permission_required
        
        @main.route('/admin')
        @login_required
        @admin_required
        def for_admins_only():
            return "For administrators!"
            
        @main.route('/moderator')
        @login_required
        @permission_required(Permission.MODERATE_COMMENTS)
        def for_moderators_only():
            return "For comment moderators!"
    ```
    
* Permissions may also need to be checked from templates, so the *Permission* class with all the bit constants needs to be accessible to them. 
    * To avoid having to add a template argument in every render_template() call, a context processor can be used. Context processors make variables globally available to all templates.
    * *app/main/__init__.py* : Adding the Permission class to the template context
    ```
        @main.app_context_processor
        def inject_permissions():
            return dict(Permission=Permission)
    ```
    
    * HOW TO USE THIS?
    
* The new roles and permissions can be exercised in unit tests. The following example shows two simple tests that also serve as a demonstration of the usage.
    * *tests/test_user_model.py* : Unit tests for roles and permissions
    ```
        class UserModelTestCase(unittest.TestCase):
            # ...
            
            def test_roles_and_permissions(self):
                Role.insert_roles()
                u = User(email='john@example.com', password='cat')
                self.assertTrue(u.can(Permission.WRITE_ARTICLES))
                self.assertFalse(u.can(Permission.MODERATE_COMMENTS))
                
            def test_anonymous_user(self):
                u = AnonymousUser()
                self.assertFalse(u.can(Permission.FOLLOW))
    ```
        
## Chapter 10. User Profiles

### Profile Information

* To make user profile pages more interesting, some additional information about users can be recorded.
    * *app/models.py* : User information fields
    ```
        class User(UserMixin, db.Model):
            # ...
            name = db.Column(db.String(64))
            location = db.Column(db.String(64))
            about_me = db.Column(db.Text())
            member_since = db.Column(db.DateTime(), default=datetime.utcnow)
            last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    ```
    
    * Note that *datetime.utcnow* is missing the () at the end. 
        * This is because the *default* argument to *db.Column()* can take a function as a default value, so each time a default value needs to be generated the function is invoked to produce it. 

* The *last_seen* field is also initialized to the current time upon creation, but it needs to be refreshed each time the user accesses the site. 
    * A method in the *User* class can be added to perform this update. 
    * *app/models.py* : Refresh last visit time of a user
    ```
        class User(UserMixin, db.Model):
            # ...
            def ping(self):
                self.last_seen = datetime.utcnow()
                db.session.add(self)
    ```
    
    * The *ping()* method must be called each time a request from the user is received.  
    * Because the *before_app_request* handler in the *auth* blueprint runs before every request, it can do this easily.
    * *app/auth/views.py* : Ping logged-in user
    ```
        @auth.before_app_request
            def before_request():
                if current_user.is_authenticated():
                    current_user.ping()
                    if not current_user.confirmed \
                            and request.endpoint[:5] != 'auth.':
                        return redirect(url_for('auth.unconfirmed'))
    ```
    

### User Profile Page

* Creating a profile page for each user does not present any new challenges.
    * *app/main/views.py* : Profile page route
    ```
        @main.route('/user/<username>')
        def user(username):
            user = User.query.filter_by(username=username).first()
            if use is None:
                abort(404)
            return render_template('user.html', user=user)    
    ```
    
    * For a user named *john* , the profile page will be at *http://localhost:5000/user/john* . 
* The *user.html* template should render the information stored in the user object.
    * *app/templates/user.html* : User Profile template
    ```
        {% block page_content %}
        <div class="page-header">
            <h1>{{ user.username }}</h1>
            {% if user.name or user.location %}
            <p>
                {% if user.name %}{{ user.name }}{% endif %}
                {% if user.location %}
                    From <a href="http://maps.google.com/?q={{ user.location }}">
                        {{ user.location }}
                    </a>
                {% endif %}
            </p>
            {% endif %}
            {% if current_user.is_administrator() %}
            <p><a href="mailto:{{ user.email }}">{{ user.email }}</a></p>
            {% endif %}
            {% if user.about_me %}<p>{{ user.about_me }}</p>{% endif %}
            <p>
                Member since {{ moment(user.member_since).format('L') }}.
                Last seen {{ moment(user.last_seen).fromNow() }}.
            </p>
        </div>
        {% endblock %}
    ```
    
* As most users will want easy access to their own profile page, a link to it can be added to the navigation bar. The relevant changes to the base.html template are shown below.
    * *app/templates/base.html*
    ```
        {% if current_user.is_authenticated() %}
        <li>
            <a href="{{ url_for('main.user', username=current_user.username) }}">
                Profile
            </a>
        </li>
        {% endif %}
    ```
    

### Profile Editor
#### User-Level Profile Editor
#### Administrator-Level Profile Editor
### User Avatars



## Chapter 11. Blog Posts
## Chapter 12. Followers
## Chapter 13. User Comments
## Chapter 14. Application Programming Interfaces

# Part III. The Last Mile







    
    
    
    
    
    
