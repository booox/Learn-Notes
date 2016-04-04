 
*  P114 : Example 9-4. app/models.py: Define a default role for users
    ```
        def __init__(self, **kwargs):
            super(User, self).__init__(**kwargs)
            if self.role is None:
                if self.email == current_app.config['FLASK_ADMIN']:
                    self.role = Role.query.filter_by(permissions=0xff).first()
                if self.role is None:
                    self.role = Role.query.filter_by(default=True).first()
    ```
    
    * `permissions=0xff` ?
    * `super(User, self).__init__(**kwargs)`
    
- [] template : `{{ url_for('static', filename='avatar/{{ img_id }}.jpg') }}`
    
    
* `TemplateNotFound: bootstratp/wtf.html`
    * a typo: `bootstrap/wtf.html`
    
* `Internal Server Error`
    * before-error: `(venv) $ python manage runserver -d`
    * modify : `(venv) $ python manage runserver`

* `python manage.py db migrate`
    `AttributeError: '_MigrateConfig' object has no attribute 'configure_args'`
    * Becasue Flask-Migrate version doesn't match
    * modify : 
        ```
            pip uninstall flask-migrate
            pip install flask-migrate
        ```
        
* `ValueError: View function did not return a response`
    * `render_template('edit_profile.html', form=form)`
    * `return render_template('edit_profile.html', form=form)` : missed *return*
    
* `BuildError: ('post', {'id': 3}, None)`
    * error from: `return redirect(url_for('post', id=post.id))`
    * modified:
        `return redirect(url_for('.post', id=post.id))` 
    * Note:
        ```
            url_for('.post', id=id)
            url_for('auth.unconfirmed')
            url_for('main.index')
        ```
    
* Refresh page every-time, need access *cdnjs.cloudflare.com* to get the *css/js* 
    * add a line in *app.config* :
        `BOOTSTRAP_SERVE_LOCAL = True`
        
* Error: `{{ url_for('static/avatar', filename='v_1.jpg') }}`
    * Right: `{{ url_for('static', filename='avatar/IMG_1.jpg') }}`

* Error: `Method Not Allowed : The method is not allowed for the requested URL.`
    * Wrong : `@main.route('/post/<int:id>')`
    * Right: `@main.route('/post/<int:id>', methods=['GET', 'POST'])`
    
* When two clients try to access the application at the same time, it not response.
    * flask default set *threading=False* 
    * so set : `(venv) $ python manage.py runserver -p 5001 --threaded` to enable threading.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    