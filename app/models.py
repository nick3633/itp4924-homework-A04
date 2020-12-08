from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login

from app.admin.models import Admin


@login.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)


from app.admin.models import *
from app.app_about.models import *
from app.app_architecture.models import *
from app.app_home.models import *
from app.app_learn.models import *