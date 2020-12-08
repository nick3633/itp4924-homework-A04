from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Admin
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class comm_method_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL')
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    submit = SubmitField('Add')
    
class comm_method_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL')
    content = TextAreaField('Content ', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')
    
    
class comm_platform_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    icon = StringField('icon URL')
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    submit = SubmitField('Add')
    
class comm_platform_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    icon = StringField('icon URL')
    content = TextAreaField('Content ', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')