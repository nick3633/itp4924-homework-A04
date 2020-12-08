from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Admin

from app.admin.forms import *
from app.app_about.forms import *
from app.app_architecture.forms import *
from app.app_home.forms import *
from app.app_learn.forms import *