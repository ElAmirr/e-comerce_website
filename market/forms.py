from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, InputRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist! Please try different username')

    def validate_email_address(sel, email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('Email addrerss already exist! Please try differente email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), InputRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), InputRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), InputRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), InputRequired()])
    submit = SubmitField(label='Create Account')
