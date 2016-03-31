#!venv/bin/python
#coding=utf-8

from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import session
from flask import flash
from flask.ext.script import Manager
from flask.ext.script import Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

from flask.ext.mail import Mail, Message
from threading import Thread

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

import os, sys
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SECRET_KEY'] = 'something that hard to guess'

# config for mail
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = os.environ.get('MAIL_USERNAME')
app.config['FLASKY_ADMIN_EMAIL'] = os.environ.get('MAIL_USERNAME')  # just for test


manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class NameForm(Form):
    name = StringField('What is your name?', 
                                validators=[Required()])
    submit = SubmitField('Submit')
    
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    
    def __repr__(self):
        return '<Role %r>' % (self.name)
        
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User %r>' % (self.username)
    
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
    
def send_async_email(app, msg):
    """ asynchronous email send """
    with app.app_context():
        mail.send(msg)
        
    
# send email
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, 
                           sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    print 'msg: ', msg
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
            # send a eamil to administrator
            print 'admin mail: ', app.config['FLASKY_ADMIN_EMAIL']
            if app.config['FLASKY_ADMIN_EMAIL']:
                print 'test admin mail'
                send_email(app.config['FLASKY_ADMIN_EMAIL'], 'New User',
                                'mail/new_user', user=user)
                                
        else:
            session['known'] = True
            
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
        
    return render_template('index.html',
                                       form=form,
                                       name=session.get('name'),
                                       known = session.get('known', False),
                                       current_time=datetime.utcnow())
                                       
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command("db", MigrateCommand)
    manager.run()