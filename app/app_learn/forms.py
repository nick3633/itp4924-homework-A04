from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Admin
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class learn_tutor_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Link')
    submit = SubmitField('Apply')

class learn_tutor_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Link')
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')
    
    
class learn_material_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    link = StringField('Link')
    submit = SubmitField('Apply')

class learn_material_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    link = StringField('Link')
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')
    
    
class learn_res_block_add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL')
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    submit = SubmitField('Apply')

class learn_res_block_edit(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image URL')
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Link')
    link_text = StringField('Link Text')
    editype = SelectField('Action ', choices=[('edit', 'Edit'), ('delete', 'Delete')], validators=[DataRequired()])
    submit = SubmitField('Apply')