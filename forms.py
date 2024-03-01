"""Forms for adopt app."""
from flask_wtf import FlaskForm

from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms import DateTimeField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Pet Species", validators=[InputRequired()])
    photo_url = StringField("Picture of Pet")
    age = SelectField("Age",
        choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'),
                 ('senior', 'Senior')],
        validators=[InputRequired()]
    )
    notes = TextAreaField("Notes about Pet")
