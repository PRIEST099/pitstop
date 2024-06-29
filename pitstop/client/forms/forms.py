from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TimeField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

class OrderForm(FlaskForm):
    car_brand = StringField('Car Brand', validators=[DataRequired()])
    car_model = StringField('Car Model', validators=[DataRequired()])
    vehicle_year = StringField('Vehicle year', validators=[DataRequired()])
    license_plate = StringField('License plate', validators=[DataRequired()])
    service_type = SelectField('Service type',
                               choices=[
                                   ('oil_change', 'Oil change'),
                                   ('tire_change', 'Tire change'),
                                   ('brake_service', 'Brake service'),
                                   ('baterry_replacement', 'Battery replacement'),
                                   ('other', 'Other')
                               ],
                               validators=[DataRequired()])
    preferred_date = DateField('Preffered date', format='%Y-%m-%d', validators=[DataRequired()])
    preferred_time = TimeField('Preffered time', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Start Order')


class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    name = StringField('Enter your name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Strong Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
