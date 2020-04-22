from flask import render_template, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import redirect

from app import app, db
from app.forms import SignUpForm, SignInForm
from flask_bootstrap import Bootstrap

from app.models import User

bootstrap = Bootstrap(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', is_auth=current_user.is_authenticated)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(login=form.login.data, name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return 'success'

    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
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
    logout_user()
    return redirect('index')
