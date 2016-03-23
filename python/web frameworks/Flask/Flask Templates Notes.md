
# The Jinja2 Template Engine
## Rendering Templates

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
## Variables

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
        
## Control Structures
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
        
# Twitter Bootstrap Integration with Flask-Bootstrap

## Bootstrap intro
    * Bootstrap is an open source framework from Twitter 
    * that provides user interface components to create clean and attractive web pages 
    * that are compatible with all modern web browsers.
    * Bootstrap is a client-side framework, so the server is not directly involved with it.
    
    * The obvious way to integrate Bootstrap with the application is to make all the necessary changes to the templates.
    * A simpler approach is to use a Flask extension called Flask-Bootstrap to simplify the integration effort.
## Install Flask-Bootstrap
    `(venv) $ pip install flask-bootstrap`
    
## Flask-Bootstrap initialization
    ```
        from flask.ext.bootstrap import Bootstrap
        # ...
        
        bootstrap = Bootstrap(app)
    
    ```
    * Flask-Bootstrap is imported from the *flask.ext* namespace
    * and initialized by passing the application instance in the constructor.
    * Once Flask-Bootstrap is initialized, a base template that includes all the Bootstrap files is aviable to the application.
    
    
    
    
    
    
    
    
    
    
    