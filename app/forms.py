from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Admin


class AdminLoginForm(FlaskForm):
    user_id = StringField('User ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AddAdminForm(FlaskForm):
    user_id = StringField('User ID', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    verification_key = PasswordField('Verification Key', validators=[DataRequired()])
    submit = SubmitField('Add Admin')

    def CheckUserID(self, user_id):
        user = Admin.query.filter_by(user_id=user_id.data).first()
        if user is not None:
            raise ('This user ID already used.')

    def CheckEmail(self, email):
        user = Admin.query.filter_by(email=email.data).first()
        if user is not None:
            raise ('This email already used.')
