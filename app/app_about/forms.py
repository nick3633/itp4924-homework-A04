from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Admin
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class about_net_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    media = TextAreaField('Media (html code)')
    content = TextAreaField('Content (can have html code)', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    submit = SubmitField('Apply')


class about_net_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    media = TextAreaField('Media (html code)')
    content = TextAreaField('Content (can have html code)', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')