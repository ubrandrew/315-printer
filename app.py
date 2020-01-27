from flask import Flask, escape, request, render_template, flash, redirect, url_for
from forms import LoginForm, GuestForm, RegistrationForm, PrintForm
from flask_bcrypt import Bcrypt
import os

PASS = os.environ.get('PRINTER_PASS')
app = Flask(__name__)
app.config['SECRET_KEY'] = '---------------------------'
bcrypt = Bcrypt(app)

@app.route('/')
@app.route('/home')
def home():
    form = PrintForm()
    if form.validate_on_submit():
         pass
    return render_template('home.html', title='home', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = GuestForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print(hashed_password)
        if bcrypt.check_password_hash(hashed_password, PASS):
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('incorrect password', 'danger')
    return render_template('authenticate.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True, )