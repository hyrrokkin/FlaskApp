import os
from os.path import join, dirname, realpath

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
