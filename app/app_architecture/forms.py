from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Admin
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class architecture_item_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField('Apply')


class architecture_ebook_block_add(FlaskForm):
    cover_url = StringField('Cover url', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField('Apply')


class architecture_item_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')


class architecture_ebook_block_edit(FlaskForm):
    cover_url = StringField('Cover url', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')