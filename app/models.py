from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    
class CustomerMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), index=True)
    quote = db.Column(db.String(64), nullable=False)
    service = db.Column(db.String(64), nullable=False)
    
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    heading = db.Column(db.String(64), nullable=False)
    posted = db.Column(db.String(64), nullable=False)
    post = db.Column(db.String(256), nullable=False)
    