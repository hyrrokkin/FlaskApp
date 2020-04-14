from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask


app = Flask(__name__)
app.config.from_object('app.config')
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models