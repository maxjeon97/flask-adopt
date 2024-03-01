"""Forms for adopt app."""
from flask_wtf import FlaskForm

from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms import DateTimeField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Pet Species",
        choices=[('cat', 'Cat'), ('dog', 'Dog'),('porcupine','Porcupine')],
        validators=[InputRequired()])
    photo_url = StringField("Picture of Pet", validators=[URL(), Optional()])
    age = SelectField("Age",
        choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'),
                 ('senior', 'Senior')],
        validators=[InputRequired()]
    )
    notes = TextAreaField("Notes about Pet")


class EditPetForm(FlaskForm):
    """Form for editing pet information"""

    photo_url = StringField("Picture of Pet", validators=[URL(), Optional()])
    notes = TextAreaField("Notes about Pet")
    available = BooleanField("Still Available?")
