from flask import Flask, escape, request, render_template, flash, redirect, url_for
from forms import LoginForm
from flask_bcrypt import Bcrypt
import os

PASS = os.environ.get('PRINTER_PASS')
app = Flask(__name__)
app.config['SECRET_KEY'] = '---------------------------'
bcrypt = Bcrypt(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == PASS:
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('incorrect password', 'danger')
    return render_template('authenticate.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True, )