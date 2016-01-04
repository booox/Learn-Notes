
# Installion

## virtualenv

*  `$ sudo pip install virtualenv`

* `$ mkdir myproject`
* `$ cd myproject`
* `$ virtualenv venv`
* `. ven/bin/activate`
    * `$ venv\scripts\activate` ** for Windows **
* `deactivate` (exit the env)
    
## install

* `$ pip install Flask`

# Quickstart

## A Minimal Application

### hello.py

* save as hello.py (NOTICE: Not **flask.py** for conflict)
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

```
* `$ python hello.py`
    * Running on http://127.0.0.1:5000/
    
## Routing

* the `route()` decorator is used to bind a function to a URL

```
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

```

## Variable Rules

* `<variable_name>` can add variable parts to a URL
* `<converter:variable_name>` using a converter
    * `int`: integers
    * `float` : 
    * `path` : like the default but also accepts slashes
    
## Unique URLs / Redirection Behavior

```
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

* With a trailing slash: 
    * Accessing it without a trailing slash will **REDIRECT** to the canonical URL
* Without the trailing slash:
    * Accessing it without a trailing slash will produce a 404 'Not Found' **ERROR**
    
## URL Building

* Build a URL to a specific function use `url_for()`

```
>>> from flask import Flask, url_for
>>> app = Flask(__name__)
>>> @app.route('/')
... def index(): pass
...
>>> @app.route('/login')
... def login(): pass
...
>>> @app.route('/user/<username>')
... def profile(username): pass
...
>>> with app.test_request_context():
...  print url_for('index')
...  print url_for('login')
...  print url_for('login', next='/')
...  print url_for('profile', username='John Doe')
...
/
/login
/login?next=/
/user/John%20Doe

```

* 这里使用了`test_request_context()`方法，它告诉Flask如何处理请求.

## HTTP Methods

* By default, a `route`只能应答对`GET`的请求
* 可以通过将参数传递给`route()`装饰器来修改它

```
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

```

## Static Files

* To generate URLs for static files, use the special `static` endpoint name: 
    `url_for('static', filename='style.css')`
* The file has to be stored on the filesystem as `static/style.css`.

## Rendering Templates

* Render a template you can use the `render_template()` method.
    * All you have to do is provide:
        * the name of the template
        * the variables you want to pass to the template engine as keyword arguments.
        
```
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

```

## Accessing Request Data

* The global `request` object to react to the data a client sent to the sever.
* Make the `request` object can be global is `Context Locals`

    
    
# Tutorial


## Step 4: Request Database Connections

* We need the database connection before each request and shut down afterwards
* Flask do that with the `before_request()`, `after_request()`and `teardown_request()` decorators:

```
    @app.before_request
    def before_request():
        g.db = connect_db()
        
    @app.teardown_request
    def teardown_request(exception):
        db = getattr(g, 'db', None)
        if db is not None:
            db.close()

```
* We store our current database connection on the special `g` object that Flask provides for us.
* This object stores information for one request only and is available from within each function.

## Step 5: The View Functions

### Show Entries

* Show all the entries stored in the database.
* The view function will pass the entries as dicts to the *show_entries.html* template and return the rendered one:

```
@app.route('/')
def show_entries():
    cur = g.db.execute("SELECT title, text FROM Entries ORDER BY id DESC")
    entries = [dict(title=row[0], text=row[1] for row in cur.fetchall())]
    return render_template('show_entries.html', entries=entries)

```

### Add New Entry

* Lets the user add new entries if they are logged in.
* This onley responds to **POST** requests, the actual form is shown on the *show_entries* page.
* If everything worked out well we will `flash()` an information message to the next request
* And redirect back to the *show_entries* page:

```
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('INSERT INTO Entries (title, text) VALUES (?, ?)',
                        [request.form['title'], request.form['text']])
    g.db.commit()
    
    flash('New entry was successfully posted')
    
    return redirect(url_for('show_entries'))
```

### Login and Logout

* Login checks the username and password against the ones from the configuration and sets the `logged_in` key in the session.
    * If the user logged in successfully, that key is set to *True*, and the user is redirected back to the *show_entries* page.
    * In addition, a message is flashed that informs the user that he or she was logged in successfully. 
    * If an error occeurred, the template is notified about that, and the user is asked again:
    
