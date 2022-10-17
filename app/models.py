from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime as dt

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    icon = db.Column(db.Integer)
    # current_user.followed.all() #all the people current user is following
    # current_user.followers.all() # all the people following the current user



    # Should return a unique identifing string
    def __repr__(self):
        return f'<User: {self.email} | {self.id} >'

    # Human Readable repr
    def __str__(self):
        return f'<User: {self.email} | {self.first_name} {self.last_name}>'
    
    # salt and hash our password to make it hard to steal
    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    # save the user to the db
    def save(self):
        db.session.add(self) # add the user to out session
        db.session.commit() # saves the session to the database

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.password = self.hash_password(data['password'])
        self.icon = data['icon']

    def get_icon_url(self):
        return f"https://avatars.dicebear.com/api/adventurer/{self.icon}.svg"