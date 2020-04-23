from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

from app.src.entity.user import User


class SignInForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign In')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user is None:
            raise ValidationError('Please use a correct login.')
