import os

from flask import render_template, flash, url_for, request, json
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import redirect, secure_filename

import requests

from flask_bootstrap import Bootstrap

from app.config import ALLOWED_EXTENSIONS
from app.src import app, db
from app.src.decorator.permission_decorator import admin_required
from app.src.entity.music import Music
from app.src.entity.user import User
from app.src.form.music_form import MusicForm
from app.src.form.sign_in_form import SignInForm
from app.src.form.sign_up_form import SignUpForm

from datetime import datetime

bootstrap = Bootstrap(app)


@app.route("/admin_page")
@admin_required
def admin_page():
    pass


@app.route("/")
@app.route("/index")
def index():
    if current_user.is_authenticated:
        current_user.ping()
        db.session.commit()
    return render_template('index.html', current_user=current_user)


@app.route("/users/<username>", methods=['GET', 'POST'])
def profile(username):
    if current_user.is_authenticated:
        current_user.ping()
        db.session.commit()
    user = User.load_from_login(username)

    # if user is None or user.login != current_user.login and not current_user.is_administrator():
    #   return redirect('index')

    # form = EditProfileForm()

    # if form.validate_on_exit():
    #    return redirect('logout')

    # if form.validate_on_save():
    #    return redirect('index')

    return render_template('profile.html', user=user, current_user=current_user)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        current_user.ping()
        db.session.commit()
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(login=form.login.data, name=form.name.data, email=form.email.data, role=0,
                    registration_date=datetime.utcnow())
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user)
        return redirect('index')

    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        current_user.ping()
        db.session.commit()
    form = SignInForm()

    if not current_user.is_authenticated:
        if form.validate_on_submit():
            user = User.load_from_login(form.login.data)

            if user is None or not user.check_password(form.password.data):
                flash('Invalid login ot password')
                return redirect(url_for('signin'))

            login_user(user, remember=form.remember_me.data)

            return redirect('index')

        return render_template('signin.html', title='Sign In', form=form)

    return redirect('index')


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        current_user.ping()
        db.session.commit()
    logout_user()
    return redirect('index')


@app.route('/country/<text>')
def country(text):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Token a2671c86ace86c4ebf110f0b8732193232b9379d',
    }

    data = ("{ \"query\": \"%s\" }" % text).encode('utf-8')

    response = requests.post('https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/country', headers=headers,
                             data=data)

    print(response.content.decode("utf-8"))

    return response.content.decode("utf-8")


@app.route('/music')
def music():
    music = Music.sort_by_input_date()

    return render_template('music.html', title='Music', music=music, current_user=current_user)


def upload():
    pass


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/music/upload', methods=['GET', 'POST'])
def upload_music():
    if not current_user.is_authenticated:
        return 'access forbidden', 403

    form = MusicForm()

    if form.validate_on_submit():
        file = form.cover.data
        filename = secure_filename(form.cover.data.filename)

        if file.filename == '':
            flash('No selected file')
            return redirect('index')
        if file and allowed_file(filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/cover/", filename))

            music = Music(
                name=form.name.data,
                performer=form.performer.data,
                genre=form.genre.data,
                input_date=datetime.utcnow(),
                release_date=form.release_date.data,
                cover=filename
            )

            db.session.add(music)
            db.session.commit()

            return redirect('/music/upload')
        return redirect('index')

    return render_template('upload_music.html', title='Загрузка', current_user=current_user, music=form)
