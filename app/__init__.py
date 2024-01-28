from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babel import Babel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
admin = Admin()
babel = Babel()
login_manager = LoginManager(app)
login_manager.init_app(app)
admin.init_app(app)
babel.init_app(app)

from app import views, models, db
from app.models import User, GalleryImage, CustomerMessage, Quote, BlogPost

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(GalleryImage, db.session))
admin.add_view(ModelView(CustomerMessage, db.session))
admin.add_view(ModelView(Quote, db.session))
admin.add_view(ModelView(BlogPost, db.session))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))