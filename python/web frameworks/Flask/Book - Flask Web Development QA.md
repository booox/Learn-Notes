 
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
    
    
* `TemplateNotFound: bootstratp/wtf.html`
    * 