from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, TextField, FileField, IntegerField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = TextField('Email')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GuestForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    email = TextField('Email')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PrintForm(FlaskForm):
    name = TextField('Job Name', validators=[DataRequired()])
    input_file = FileField('Upload File', validators=[DataRequired()])
    quantity = IntegerField("Quantity", default=1)
    submit = SubmitField('Submit')