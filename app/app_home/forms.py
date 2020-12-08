from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Admin
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class home_function_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    icon = StringField('Icon URL')
    content = TextAreaField('Content (can have html code)', validators=[DataRequired()])
    submit = SubmitField('Add')


class home_about_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL')
    content = TextAreaField('Content (can have html code)', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    submit = SubmitField('Add')


class home_client_block_add(FlaskForm):
    client_logo = StringField('Icon URL')
    submit = SubmitField('Add')


class home_function_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    icon = StringField('Icon URL')
    content = TextAreaField('Content (can have html code)', validators=[DataRequired()])
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    # https://wtforms.readthedocs.io/en/stable/fields.html (4/9/2020 4:19PM)
    submit = SubmitField('Apply')


class home_about_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL')
    content = TextAreaField('Content (can have html code)', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')


class home_client_block_edit(FlaskForm):
    client_logo = StringField('Icon URL')
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')