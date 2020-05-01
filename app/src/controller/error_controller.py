from flask import render_template
from flask_login import current_user

from app.src import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html', is_auth=current_user.is_authenticated), 404


@app.errorhandler(403)
def access_forbidden(e):
    return render_template('error/403.html', is_auth=current_user.is_authenticated), 403
