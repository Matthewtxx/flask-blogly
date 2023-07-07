"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    """site user"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """return full name of the user"""

        return f"{self.first_name} {self.last_name}"
    

class Post(db.Model):
    """blog post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.Foreignkey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """return nicer formatted date"""
        return self.created_at.strftime("%a %b %-d %Y, %-I:%M: %p")

    
def connect_db(app):
    """connect database to provided flask app"""

    db.app = app
    db.init_app(app)