from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Admin


class home_function_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    icon = StringField('Icon URL')
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add')


class home_about_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL')
    content = TextAreaField('Content', validators=[DataRequired()])
    link = TextAreaField('Link', validators=[DataRequired()])
    submit = SubmitField('Add')


class home_function_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    icon = StringField('Icon URL')
    content = TextAreaField('Content', validators=[DataRequired()])
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    # https://wtforms.readthedocs.io/en/stable/fields.html (4/9/2020 4:19PM)
    submit = SubmitField('Apply')


class home_about_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL')
    content = TextAreaField('Content', validators=[DataRequired()])
    link = TextAreaField('Link', validators=[DataRequired()])
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')


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
