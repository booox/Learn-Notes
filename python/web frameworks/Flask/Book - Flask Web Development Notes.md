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
    * ![Table 4-1. WTForms standard HTML fields.jpg](Table 4-1. WTForms standard HTML fields.jpg)
* WTForms built-in validators
    * *Email* : Validates an email address
    * *EqualTo* : useful when requesting a password to be entered twice for confirmation
    * *IPAddress* : Validates an IPv4 network address
    * ...
    * ![Table 4-2. WTForms validators.jpg](Table 4-2. WTForms validators.jpg)
    
    

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
    * It offers a high-level ORM and low level access to the database¡¯s native SQL functionality.
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




    
    
    
    
    
    
