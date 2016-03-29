
# read-only
class C(object):
    @property
    def age(self):
        return self._age
        
        
# read-write
class C(object):
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
       assert value >= 0
       self._age = value
       
       
# only write, unreadable
class User(object):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)