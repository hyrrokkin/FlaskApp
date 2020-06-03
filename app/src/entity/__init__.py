from flask_login import LoginManager

from app.src import app

login = LoginManager(app)

from app.src.entity import role, user, track, music
