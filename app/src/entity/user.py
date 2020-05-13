from datetime import datetime

from flask_login import UserMixin, AnonymousUserMixin

from app.src import db, login_manager

from werkzeug.security import generate_password_hash, check_password_hash

from app.src.entity import login as login_form
from app.src.entity.role import Permission


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role_object = db.relationship('Role', back_populates='users')
    last_name = db.Column(db.String(120), nullable=True)
    about_me = db.Column(db.String(255), nullable=True)
    registration_date = db.Column(db.DateTime, nullable=True)
    last_seen = db.Column(db.DateTime, nullable=True)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def load_from_login(login):
        return User.query.filter_by(login=login).first()

    def can(self, permission):
        return self.role_object is not None and (self.role_object.permissions & permission) == permission

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class AnonymousUser(AnonymousUserMixin):
    def can(self, permission):
        return False

    def is_administrator(self):
        return False


@login_form.user_loader
def load_user(login):
    return User.query.get(login)


login_manager.anonymous_user = AnonymousUser
