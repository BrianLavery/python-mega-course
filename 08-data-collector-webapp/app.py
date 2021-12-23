from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy # Old code that Ardit uses
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from send_email import send_email
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost:5433/height_collector' # Somehow port is 5433 and not default 5432
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
db = SQLAlchemy(app)

# Inheriting from model class of SQL Alchemy
# We run this from command line in virtual env - we use "from app import db" then "db.create_all()" to create the table
class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['GET','POST']) # Need to explicitly declare non-GET methods
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        # How we send data to db using SQLAlchemy
        # We create a model instance then we pass instance to the DB
        # First check if email exists as it must be unique
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            # Use scalar to get number from query return
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1) # We choose 1 dp
            count = db.session.query(Data.height).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template("index.html",
                            text = "Email address has already been used!")

if __name__ == '__main__':
    app.debug = True
    app.run() # Can pass in specific port here if want