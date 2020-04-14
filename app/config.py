import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
