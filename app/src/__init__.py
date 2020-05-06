from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint
from app import config

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bp = Blueprint('main', __name__)
login_manager = LoginManager(app)

from app.src import entity, form, controller, login_manager
