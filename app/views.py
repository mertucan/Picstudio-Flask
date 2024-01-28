from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.forms import LoginForm, RegisterForm, QuoteForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, GalleryImage, CustomerMessage, Quote, BlogPost

@app.route('/')
def index():
    messages = CustomerMessage.query.all()
    posts = BlogPost.query.all()
    return render_template('index.html', messages=messages, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    posts = BlogPost.query.all()
    return render_template('blog.html', posts=posts)

@app.route('/gallery')
def gallery():
    images = GalleryImage.query.all()
    return render_template('gallery.html', images=images)

@app.route('/myquote', methods=['GET', 'POST'])
def myquote():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    my_quotes = Quote.query.filter_by(email=current_user.email).all()

    return render_template('myquote.html', my_quotes=my_quotes, hide_menu = True)

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    form = QuoteForm()
    if form.validate_on_submit():
        quote = Quote(name=form.full_name.data, email=form.email.data, quote=form.quote.data, service=form.service.data)
        db.session.add(quote)
        db.session.commit()
        return redirect(url_for('quote'))
    
    return render_template('quote.html', form=form, hide_menu = True)

@app.route('/testimonial')
def testimonial():
    messages = CustomerMessage.query.all()
    return render_template('testimonial.html', messages=messages)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, hide_menu = True)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user() 
    return redirect(url_for('index'))
  
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form, hide_menu = True)