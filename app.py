from flask import Flask, escape, request, render_template, flash, redirect, url_for
from forms import LoginForm, GuestForm, RegistrationForm, PrintForm
from flask_bcrypt import Bcrypt
import os
import pathlib
from werkzeug.utils import secure_filename


PASS = os.environ.get('PRINTER_PASS')
app = Flask(__name__)
app.config['SECRET_KEY'] = '---------------------------'
bcrypt = Bcrypt(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'temp_doc_store')


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = PrintForm()
    print(request)

    if form.validate_on_submit() and request.method == 'POST':
        input_file = request.files['input_file']
        filename = secure_filename(input_file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        input_file.save(path)
        os.system(f'lp -dHP_LaserJet_1018 {path}')
        flash("Printed successfully")
    return render_template('home.html', title='home', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = GuestForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if bcrypt.check_password_hash(hashed_password, PASS):
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('incorrect password', 'danger')
    return render_template('authenticate.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True, )