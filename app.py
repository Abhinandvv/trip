from flask import Flask, render_template, url_for, flash, redirect 
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd53157d4061ed102dae462d1365e8b11'
@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
       if form.validate_on_submit(): 
        if form.email.data == 'admin@blog.com' and form.password.data == 'password': 
            flash('You have been logged in!', 'success') 
            return redirect(url_for('home')) 
        else:
            flash('Login Unsuccessfull. Please check username and password', 'danger') 
    return render_template('index1.html', title='Home', form=form) 
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('Signup.html', title='Signup', form=form)

if __name__ == "__main__":
        app.run(debug=True) 