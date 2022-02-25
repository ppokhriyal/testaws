from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class AddUserForm(FlaskForm):
    firstname = StringField('Firstname',validators=[DataRequired()])
    lastname = StringField('Lastname',validators=[DataRequired()])
    submit = SubmitField('Add')