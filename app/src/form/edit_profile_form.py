from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class EditProfileForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    about_me = TextAreaField('Обо мне', validators=[DataRequired()])
    email = StringField('Адрес почтового ящика', validators=[DataRequired(), Email()])

    submit = SubmitField('Сохранить')
