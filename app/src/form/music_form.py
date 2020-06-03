from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SubmitField, FileField, DateField
from wtforms.validators import DataRequired


class MusicForm(FlaskForm):
    name = StringField(
        'Название',
        validators=[DataRequired()],
        default=''
    )

    performer = StringField(
        'Исполнитель',
        validators=[DataRequired()],
        default=''
    )

    genre = StringField(
        'Жанр',
        validators=[DataRequired()],
        default=''
    )

    release_date = DateField(
        'Дата выхода',
        format='%d.%m.%Y'
    )

    cover = FileField(
        'image',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png'], 'Images only!')
        ]
    )

    submit = SubmitField('Сохранить')
