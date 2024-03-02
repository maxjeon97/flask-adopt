"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pets. Adoption site has many pets"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(30),
        nullable=False
    )

    species = db.Column(
        db.String(30),
        nullable=False
    )

    photo_url = db.Column(
        db.String(100),
        nullable=False,
        default=""
    )

    age = db.Column(
        db.String(6),
        nullable=False
    )

    notes = db.Column(
        db.Text,
        default=""
    )
    # TODO:nullable

    available = db.Column(
        db.Boolean,
        default=True
    )