```
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid Username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Password'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


```

* The logout function, removes that key from the session again.
    * We use the `pop()` method of the dict and pass a second parameter to it(the default)
    * the method will delete the key from the dictionary.
    
```
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
    

```

## Step 6: The Templates

### layout.html

* This template contains the HTML skeleton, the header and a link to log in(or log out if the user was already logged in ).
* It alse displays the flashed messages if there are any.
* The `{% block body %}` block can be replaced by a block of the same name (*body*) in a child template.
* The `Session` dict is available in the template as well, so you can use that to check if the user is logged in or not.
* Note that in **Jinja** you can access missing attributes and items of objects / dicts.

```
<!doctype html>
<title>Flaskblog</title>
<link rel="stylesheet" type=text/css href="{{ url_for('static', filename='style.css')}}" />
<div class=page>
	<h1>Flaskblog</h1>
	<div class=metanav>
        {% if not session.logged_in %}
            <a href="{{ url_for('login') }}">login</a>
        {% else %}
            <a href="{{ url_for('logout') }}">logout</a>
        {% endif %}
    </div>
        {% for message in get_flashed_messages() %}
        <div class="flash">{{ message }}</div>
        {% endfor %}
    {% block body %}{% endblock %}
</div>

```


### show_entries.html

* This template extends the *layout.html* template from above to display the messages.
* The *for* loop iterates over the messages we passed in with the `render_template()` function.
* We also tell the form to submit to your *add_entry* function and use *POST* as *HTTP* method.

```
{% extends "layout.html" %}
{% block body %}
    {% if session.logged_in %}
        <form action="{{ url_for('add_entry') }}" class="add-entry" method="post">
        	<dl>
        		<dt>Title:</dt>
        		<dd><input type="text" size=30 name=title /></dd>
        		<dt>Text:</dt>
        		<dd><textarea name="text" cols="40" rows="5"></textarea></dd>
        		<dd><input type="submt" value="Share" /></dd>
        	</dl>
        </form>
    {% endif %}
    <ul class="entries">
    {% for entry in entries %}
        <li>
        	<h2>{{ entry.title }}</h2>
            {{ entry.text |safe }}
        </li>
    {% else %}
        <li><em>Unbelievable. No entries here so far</em></li>
    {% endfor %}
    </ul>

{% endblock %}

```

### layin.html

* The login template which basically just displays a form to allow the user to login:

```
{% extends "layout.html" %}
{% block body %}
    <h2>Login</h2>
    {% if error %} <p class="error"><strong>Error:</strong> {{ error }}</p> {% endif %}
    <form action="{{ url_for('login') }}" method=post>
    	<dl>
    		<dt>Username:</dt>
    		<dd><input type="text" name="username" /></dd>
            <dt>Password:</dt>
    		<dd><input type="password" name="password" /></dd>
    		<dd><input type="submit" value="Login" /></dd>
    	</dl>
    </form>
{% endblock %}

```
## Step 7: Adding Style

* Create a stylesheet called *style.css* in the static folder.

```
body            { font-family: sans-serif; background: #eee; }
a, h1, h2       { color: #377ba8; }
h1, h2          { font-family: 'Georgia', serif; margin: 0; }
h1              { border-bottom: 2px solid #eee; }
h2              { font-size: 1.2em; }

.page           { margin: 2em auto; width: 35em; border: 5px solid #ccc;
                  padding: 0.8em; background: white; }
.entries        { list-style: none; margin: 0; padding: 0; }
.entries li     { margin: 0.8em 1.2em; }
.entries li h2  { margin-left: -1em; }
.add-entry      { font-size: 0.9em; border-bottom: 1px solid #ccc; }
.add-entry dl   { font-weight: bold; }
.metanav        { text-align: right; font-size: 0.8em; padding: 0.3em;
                  margin-bottom: 1em; background: #fafafa; }
.flash          { background: #cee5F5; padding: 0.5em;
                  border: 1px solid #aacbe2; }
.error          { background: #f0d6d6; padding: 0.5em; }

```

## Bonus: Testing the Application

* Add a automated tests

## Testing Flask Applications








