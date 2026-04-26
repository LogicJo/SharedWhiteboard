from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    name = StringField("Username: ", validators=[InputRequired(), Length(max=16)])
    room = StringField("Room: ", validators=[InputRequired(), Length(min=4, max=4)])
    join = SubmitField()
    create = SubmitField()
