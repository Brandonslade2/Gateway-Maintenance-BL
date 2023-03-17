from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, TextAreaField 
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_login import UserMixin
from sqlalchemy import create_engine
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

db = SQLAlchemy()


#Connect to Database
def connect_to_db(flask_app, db_uri="postgresql://postgres:postgres@localhost:5432/GMBL", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = flask_app
    db.init_app(flask_app)
    print("Connected to the db!")

#If executing model.py, this function will run the server.
if __name__ == "__main__":
    from server import app
    app.run(debug=True)
    connect_to_db(app)