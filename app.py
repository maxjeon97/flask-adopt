"""Flask app for adopt app."""

import os

from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

from dotenv import load_dotenv
load_dotenv()

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

API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJYRmVhb1E3VjBPVjZGcTc4M2l0N2tyUVhzS204YllYemxCZXFGOVNjMkYxaW9nb21MMyIsImp0aSI6ImViNzU4ZjNmNTY5NTBkZjFkZGIzN2Q5ZGZiMjA5ZDA5ZmEzYWYyNmYxY2U1YTRlYWNiMzA0ODNjODE4MmZkNTdmYjZhOTFjNzVjZmQ2ZmYwIiwiaWF0IjoxNzA5MzM4NTMxLCJuYmYiOjE3MDkzMzg1MzEsImV4cCI6MTcwOTM0MjEzMSwic3ViIjoiIiwic2NvcGVzIjpbXX0.Qql_KCMn8tdC_1QNWdeixj7t7xqj4nwnvBFnWAB7PU8Waibcyjsx2kIBp4lnm8vBmq7VVnlkUFBIZuEVCiZLKAYLm7Q0ggG7F3vrtVXm4wXTCb4W-b-dYuF-YcVGZPUc1GoJLZFymAOgLf39F83Kuc9imaLZxBYwaKEqGD3mDoM9cMBq1j1dVs1TXg8d3HJzmqaVGke_NtS7ZUq6wEmLDG0Ao6QMGBkVFBjEqLACAx_6YZ6N1Foh8fNOpuJfOHvIvG_vH1AXUbysDUGJQzQ-_sfaUCelmjmln-jNDN6NjGVSEUjvINbJOmDvtk6orLFACrBkfsboAxOEImcQUnTKeQ'
URL = 'https://api.petfinder.com/v2/animals'

@app.get('/')
def show_homepage():
    """ Renders homepage """
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

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
