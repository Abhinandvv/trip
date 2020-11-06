from flask import render_template, url_for, flash, redirect 
from sampleproject import app, db, bcrypt
from sampleproject.forms import RegistrationForm, LoginForm
from sampleproject.models import User, Post
from flask_login import login_user, current_user, logout_user
# home and login route
@app.route('/', methods=['GET', 'POST'])
def home():
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(email=lform.email.data).first()
        if user and bcrypt.check_password_hash(user.password, lform.password.data):
            login_user(user, remember=lform.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull. Please check email and password', 'danger') 
    return render_template('index1.html', title='Home', lform=lform) 
# sign up route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    lform = LoginForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created For {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('Signup.html', title='Signup', form=form, lform=lform)
# logout route
@app.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('home'))
# add story
@app.route('/addstory')
def addstory():
    lform = LoginForm()
    if current_user.is_authenticated:
        return render_template('addstory.html', title='Add Story', lform=lform)
    return redirect(url_for('home'))