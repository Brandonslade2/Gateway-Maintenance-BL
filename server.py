from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from model import connect_to_db, db


app = Flask(__name__)

#Secret Key for Flask application to encrypt session data.
app.secret_key = "dev"

#Database URL for the app. Right now this is set to the local PostgreSQL database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/GMBL'


#-----------------------------------#
#              Routes               #
#-----------------------------------#

#Home Page
@app.route('/')
def home():
    return render_template('home.html')









#When the server is running
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
