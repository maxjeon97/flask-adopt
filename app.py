"""Flask app for adopt app."""

import os

from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

from dotenv import load_dotenv
load_dotenv()

from petfinder import update_auth_token_string, get_pet_finder_info

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)



@app.get('/')
def show_homepage():
    """ Renders homepage """
    pets = Pet.query.all()

    token = update_auth_token_string()
    pet_info = get_pet_finder_info(token)

    return render_template('index.html', pets=pets, pet_info = pet_info)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Show add pet form and handle adding pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name = name, species=species,
                  photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f'Put up {name} for adoption!')
        return redirect('/')

    else:
        return render_template("add_pet_form.html",form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edits pet information and handles edit form submission"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        flash(f'{pet.name} information updated!')
        return redirect('/')

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
