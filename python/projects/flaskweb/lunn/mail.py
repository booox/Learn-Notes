#!venv/bin/python
#coding=utf-8
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
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            