from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Admin(UserMixin, db.Model):
    user_id = db.Column(db.String(64), primary_key=True, index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Admin {}>'.format(self.user_id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return (self.user_id)
    # https://stackoverflow.com/questions/37472870/login-user-fails-to-get-user-id (4/7/2020 1:15AM)