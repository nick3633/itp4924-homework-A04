from app import db


class Admin(db.Model):
    user_id = db.Column(db.String(64), primary_key=True, index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Admin {}>'.format(self.user_id)
