from flask import render_template, flash

from app import app, db
from app.forms import SignUpForm
from flask_bootstrap import Bootstrap

from app.models import User

bootstrap = Bootstrap(app)


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

    return render_template('signup.html', title='Sign In', form=form)
