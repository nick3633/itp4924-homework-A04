from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db


class home_functions_block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    icon = db.Column(db.String(256))
    content = db.Column(db.String(256))
    editor_user_id = db.Column(db.String(64), db.ForeignKey('admin.user_id'))
    edited_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<home_functions_block {}>'.format(self.id)


class home_about_block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    image = db.Column(db.String(256))
    content = db.Column(db.String(1024))
    link = db.Column(db.String(256))
    link_text = db.Column(db.String(64))
    editor_user_id = db.Column(db.String(64), db.ForeignKey('admin.user_id'))
    edited_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<home_about_block> {}'.format(self.id)


class home_client_block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_logo = db.Column(db.String(256))
    editor_user_id = db.Column(db.String(64), db.ForeignKey('admin.user_id'))
    edited_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<home_client_block> {}'.format(self.id)